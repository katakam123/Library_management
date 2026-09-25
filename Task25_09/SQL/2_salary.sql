-- TOP 3 HIGHEST SALARIES
SELECT
    Employee_ID,
    Employee_Name,
    Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 3;

-- SECOND HIGHEST SALARY
SELECT MAX(Salary) AS Second_Highest_Salary
FROM Employees
WHERE Salary < (
    SELECT MAX(Salary)
    FROM Employees
);

-- DUPLICATE RECORDS
-- Find duplicate salary values
SELECT
    Salary,
    COUNT(*) AS Duplicate_Count
FROM Employees
GROUP BY Salary
HAVING COUNT(*) > 1;
