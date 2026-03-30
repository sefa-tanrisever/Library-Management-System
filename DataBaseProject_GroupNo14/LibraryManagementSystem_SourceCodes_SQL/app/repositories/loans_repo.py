# app/repositories/loans_repo.py
from __future__ import annotations  # Enables forward-referenced type hints (cleaner typing)
from datetime import datetime, timedelta  # Used for borrow_date and due_date calculations
from app.db import get_conn  # Shared helper: opens a PostgreSQL connection (psycopg)


def check_member_can_borrow(member_id: int) -> dict:
    """
    Check if member can borrow books
    Returns: {"can_borrow": bool, "reason": str, "active_loans": int, "overdue_loans": int}
    """
    # Calls a DB function (business logic lives in PostgreSQL for consistency)
    sql = "SELECT * FROM can_member_borrow(%s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (member_id,))
            row = cur.fetchone()
            # The function returns multiple columns; we map them to a friendly dict
            return {
                "can_borrow": row[0],
                "reason": row[1],
                "active_loans": row[2],
                "overdue_loans": row[3]
            }

def list_loans(keyword: str = "", status_filter: str = "", limit: int = 500):
    """
    Returns list of tuples:
    (loan_id, member_name, book_title, borrow_date, due_date, return_date, status)
    """
    # Normalize filters (avoid None, trim spaces)
    keyword = (keyword or "").strip()
    status_filter = (status_filter or "").strip().lower()

    # Base query: joins loan -> member + books to show readable info in the UI
    sql = """
          SELECT l.loan_id, \
                 (m.first_name || ' ' || m.last_name) as member_name, \
                 b.title                              as book_title, \
                 l.borrow_date, \
                 l.due_date, \
                 l.return_date, \
                 l.status
          FROM loan l
                   JOIN member m ON m.member_id = l.member_id
                   JOIN books b ON b.book_id = l.book_id \
          """

    # Build WHERE clauses dynamically based on filters
    conditions = []
    params = []

    if keyword:
        # Search across member first/last name and book title
        conditions.append("""
            (m.first_name ILIKE %s OR 
             m.last_name ILIKE %s OR 
             b.title ILIKE %s)
        """)
        params.extend([f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"])

    if status_filter:
        # Status is expected to match values like 'borrowed', 'returned', 'overdue'
        conditions.append("l.status = %s")
        params.append(status_filter)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    # Most recent loans first; limit keeps UI fast
    sql += " ORDER BY l.borrow_date DESC LIMIT %s"
    params.append(limit)

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()


def get_loans_stats():
    """Get statistics for loans dashboard"""
    # Similar to books stats: compute multiple counts in one query using FILTER
    sql = """
          SELECT COUNT(*) as total, \
                 COUNT(*)    FILTER (WHERE status = 'borrowed') as borrowed, COUNT(*) FILTER (WHERE status = 'overdue') as overdue, COUNT(*) FILTER (WHERE status = 'returned') as returned
          FROM loan \
          """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()
            return {
                "total": row[0],
                "borrowed": row[1],
                "overdue": row[2],
                "returned": row[3]
            }


def get_active_members():
    """Get list of members for dropdown (format: "Name (ID: X)")"""
    # UI dropdown needs a readable label but also contains the ID for parsing later
    sql = """
          SELECT member_id, \
                 first_name || ' ' || last_name as full_name
          FROM member
          ORDER BY first_name, last_name \
          """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [f"{row[1]} (ID: {row[0]})" for row in cur.fetchall()]


def get_available_books():
    """Get list of available books for dropdown (format: "Title (ID: X)")"""
    # Only books with status 'available' can be borrowed
    sql = """
          SELECT book_id, \
                 title
          FROM books
          WHERE book_status = 'available'
          ORDER BY title \
          """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [f"{row[1]} (ID: {row[0]})" for row in cur.fetchall()]


def create_loan(data: dict) -> dict:
    """
    Create a new loan
    Returns: {"success": bool, "message": str}
    """
    try:
        # First: enforce borrowing rules (max active loans, no overdue, etc.)
        check_result = check_member_can_borrow(data["member_id"])

        if not check_result["can_borrow"]:
            return {
                "success": False,
                "message": check_result["reason"]
            }

        # Loan dates (stored as DATE in DB; UI shows them nicely)
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=data["days"])

        with get_conn() as conn:
            with conn.cursor() as cur:
                # Create loan record (status starts as 'borrowed')
                cur.execute("""
                            INSERT INTO loan (member_id, book_id, borrow_date, due_date, status)
                            VALUES (%s, %s, %s, %s, 'borrowed')
                            """, (
                                data["member_id"],
                                data["book_id"],
                                borrow_date,
                                due_date
                            ))

                # Keep books table in sync: mark the book as borrowed
                cur.execute("""
                            UPDATE books
                            SET book_status = 'borrowed'
                            WHERE book_id = %s
                            """, (data["book_id"],))

                # Commit both operations as one transaction
                conn.commit()
                return {
                    "success": True,
                    "message": "Loan created successfully!"
                }
    except Exception as e:
        # If DB rejects the insert/update, convert into a user-friendly response
        error_msg = str(e)
        print(f"Error creating loan: {error_msg}")

        # Parse database constraint errors (simple keyword-based mapping)
        if "overdue books" in error_msg.lower():
            return {
                "success": False,
                "message": "This member has overdue books and cannot borrow until they are returned."
            }
        elif "maximum limit" in error_msg.lower():
            return {
                "success": False,
                "message": "This member has reached the maximum limit of 3 active loans."
            }
        else:
            return {
                "success": False,
                "message": f"Failed to create loan: {error_msg}"
            }


def return_loan(loan_id: int) -> bool:
    """Mark a loan as returned"""
    try:
        # Return date is set to today's date
        return_date = datetime.now().date()

        with get_conn() as conn:
            with conn.cursor() as cur:
                # We need the book_id to update books.book_status back to 'available'
                cur.execute("""
                            SELECT book_id
                            FROM loan
                            WHERE loan_id = %s
                            """, (loan_id,))
                result = cur.fetchone()
                if not result:
                    # No such loan_id
                    return False

                book_id = result[0]

                # Mark loan as returned (also store return_date)
                cur.execute("""
                            UPDATE loan
                            SET return_date = %s,
                                status      = 'returned'
                            WHERE loan_id = %s
                            """, (return_date, loan_id))

                # Update book status back to available so it can be borrowed again
                cur.execute("""
                            UPDATE books
                            SET book_status = 'available'
                            WHERE book_id = %s
                            """, (book_id,))

                # Commit both updates
                conn.commit()
                return True
    except Exception as e:
        print(f"Error returning loan: {e}")
        return False
