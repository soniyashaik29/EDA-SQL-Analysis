-- Top 5 products by revenue
SELECT ProductName, SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY ProductName
ORDER BY TotalRevenue DESC
LIMIT 5;

-- Monthly user acquisition trend
SELECT DATE_TRUNC('month', SignupDate) AS Month, COUNT(UserID) AS NewUsers
FROM Users
GROUP BY Month
ORDER BY Month;
