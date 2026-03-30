# app/repositories/members_repo.py
from __future__ import annotations  # Enables forward-referenced type hints (cleaner typing)
from app.db import get_conn  # Shared helper: opens a PostgreSQL connection (psycopg)


def list_members(keyword: str = "", limit: int = 500):
    """
    Returns list of tuples:
    (member_id, full_name, phone_number, email, permission_name)
    """
    # Normalize user input (avoid None, trim spaces)
    keyword = (keyword or "").strip()

    # Base query: permission is optional (LEFT JOIN) so COALESCE protects UI display
    sql = """
          SELECT m.member_id, \
                 (m.first_name || ' ' || m.last_name) as full_name, \
                 m.phone_number, \
                 m.email, \
                 COALESCE(p.permission_name, 'N/A')   as permission_name
          FROM member m
                   LEFT JOIN permission p ON p.permission_id = m.permission_id \
          """

    params = []
    if keyword:
        # Search by first name, last name, or email (ILIKE = case-insensitive)
        sql += """ WHERE 
            m.first_name ILIKE %s OR 
            m.last_name ILIKE %s OR 
            m.email ILIKE %s
        """
        params.extend([f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"])

    # Keep output stable + prevent huge response sets
    sql += " ORDER BY m.first_name, m.last_name LIMIT %s"
    params.append(limit)

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()


def get_members_stats():
    """Get statistics for members dashboard"""
    # Note: "new_this_month" here is approximated by last 10 member_ids (simple demo logic)
    sql = """
          SELECT COUNT(*)                    as total, \
                 COUNT(DISTINCT l.member_id) as active_borrowers, \
                 COUNT(*)                       FILTER (
                WHERE m.member_id >= (
                    SELECT MAX(member_id) - 10 FROM member
                )
            ) as new_this_month
          FROM member m
                   LEFT JOIN loan l ON l.member_id = m.member_id
              AND l.return_date IS NULL \
          """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()
            return {
                "total": row[0],
                "active": row[1],
                "new_this_month": row[2]
            }


def add_member(data: dict) -> bool:
    """Add a new member"""
    try:
        # permission_name from UI is converted to permission_id via subquery
        sql = """
              INSERT INTO member (first_name, last_name, phone_number, email, password, permission_id)
              VALUES (%s, %s, %s, %s, %s, \
                      (SELECT permission_id FROM permission WHERE permission_name = %s)) \
              """

        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (
                    data["first_name"],
                    data["last_name"],
                    data["phone"] or None,  # empty -> NULL (phone is optional)
                    data["email"],
                    data["password"],
                    data["permission"]
                ))
                conn.commit()  # persist insert
                return True
    except Exception as e:
        # Often fails on unique email constraint (email already exists)
        print(f"Error adding member: {e}")
        return False


def update_member(data: dict) -> bool:
    """Update an existing member"""
    try:
        # Build SQL dynamically based on whether password is provided
        # (If password is empty, we keep the existing password in DB.)
        if data["password"]:
            sql = """
                  UPDATE member
                  SET first_name    = %s,
                      last_name     = %s,
                      phone_number  = %s,
                      email         = %s,
                      password      = %s,
                      permission_id = (SELECT permission_id FROM permission WHERE permission_name = %s)
                  WHERE member_id = %s \
                  """
            params = (
                data["first_name"],
                data["last_name"],
                data["phone"] or None,
                data["email"],
                data["password"],
                data["permission"],
                data["member_id"]
            )
        else:
            sql = """
                  UPDATE member
                  SET first_name    = %s,
                      last_name     = %s,
                      phone_number  = %s,
                      email         = %s,
                      permission_id = (SELECT permission_id FROM permission WHERE permission_name = %s)
                  WHERE member_id = %s \
                  """
            params = (
                data["first_name"],
                data["last_name"],
                data["phone"] or None,
                data["email"],
                data["permission"],
                data["member_id"]
            )

        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()  # persist update
                return True
    except Exception as e:
        print(f"Error updating member: {e}")
        return False


def delete_member(member_id: int) -> bool:
    """Delete a member"""
    try:
        # Delete by primary key; may fail if foreign keys exist (active loans, etc.)
        sql = "DELETE FROM member WHERE member_id = %s"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (member_id,))
                conn.commit()
                return True
    except Exception as e:
        print(f"Error deleting member: {e}")
        return False
