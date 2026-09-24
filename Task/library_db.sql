-- LIBRARY MANAGEMENT SYSTEM

-- CREATE DATABASE
CREATE DATABASE library_db;

USE library_db;

-- CREATE BOOKS TABLE
CREATE TABLE Books (
    Book_ID INT PRIMARY KEY,
    Book_Name VARCHAR(100) NOT NULL,
    Author_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Published_Year INT
);

-- CREATE MEMBERS TABLE
CREATE TABLE Members (
    Member_ID INT PRIMARY KEY,
    Member_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) UNIQUE
);

-- CREATE BORROW_RECORDS TABLE
CREATE TABLE Borrow_Records (
    Borrow_ID INT PRIMARY KEY,
    Book_ID INT NOT NULL,
    Member_ID INT NOT NULL,
    Borrow_Date DATE NOT NULL,
    Return_Date DATE,

    FOREIGN KEY (Book_ID)
        REFERENCES Books(Book_ID),

    FOREIGN KEY (Member_ID)
        REFERENCES Members(Member_ID)
);

-- INSERT BOOK RECORDS
INSERT INTO Books
(Book_ID, Book_Name, Author_Name, Category, Published_Year)
VALUES
(1, 'Python ', 'John Smith', 'Programming', 2022),
(2, 'SQL ', 'Robert Brown', 'Database', 2021),
(3, 'Data Science ', 'David Miller', 'Data Science', 2020),
(4, 'Web Development', 'James Wilson', 'Programming', 2020),
(5, 'Machine Learning', 'Andrew Clark', 'AI', 2023);

-- INSERT MEMBER RECORDS
INSERT INTO Members
(Member_ID, Member_Name, Email, Phone)
VALUES
(1, 'Rahul', 'rahul@gmail.com', '9876543210'),
(2, 'Pavan', 'pavan@gmail.com', '9876543233'),
(3, 'Arun', 'arun@gmail.com', '9876543212'),
(4, 'Suresh', 'suresh@gmail.com', '9876543232');

-- INSERT BORROW RECORDS
INSERT INTO Borrow_Records
(Borrow_ID, Book_ID, Member_ID, Borrow_Date, Return_Date)
VALUES
(1, 1, 1, '2026-09-01', '2026-09-10'),
(2, 2, 2, '2026-09-03', '2026-09-12'),
(3, 1, 3, '2026-09-05', NULL),
(4, 3, 1, '2026-09-07', NULL),
(5, 4, 4, '2026-09-08', '2026-09-15');

--  CRUD OPERATIONS ON BOOKS
-- CREATE
INSERT INTO Books
(Book_ID, Book_Name, Author_Name, Category, Published_Year)
VALUES
(6, 'Java Programming', 'Tom Smith', 'Programming', 2023);

-- READ
SELECT * FROM Books;

-- READ - SEARCH BY BOOK ID
SELECT *FROM Books
WHERE Book_ID = 1;

-- UPDATE
UPDATE Books
SET Book_Name = 'Advanced Python Programming'
WHERE Book_ID = 1;

-- DELETE
DELETE FROM Books
WHERE Book_ID = 6;

-- JOIN QUERY
SELECT
    b.Book_Name,
    b.Author_Name,
    m.Member_Name,
    br.Borrow_Date,
    br.Return_Date
FROM Borrow_Records br
JOIN Books b
    ON br.Book_ID = b.Book_ID
JOIN Members m
    ON br.Member_ID = m.Member_ID;

--  GROUP BY QUERY
-- Number of books in each category
SELECT
    Category,
    COUNT(*) AS Total_Books
FROM Books
GROUP BY Category;

-- Number of books borrowed by each member
SELECT
    m.Member_Name,
    COUNT(br.Borrow_ID) AS Total_Borrowed
FROM Members m
JOIN Borrow_Records br
    ON m.Member_ID = br.Member_ID
GROUP BY m.Member_Name;

-- ORDER BY QUERY
-- Books by name
SELECT *FROM Books
ORDER BY Book_Name ASC;

-- Books by published year
SELECT *FROM Books
ORDER BY Published_Year DESC;

-- AGGREGATE FUNCTIONS

-- Total number of books
SELECT COUNT(*) AS Total_Books
FROM Books;

-- Latest published year
SELECT MAX(Published_Year) AS Latest_Year
FROM Books;

-- Oldest published year
SELECT MIN(Published_Year) AS Oldest_Year
FROM Books;

-- Average published year
SELECT AVG(Published_Year) AS Average_Year
FROM Books;

-- BORROWED BOOK REPORT
SELECT
    b.Book_Name,
    m.Member_Name,
    br.Borrow_Date,
    br.Return_Date
FROM Borrow_Records br
JOIN Books b
    ON br.Book_ID = b.Book_ID
JOIN Members m
    ON br.Member_ID = m.Member_ID;

-- CREATE SQL VIEW
CREATE VIEW Borrowed_Book_Report AS
SELECT
    b.Book_ID,
    b.Book_Name,
    b.Author_Name,
    m.Member_ID,
    m.Member_Name,
    br.Borrow_Date,
    br.Return_Date
FROM Borrow_Records br
JOIN Books b
    ON br.Book_ID = b.Book_ID
JOIN Members m
    ON br.Member_ID = m.Member_ID;

-- DISPLAY SQL VIEW
SELECT *FROM Borrowed_Book_Report;