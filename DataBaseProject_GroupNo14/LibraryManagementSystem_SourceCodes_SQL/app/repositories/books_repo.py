# app/repositories/books_repo.py
from __future__ import annotations  # Enables forward-referenced type hints (cleaner typing in large projects)
from app.db import get_conn  # Shared helper: opens a PostgreSQL connection (psycopg)


def list_books(keyword: str = "", language: str = "", limit: int = 500):
    """
    Returns list of tuples:
    (book_id, title, author_name, section_name, publisher_name, language, book_status)
    """
    # Normalize user input (avoid None, trim spaces)
    keyword = (keyword or "").strip()
    language = (language or "").strip()

    # Base query: joins author/section, and publisher is optional (LEFT JOIN)
    sql = """
          SELECT b.book_id,
                 b.title,
                 a.author_name,
                 s.section_name,
                 COALESCE(p.publisher_name, 'N/A') as publisher_name,
                 b.language,
                 b.book_status
          FROM books b
                   JOIN author a ON a.author_id = b.author_id
                   JOIN section s ON s.section_id = b.section_id
                   LEFT JOIN publisher p ON p.publisher_id = b.publisher_id
          """

    # We'll build WHERE clauses dynamically depending on filters
    conditions = []
    params = []

    if keyword:
        # ILIKE = case-insensitive match in PostgreSQL
        conditions.append("b.title ILIKE %s")
        params.append(f"%{keyword}%")  # %...% means "contains"

    if language:
        # Exact match on language (no wildcard)
        conditions.append("b.language = %s")
        params.append(language)

    if conditions:
        # Add the WHERE part only if we actually have filters
        sql += " WHERE " + " AND ".join(conditions)

    # Always order results in a predictable way; limit protects UI from huge datasets
    sql += " ORDER BY b.title LIMIT %s"
    params.append(limit)

    # Use context managers so connection/cursor are closed safely
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)  # params are bound safely (prevents SQL injection)
            return cur.fetchall()


def get_languages():
    """Get list of unique languages from books"""
    # DISTINCT returns each language once; ORDER BY keeps dropdown sorted
    sql = """
          SELECT DISTINCT language
          FROM books
          WHERE language IS NOT NULL
          ORDER BY language
          """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            # Each row is a tuple like ("English",) so we take row[0]
            return [row[0] for row in cur.fetchall()]


def get_books_stats():
    """Get statistics for books dashboard"""
    # FILTER lets us count subsets in a single query (PostgreSQL feature)
    sql = """
          SELECT COUNT(*) as total,
                 COUNT(*)    FILTER (WHERE book_status = 'available') as available, COUNT(*) FILTER (WHERE book_status = 'borrowed') as borrowed, COUNT(*) FILTER (WHERE book_status = 'maintenance') as maintenance
          FROM books
          """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()
            # Return a small dict to make UI code readable
            return {
                "total": row[0],
                "available": row[1],
                "borrowed": row[2],
                "maintenance": row[3]
            }


def get_authors():
    """Get list of author names"""
    # Used for dropdown values in Add/Edit book dialogs
    sql = "SELECT author_name FROM author ORDER BY author_name"
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [row[0] for row in cur.fetchall()]


def get_sections():
    """Get list of section names"""
    # Used for dropdown values in Add/Edit book dialogs
    sql = "SELECT section_name FROM section ORDER BY section_name"
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [row[0] for row in cur.fetchall()]


def get_publishers():
    """Get list of publisher names"""
    # Used for dropdown values in Add/Edit book dialogs
    sql = "SELECT publisher_name FROM publisher ORDER BY publisher_name"
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [row[0] for row in cur.fetchall()]

def add_book(data: dict) -> bool:
    """Add a new book"""
    try:
        # We store author/section/publisher as IDs, but UI provides names.
        # This INSERT uses subqueries to translate names -> IDs.
        sql = """
              INSERT INTO books (title, author_id, section_id, publisher_id, language, book_status)
              VALUES (%s,
                      (SELECT author_id FROM author WHERE author_name = %s),
                      (SELECT section_id FROM section WHERE section_name = %s),
                      (SELECT publisher_id FROM publisher WHERE publisher_name = %s),
                      %s,
                      %s)
              """

        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (
                    data["title"],
                    data["author"],
                    data["section"],
                    data["publisher"],
                    data["language"] or None,  # empty string -> NULL in DB
                    data["status"]
                ))
                conn.commit()  # persist the insert
                return True
    except Exception as e:
        # Printed for debugging; UI shows a generic failure message
        print(f"Error adding book: {e}")
        return False


def update_book(data: dict) -> dict:
    """
    Update an existing book
    Returns: {"success": bool, "message": str}
    """
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                # First: verify the book exists and read its current status
                cur.execute(
                    "SELECT book_status FROM books WHERE book_id = %s",
                    (data["book_id"],)
                )
                result = cur.fetchone()

                if not result:
                    return {"success": False, "message": "Book not found!"}

                current_db_status = result[0]

                # Safety rule:
                # If a book is currently borrowed, staff cannot manually change it to another status.
                # Status must be updated via the Loans -> Return workflow.
                if current_db_status == "borrowed" and data["status"] != "borrowed":
                    return {
                        "success": False,
                        "message": "Cannot change status of a borrowed book. Please use Loans → Return process first."
                    }

                # Normalize language: empty -> NULL (keeps DB clean)
                language_value = data["language"] if data["language"] else None

                # Normal update (again, translate UI names -> IDs via subqueries)
                sql = """
                      UPDATE books
                      SET title        = %s,
                          author_id    = (SELECT author_id FROM author WHERE author_name = %s),
                          section_id   = (SELECT section_id FROM section WHERE section_name = %s),
                          publisher_id = (SELECT publisher_id FROM publisher WHERE publisher_name = %s),
                          language     = %s,
                          book_status  = %s
                      WHERE book_id = %s
                      """

                cur.execute(sql, (
                    data["title"],
                    data["author"],
                    data["section"],
                    data["publisher"],
                    language_value,
                    data["status"],
                    data["book_id"]
                ))

                conn.commit()  # persist changes
                return {"success": True, "message": "Book updated successfully!"}

    except Exception as e:
        # If DB triggers or constraints fail, we return a user-friendly message
        error_msg = str(e)
        print(f"Error updating book: {error_msg}")

        # Trigger/constraint specific handling:
        # If a trigger blocks changing availability due to active loan, explain it clearly.
        if "prevent_manual_available" in error_msg or "active loan" in error_msg.lower():
            return {
                "success": False,
                "message": "Cannot change book status: This book has an active loan. Please return the book first via Loans → Return."
            }

        return {"success": False, "message": f"Failed to update book: {error_msg}"}


def delete_book(book_id: int) -> bool:
    """Delete a book"""
    try:
        # Simple delete by primary key
        sql = "DELETE FROM books WHERE book_id = %s"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (book_id,))
                conn.commit()
                return True
    except Exception as e:
        # This can fail if foreign keys exist (e.g., loans reference this book)
        print(f"Error deleting book: {e}")
        return False
