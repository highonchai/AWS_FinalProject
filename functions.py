import os
from os import system
import mysql.connector
from mysql.connector import connect
import connection
from connection import conn
import colorama
from colorama import Fore, Style
from datetime import date

# THE FUNCTIONS FOR THE PROJECT


def displayAllEnrollmentsTable():
    system('clear')
    tableName1 = 'enrollments'
    tableName2 = 'users'
    tableName3 = 'courses'
    try:
        cursor = conn.cursor()
        cursor.execute(
            f'''
            SELECT e.enrollment_id as 'Enrollment ID', 
            CONCAT(u.user_firstname, ' ', u.user_lastname) as 'Student Name', 
            e.user_id as 'Student ID', 
            c.course_name as 'Course Name', 
            c.course_id as 'Course ID',
            e.enrollment_grade as 'Student Grade' 
            FROM {tableName1} e
            LEFT JOIN {tableName2} u on u.user_id = e.user_id
            LEFT JOIN {tableName3} c on c.course_id = e.course_id
            ORDER BY u.user_lastname, u.user_firstname
            ''')
        print(Style.RESET_ALL)
        print(Fore.GREEN, 'ENROLLMENT INFO: ')
        print(Style.RESET_ALL)
        for row in cursor:
            print(f'''{Fore.YELLOW}
            Student ID: ........................{Style.RESET_ALL}{Fore.CYAN}{row[2]}{Fore.YELLOW}
            Student Name: ......................{Style.RESET_ALL}{Fore.CYAN}{row[1]}{Fore.YELLOW}
            Enrollment ID: .....................{Style.RESET_ALL}{Fore.CYAN}{row[0]}{Fore.YELLOW}
            Course Name: .......................{Style.RESET_ALL}{Fore.CYAN}{row[3]}{Fore.YELLOW}
            Course ID: .........................{Style.RESET_ALL}{Fore.CYAN}{row[4]}{Fore.YELLOW}
            Student Grade: .....................{Style.RESET_ALL}{Fore.CYAN}{row[5]}{Fore.YELLOW}
            ''')
        cursor.close()
        conn.close()

    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from database', error)


displayAllEnrollmentsTable()
