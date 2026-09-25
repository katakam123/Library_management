-- EMPLOYEE-DEPARTMENT JOIN REPORT
SELECT
    e.Employee_ID,
    e.Employee_Name,
    d.Department_Name,
    e.Salary
FROM Employees e
JOIN Departments d
    ON e.Department_ID = d.Department_ID
ORDER BY d.Department_Name, e.Employee_Name;

-- EMPLOYEES WITH SALARY ABOVE AVERAGE
-- Using Subquery
SELECT
    Employee_ID,
    Employee_Name,
    Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);
