--05_integrity.sql
-- 1) A book can have at most ONE active loan at a time
-- Active loan = return_date IS NULL
CREATE UNIQUE INDEX IF NOT EXISTS ux_loan_one_active_per_book
ON loan(book_id)
WHERE return_date IS NULL;


-- 2) Prevent manually setting a borrowed book to 'available' while it still has an active loan
CREATE OR REPLACE FUNCTION prevent_manual_available()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
    -- If someone tries to change borrowed -> available
    IF OLD.book_status = 'borrowed' AND NEW.book_status = 'available' THEN

        -- Check if there is any active loan for this book
        IF EXISTS (
            SELECT 1
            FROM loan l
            WHERE l.book_id = OLD.book_id
              AND l.return_date IS NULL
              AND l.status IN ('borrowed', 'overdue')
        ) THEN
            RAISE EXCEPTION
                'Cannot set book_status to available while there is an active loan for this book (book_id=%). Use the Loans -> Return process.',
                OLD.book_id;
        END IF;

    END IF;

    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_books_prevent_manual_available ON books;

CREATE TRIGGER trg_books_prevent_manual_available
BEFORE UPDATE OF book_status ON books
FOR EACH ROW
EXECUTE FUNCTION prevent_manual_available();
