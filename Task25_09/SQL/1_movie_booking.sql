-- CREATE DATABASE
CREATE DATABASE movie_booking_db;

USE movie_booking_db;

-- CREATE TABLES
-- Departments Table
CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY AUTO_INCREMENT,
    Department_Name VARCHAR(100) NOT NULL UNIQUE
);

-- Employees Table
CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_Name VARCHAR(100) NOT NULL,
    Department_ID INT NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (Department_ID)
        REFERENCES Departments(Department_ID)
);

-- Movies Table
CREATE TABLE Movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    language VARCHAR(50),
    duration_minutes INT CHECK (duration_minutes > 0),
    release_date DATE,
    rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10)
);

-- Customers Table
CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

-- Theaters Table
CREATE TABLE Theaters (
    Theater_ID INT PRIMARY KEY AUTO_INCREMENT,
    Theater_Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- Shows Table
CREATE TABLE Shows (
    show_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT NOT NULL,
    screen_id INT NOT NULL,
    show_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    ticket_price DECIMAL(10,2) NOT NULL CHECK (ticket_price > 0),

    FOREIGN KEY (movie_id)
        REFERENCES Movies(movie_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (screen_id)
        REFERENCES Screens(screen_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
-- Bookings Table
CREATE TABLE Bookings (
    Booking_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_ID INT NOT NULL,
    Show_ID INT NOT NULL,
    Booking_Date DATE NOT NULL,
    Tickets INT NOT NULL,

    FOREIGN KEY (Customer_ID)
        REFERENCES Customers(Customer_ID),

    FOREIGN KEY (Show_ID)
        REFERENCES Shows(Show_ID)
);


-- Employee Delete Log Table
CREATE TABLE Employee_Delete_Log (
    Log_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_ID INT,
    Employee_Name VARCHAR(100),
    Department_ID INT,
    Salary DECIMAL(10,2),
    Deleted_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT SAMPLE DATA
-- Departments
INSERT INTO Departments
(Department_Name)
VALUES
('Technical'),
('HR'),
('Accounts'),
('Sales');

-- Employees
INSERT INTO Employees
(Employee_Name, Department_ID, Salary)
VALUES
('Pavan', 2, 85000),
('Priya', 4, 65000),
('Arun', 1, 75000),
('Lakshmi', 3, 90000),
('Rahul', 4, 60000),
('Ravi', 1, 85000);

-- Movies
INSERT INTO Movies
(title, genre, language, duration_minutes, release_date, rating)
VALUES
('Inception', 'Sci-Fi', 'English', 148, '2010-07-16', 8.8),
('Interstellar', 'Sci-Fi', 'English', 169, '2014-11-07', 8.7),
('Baahubali', 'Action', 'Telugu', 159, '2015-07-10', 8.0);

-- Customers
INSERT INTO Customers
(Customer_Name, Email)
VALUES
('Pavan', 'pavan@gmail.com'),
('Rahul', 'rahul@gmail.com'),
('Priya', 'priya@gmail.com'),
('Arun', 'arun@gmail.com');

-- Theaters
INSERT INTO Theaters
(Theater_Name, Location)
VALUES
('PVR Cinemas', 'Hyderabad'),
('INOX', 'Kukatpally'),
('Asian Cinemas', 'Miyapur');

-- Shows
INSERT INTO Shows
(movie_id, screen_id, show_date, start_time, end_time, ticket_price)
VALUES
(1, 1, '2026-09-25', '10:00:00', '12:28:00', 200.00),
(2, 1, '2026-09-25', '18:00:00', '20:49:00', 250.00),
(3, 2, '2026-09-25', '19:00:00', '21:39:00', 180.00);

-- Bookings
INSERT INTO Bookings
(Customer_ID, Show_ID, Booking_Date, Tickets)
VALUES
(1, 1, '2026-09-25', 4),
(2, 2, '2026-09-25', 2),
(3, 3, '2026-09-26', 3),
(4, 4, '2026-09-26', 5),
(1, 5, '2026-09-27', 8);

-- DISPLAY TABLE DATA
SELECT * FROM Departments;

SELECT * FROM Employees;

SELECT * FROM Movies;

SELECT * FROM Customers;

SELECT * FROM Theaters;

SELECT * FROM Shows;

SELECT * FROM Bookings;

SELECT * FROM Products;

SELECT * FROM Sales;
