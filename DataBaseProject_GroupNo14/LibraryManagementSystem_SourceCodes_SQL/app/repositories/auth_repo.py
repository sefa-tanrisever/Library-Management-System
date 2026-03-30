# app/repositories/auth_repo.py

from __future__ import annotations  # Helps with type hints and forward references
from app.db import get_conn  # Shared DB connection helper (psycopg3)


def authenticate_user(email: str, password: str):
    """
    Authenticate user against librarian table
    Returns user data if successful, None if failed
    """
    try:
        # Parameterized SQL (using %s placeholders) protects against SQL injection
        sql = """
              SELECT l.librarian_id, \
                     l.name, \
                     l.email, \
                     p.permission_name
              FROM librarian l
                       LEFT JOIN permission p ON p.permission_id = l.permission_id
              WHERE l.email = %s \
                AND l.password = %s \
              """

        # Context manager closes connection automatically (commit/rollback behavior handled by psycopg)
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (email, password))  # tuple binds to %s placeholders
                result = cur.fetchone()              # one row or None

                # Convert DB row into the dict format used by the UI layer
                if result:
                    return {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "role": result[3] or "staff"  # fallback if permission is missing
                    }
                return None
    except Exception as e:
        # Keep errors visible during development (UI handles None as "login failed")
        print(f"Authentication error: {e}")
        return None


def authenticate_member(email: str, password: str):
    """
    Authenticate member (alternative authentication)
    """
    try:
        # Same idea as staff auth, but this time using the member table
        sql = """
              SELECT m.member_id, \
                     (m.first_name || ' ' || m.last_name) as name, \
                     m.email, \
                     p.permission_name
              FROM member m
                       LEFT JOIN permission p ON p.permission_id = m.permission_id
              WHERE m.email = %s \
                AND m.password = %s \
              """

        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (email, password))
                result = cur.fetchone()

                if result:
                    return {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2],
                        "role": result[3] or "member"  # members default to "member"
                    }
                return None
    except Exception as e:
        print(f"Member authentication error: {e}")
        return None
