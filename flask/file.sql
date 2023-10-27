-- -- Create the students table
-- CREATE TABLE students_data_two (
--     id serial PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     age INT,
--     grade CHAR(1)
-- );

-- Insert student data
INSERT INTO students_data_two (first_name, last_name, age, grade) VALUES
    ('Samantha', 'Davis', 22, 'A'),
    ('Oliver', 'Jones', 20, 'B'),
    ('Sophia', 'Miller', 21, 'A'),
    ('Ethan', 'Wilson', 19, 'C'),
    ('Isabella', 'Moore', 22, 'B');

-- Retrieve student information
SELECT * FROM students_data_two;