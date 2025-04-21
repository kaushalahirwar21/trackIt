CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    roll VARCHAR(50),
    course VARCHAR(50),
    mobile VARCHAR(15)
);

select * from students;

#drop database student_db;