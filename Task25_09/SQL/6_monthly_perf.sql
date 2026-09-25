-- DISPLAY MONTHLY PERFORMANCE REPORT
SELECT *
FROM Monthly_Performance_Report
ORDER BY Booking_Month, Movie_Name;

-- MOVIE BOOKING REPORT USING JOINS
SELECT
    b.Booking_ID,
    c.Customer_Name,
    m.Movie_Name,
    t.Theater_Name,
    t.Location,
    s.Show_Date,
    s.Show_Time,
    b.Tickets,
    s.Ticket_Price,
    (b.Tickets * s.Ticket_Price) AS Total_Amount
FROM Bookings b
JOIN Customers c
    ON b.Customer_ID = c.Customer_ID
JOIN Shows s
    ON b.Show_ID = s.Show_ID
JOIN Movies m
    ON s.Movie_ID = m.Movie_ID
JOIN Theaters t
    ON s.Theater_ID = t.Theater_ID
ORDER BY b.Booking_ID;