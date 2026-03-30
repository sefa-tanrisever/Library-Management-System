-- 06_business_rules.sql

--  Users with overdue books cannot borrow new books

CREATE OR REPLACE FUNCTION check_member_has_overdue()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if the member has any overdue loans
    IF EXISTS (
        SELECT 1
        FROM loan
        WHERE member_id = NEW.member_id
          AND return_date IS NULL
          AND status = 'overdue'
    ) THEN
        RAISE EXCEPTION 
            'Member ID % has overdue books and cannot borrow new books until they are returned.',
            NEW.member_id;
    END IF;
    
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_loan_check_overdue ON loan;

CREATE TRIGGER trg_loan_check_overdue
BEFORE INSERT ON loan
FOR EACH ROW
EXECUTE FUNCTION check_member_has_overdue();



--  A user can borrow a maximum of 3 books at the same time

CREATE OR REPLACE FUNCTION check_member_loan_limit()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    active_loans_count INTEGER;
BEGIN
    -- Count active loans (not returned) for this member
    SELECT COUNT(*)
    INTO active_loans_count
    FROM loan
    WHERE member_id = NEW.member_id
      AND return_date IS NULL
      AND status IN ('borrowed', 'overdue');
    
    -- Check if member already has 3 active loans
    IF active_loans_count >= 3 THEN
        RAISE EXCEPTION 
            'Member ID % has reached the maximum limit of 3 active loans. Current active loans: %',
            NEW.member_id, active_loans_count;
    END IF;
    
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_loan_check_limit ON loan;

CREATE TRIGGER trg_loan_check_limit
BEFORE INSERT ON loan
FOR EACH ROW
EXECUTE FUNCTION check_member_loan_limit();



-- HELPER FUNCTION: Check if member can borrow books

CREATE OR REPLACE FUNCTION can_member_borrow(p_member_id INTEGER)
RETURNS TABLE (
    can_borrow BOOLEAN,
    reason TEXT,
    active_loans INTEGER,
    overdue_loans INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_active_count INTEGER;
    v_overdue_count INTEGER;
BEGIN
    -- Count active loans
    SELECT COUNT(*)
    INTO v_active_count
    FROM loan
    WHERE member_id = p_member_id
      AND return_date IS NULL
      AND status IN ('borrowed', 'overdue');
    
    -- Count overdue loans
    SELECT COUNT(*)
    INTO v_overdue_count
    FROM loan
    WHERE member_id = p_member_id
      AND return_date IS NULL
      AND status = 'overdue';
    
    -- Determine if member can borrow
    IF v_overdue_count > 0 THEN
        RETURN QUERY SELECT 
            FALSE, 
            'Cannot borrow: Member has ' || v_overdue_count || ' overdue book(s)',
            v_active_count,
            v_overdue_count;
    ELSIF v_active_count >= 3 THEN
        RETURN QUERY SELECT 
            FALSE, 
            'Cannot borrow: Member has reached the maximum limit of 3 active loans',
            v_active_count,
            v_overdue_count;
    ELSE
        RETURN QUERY SELECT 
            TRUE, 
            'Member can borrow ' || (3 - v_active_count) || ' more book(s)',
            v_active_count,
            v_overdue_count;
    END IF;
END;
$$;


