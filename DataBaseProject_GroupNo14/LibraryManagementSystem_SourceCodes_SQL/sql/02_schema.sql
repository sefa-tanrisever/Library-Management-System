-- 02_schema.sql 

CREATE TABLE permission (
    permission_id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    permission_name VARCHAR(50) NOT NULL UNIQUE,
    description     TEXT
);

CREATE TABLE section (
    section_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    section_name    VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE publisher (
    publisher_id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    publisher_name      VARCHAR(150) NOT NULL UNIQUE,
    publisher_country   VARCHAR(80)
);

CREATE TABLE author (
    author_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    author_name     VARCHAR(150) NOT NULL,
    date_of_birth   DATE
);

CREATE TABLE books (
    book_id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title           VARCHAR(250) NOT NULL,
    author_id       INTEGER NOT NULL REFERENCES author(author_id) ON DELETE RESTRICT,
    section_id      INTEGER NOT NULL REFERENCES section(section_id) ON DELETE RESTRICT,
    publisher_id    INTEGER REFERENCES publisher(publisher_id) ON DELETE SET NULL,
    language        VARCHAR(50),
    book_status     VARCHAR(20) NOT NULL DEFAULT 'available',
    CONSTRAINT chk_book_status
        CHECK (book_status IN ('available', 'borrowed', 'reserved', 'lost', 'maintenance'))
);

CREATE TABLE member (
    member_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name      VARCHAR(80) NOT NULL,
    last_name       VARCHAR(80) NOT NULL,
    phone_number    VARCHAR(30),
    email           VARCHAR(255) NOT NULL UNIQUE,
    password        VARCHAR(255) NOT NULL,
    permission_id   INTEGER REFERENCES permission(permission_id) ON DELETE SET NULL
);

CREATE TABLE librarian (
    librarian_id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            VARCHAR(120) NOT NULL,
    phone_number    VARCHAR(30),
    email           VARCHAR(255) NOT NULL UNIQUE,
    password        VARCHAR(255) NOT NULL,
    permission_id   INTEGER REFERENCES permission(permission_id) ON DELETE SET NULL
);

CREATE TABLE loan (
    loan_id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_id       INTEGER NOT NULL REFERENCES member(member_id) ON DELETE CASCADE,
    book_id         INTEGER NOT NULL REFERENCES books(book_id) ON DELETE RESTRICT,
    borrow_date     DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date        DATE NOT NULL,
    return_date     DATE,
    status          VARCHAR(20) NOT NULL DEFAULT 'borrowed',
    CONSTRAINT chk_loan_status
        CHECK (status IN ('borrowed', 'returned', 'overdue')),
    CONSTRAINT chk_loan_dates
        CHECK (due_date >= borrow_date AND (return_date IS NULL OR return_date >= borrow_date))
);
