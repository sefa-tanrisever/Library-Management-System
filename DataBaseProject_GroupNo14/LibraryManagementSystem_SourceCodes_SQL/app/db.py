# app/db.py

from __future__ import annotations  # Allows forward references in type hints (py<3.11 friendly)

import os  # Used to read environment variables (DB_HOST, DB_USER, etc.)
from pathlib import Path  # Safer path handling across OS (Windows/macOS/Linux)

import psycopg #Psycopg3 is a reliable PostgreSQL adapter for Python
from psycopg.rows import tuple_row  # Makes cursor results come back as plain tuples
from dotenv import load_dotenv  # Loads variables from a local .env file


# Proje kökünü (Library Management System) garanti bul:
# app/db.py -> app/.. = proje kökü
# Find the project root reliably:
# app/db.py -> go up one level to reach the project root directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"  # Where we expect DB credentials to live

# .env dosyasını kesin yükle
# Always load the .env file so local development works consistently.
load_dotenv(ENV_PATH)


def _required_env(name: str) -> str:
    """Read a required environment variable, failing fast with a clear message if missing."""
    value = os.getenv(name)
    if value is None or value.strip() == "":
        # This error is intentionally specific to help debugging when .env is missing/misconfigured
        raise RuntimeError(f"{name} is missing in .env (expected at: {ENV_PATH})")
    return value.strip()

#use psycopg3 library to take data from database.
def get_conn():
    """
    Create and return a psycopg3 connection.
    row_factory=tuple_row => fetchone()/fetchall() returns tuple-based rows (simple + consistent).
    """
    # Pull connection settings from .env (raises RuntimeError if any is missing)
    host = _required_env("DB_HOST")
    port = int(_required_env("DB_PORT"))
    dbname = _required_env("DB_NAME")
    user = _required_env("DB_USER")
    password = _required_env("DB_PASSWORD")

    # Return a live connection (callers usually use: `with get_conn() as conn: ...`)
    return psycopg.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password,
        row_factory=tuple_row,
    )
