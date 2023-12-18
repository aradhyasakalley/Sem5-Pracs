CREATE DATABASE temporal;
USE temporal;

CREATE TABLE time_records (
    date DATE,
    present_time TIME,
    Last_Name VARCHAR(25),
    First_Name VARCHAR(25),
    Location VARCHAR(25)
);

INSERT INTO time_records
VALUES 
    ("2022-12-01", "09:20:30", "Smith", "John", "New York"),
    ("2022-12-01", "09:30:30", "Johnson", "Emma", "Los Angeles"),
    ("2022-12-01", "09:45:30", "Williams", "Michael", "Chicago"),
    ("2022-12-02", "09:00:30", "Brown", "Sophia", "Houston"),
    ("2022-12-02", "10:00:30", "Jones", "Oliver", "Miami"),
    ("2022-12-02", "10:40:30", "Davis", "Ava", "San Francisco");

SELECT * FROM time_records;
