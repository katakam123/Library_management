-- CREATE DELETE TRIGGER
-- Log deleted employee records
DELIMITER $$

CREATE TRIGGER after_employee_delete
AFTER DELETE ON Employees
FOR EACH ROW
BEGIN

    INSERT INTO Employee_Delete_Log
    (
        Employee_ID,
        Employee_Name,
        Department_ID,
        Salary
    )
    VALUES
    (
        OLD.Employee_ID,
        OLD.Employee_Name,
        OLD.Department_ID,
        OLD.Salary
    );

END$$

DELIMITER ;

-- TEST DELETE TRIGGER
-- Delete employee ID 3

DELETE FROM Employees
WHERE Employee_ID = 3;

-- Check deleted employee log
SELECT *
FROM Employee_Delete_Log;