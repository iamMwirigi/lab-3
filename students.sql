-- Create a database
CREATE DATABASE IF NOT EXISTS school;

-- Use the database
USE school;

-- Create the student table
CREATE TABLE IF NOT EXISTS student (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

-- Insert sample data
INSERT INTO student (name, age, gender) VALUES 
('Alice Johnson', 22, 'Female'),
('Bob Smith', 25, 'Male'),
('Charlie Brown', 20, 'Non-binary');

-- Verify data
SELECT * FROM student;
