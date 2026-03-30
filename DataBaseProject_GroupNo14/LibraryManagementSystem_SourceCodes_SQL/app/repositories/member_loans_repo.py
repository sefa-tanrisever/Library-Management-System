# app/repositories/member_loans_repo.py
from __future__ import annotations  # Enables forward-referenced type hints (cleaner typing)
from app.db import get_conn  # Shared helper: opens a PostgreSQL connection (psycopg)


def get_member_loans(member_id: int):
    """
    Get all loans for a specific member
    Returns: (loan_id, book_title, borrow_date, due_date, return_date, status)
    """
    # This query is used for "My Loans" page (member-only view)
    sql = """
          SELECT l.loan_id,
                 b.title              as book_title,
                 l.borrow_date,
                 l.due_date,
                 l.return_date,
                 l.status
          FROM loan l
                   JOIN books b ON b.book_id = l.book_id
          WHERE l.member_id = %s
          ORDER BY l.borrow_date DESC
          """

    with get_conn() as conn:
        with conn.cursor() as cur:
            # Parameterized query prevents SQL injection
            cur.execute(sql, (member_id,))
            return cur.fetchall()


def get_member_loan_stats(member_id: int):
    """
    Get loan statistics for a specific member
    """
    # Used to build the member dashboard cards (total, active, overdue, returned)
    sql = """
          SELECT COUNT(*)                                          as total,
                 COUNT(*) FILTER (WHERE status = 'borrowed')       as active,
                 COUNT(*) FILTER (WHERE status = 'overdue')        as overdue,
                 COUNT(*) FILTER (WHERE status = 'returned')       as returned
          FROM loan
          WHERE member_id = %s
          """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (member_id,))
            row = cur.fetchone()
            return {
                "total": row[0],
                "active": row[1],
                "overdue": row[2],
                "returned": row[3]
            }
