# app/repositories/overdue_repo.py
from __future__ import annotations  # Enables forward-referenced type hints (cleaner typing)
from app.db import get_conn  # Shared helper: opens a PostgreSQL connection (psycopg)


def list_overdue_loans(keyword: str = ""):
    """
    Get list of overdue loans using the database function
    Returns: (loan_id, member_name, member_email, book_title, due_date, days_overdue)
    """
    # Normalize search input
    keyword = (keyword or "").strip()

    # The database function list_overdue_loans() returns a table-like result set.
    # We can filter its output with WHERE just like a normal SELECT.
    sql = "SELECT * FROM list_overdue_loans()"

    if keyword:
        # Search across member name/email and book title (ILIKE = case-insensitive)
        sql += """ 
            WHERE member_name ILIKE %s 
            OR member_email ILIKE %s 
            OR book_title ILIKE %s
        """
        params = [f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"]
    else:
        params = []

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()

            # The DB function returns more columns than the UI table needs.
            # We reshape each row into the exact tuple format used by OverdueView.
            return [
                (
                    row[0],  # loan_id
                    row[2],  # member_name
                    row[3],  # member_email
                    row[5],  # book_title
                    row[6],  # due_date
                    row[7]  # days_overdue
                )
                for row in rows
            ]


def mark_loans_overdue() -> bool:
    """
    Call the stored procedure to mark overdue loans
    """
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                # Stored procedure updates loan.status to 'overdue' where due_date has passed
                cur.execute("CALL mark_overdue_loans()")
                conn.commit()  # persist procedure changes
                return True
    except Exception as e:
        print(f"Error marking loans overdue: {e}")
        return False
