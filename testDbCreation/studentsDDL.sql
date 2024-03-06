-- Create a DataBase or use this one.

-- CREATE DATABASE "A3Q1_3005"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Canada.1252'
--     LC_CTYPE = 'English_Canada.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

CREATE TABLE STUDENTS(
    student_id          SERIAL PRIMARY KEY,
    first_name          TEXT NOT NULL,
    last_name           TEXT NOT NULL,
    email               TEXT UNIQUE NOT NULL,
    enrollment_date     DATE DEFAULT(CURRENT_DATE)
);