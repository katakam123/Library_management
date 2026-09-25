-- Products with total quantity above average

SELECT
    p.Product_ID,
    p.Product_Name,
    SUM(s.Quantity) AS Total_Quantity
FROM Products p
JOIN Sales s
    ON p.Product_ID = s.Product_ID
GROUP BY p.Product_ID, p.Product_Name
HAVING SUM(s.Quantity) > (
    SELECT AVG(Total_Quantity)
    FROM
    (
        SELECT
            Product_ID,
            SUM(Quantity) AS Total_Quantity
        FROM Sales
        GROUP BY Product_ID
    ) AS Sales_Summary
);

-- PRODUCT WITH HIGHEST TOTAL SALES QUANTITY
-- Using Subquery

SELECT
    p.Product_Name,
    s.Total_Quantity
FROM Products p
JOIN
(
    SELECT
        Product_ID,
        SUM(Quantity) AS Total_Quantity
    FROM Sales
    GROUP BY Product_ID
) s
    ON p.Product_ID = s.Product_ID
WHERE s.Total_Quantity = (
    SELECT MAX(Total_Quantity)
    FROM
    (
        SELECT
            Product_ID,
            SUM(Quantity) AS Total_Quantity
        FROM Sales
        GROUP BY Product_ID
    ) AS Sales_Total
);
