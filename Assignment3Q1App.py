import psycopg
import datetime
from dotenv import dotenv_values
from os import path


__env_path = path.join(path.dirname(__file__), ".env")
config = dotenv_values(__env_path)


class DataBase():
    
    def __init__(self, db_name: str, user_name: str, password: str, port: str) -> None:
        try:
            self.connection = psycopg.connect(
                f"dbname={db_name} user={user_name} password={password} port={port}"
            )

        except psycopg.OperationalError as e:
            print(e)
            exit(1)
    

    def getAllStudents(self) -> list:
        """Gets all students in the students table

        Returns:
            list: list of tuples containing all the students' information
        """
        with self.connection.cursor() as cursor:
            cursor = cursor.execute("SELECT * FROM STUDENTS")
            self.connection.commit()
            return cursor.fetchall()

    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str) -> bool:
        """Adds a student to the students table

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            email (str): The student's email
            enrollment_date (str): The student's date of enrollment ('year-month-day' -> '2023-12-31')

        Returns:
            bool: True if the process completed without an error
        """
        with self.connection.cursor() as cursor:
            cursor = cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES( %(fn)s , %(ln)s , %(email)s , %(date)s )", 
                                    {'date': enrollment_date, 'fn': first_name, 'ln': last_name, 'email': email})
            self.connection.commit()
        return True

    def updateStudentEmail(self, student_id: str, new_email: str) -> bool:
        """Changes a student's email

        Args:
            student_id (str): The student id of the student who will have their email changed.
            new_email (str): The new email to replace the old email.

        Returns:
            bool: True if the process completed without an error
        """
        with self.connection.cursor() as cursor:
            cursor = cursor.execute("UPDATE students SET email = %(new_email)s WHERE student_id = %(student_id)s", {'new_email': new_email, 'student_id': student_id})
            self.connection.commit()
        return True

    def deleteStudent(self, student_id: str) -> bool:
        """Removes a student

        Args:
            student_id (str): The student_id of the student to be removed.

        Returns:
            bool: True if the process completed without an error
        """
        with self.connection.cursor() as cursor:
            cursor = cursor.execute("DELETE FROM students WHERE student_id = %(sid)s", {'sid': student_id})
            self.connection.commit()
        return True


if __name__ == "__main__":
    try:
        db = DataBase(
            db_name=config["DB_NAME"],
            user_name=config["UNAME"],
            password=config["PASSWORD"],
            port=config["PORT"]
        )
    
    except KeyError:
        print(".env file not configured properly, ensure DB_NAME, UNAME, PASSWORD, PORT are all set.")
        exit(1)
    
    print(db.getAllStudents())
    print(db.addStudent("name1", "name2", "email@mail.com", datetime.date(2023, 10, 1)))
    print(db.updateStudentEmail("1", "new@email.com"))
    print(db.deleteStudent("1"))
    