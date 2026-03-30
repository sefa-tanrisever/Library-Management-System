-- 04_routines.sql
--stored function
CREATE OR REPLACE FUNCTION list_overdue_loans(p_as_of_date DATE DEFAULT CURRENT_DATE)
RETURNS TABLE (
    loan_id        INT,
    member_id      INT,
    member_name    TEXT,
    member_email   TEXT,
    book_id        INT,
    book_title     TEXT,
    due_date       DATE,
    days_overdue   INT
)
LANGUAGE sql
AS $$
    SELECT
        l.loan_id,
        m.member_id,
        (m.first_name || ' ' || m.last_name) AS member_name,
        m.email AS member_email,
        b.book_id,
        b.title AS book_title,
        l.due_date,
        (p_as_of_date - l.due_date)::INT AS days_overdue
    FROM loan l
    JOIN member m ON m.member_id = l.member_id
    JOIN books  b ON b.book_id = l.book_id
    WHERE l.return_date IS NULL
      AND l.due_date < p_as_of_date
    ORDER BY days_overdue DESC, l.due_date ASC;
$$;
--stored procedure. this procedure is saved here and can be infinitely called from overdue_repo.py
CREATE OR REPLACE PROCEDURE mark_overdue_loans(p_as_of_date DATE DEFAULT CURRENT_DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE loan
    SET status = 'overdue'
    WHERE return_date IS NULL
      AND due_date < p_as_of_date
      AND status <> 'overdue';
END;
$$;
