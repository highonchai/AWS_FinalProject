import os
from os import system
import mysql.connector
from mysql.connector import connect
import connection
from connection import conn, connSQL
import colorama
from colorama import Fore, Style
from datetime import date

# THE FUNCTIONS FOR THE PROJECT


def displayAllEnrollmentsTable():
    system('clear')
    tableName1 = "enrollments"
    try:
        cursor = connSQL.cursor()
        cursor.execute(
            f"SELECT * FROM {tableName1} ORDER BY user_id"
        )
        print(Style.RESET_ALL)
         print(Fore.GREEN, 'ENROLLMENT INFO: ')
          print(Style.RESET_ALL)
           for row in cursor:
                print(f'''{Fore.YELLOW}
                Enrollment ID: .....................{Style.RESET_ALL}{Fore.CYAN}{row[0]}{Fore.YELLOW}
                Enrollment Name: ...................{Style.RESET_ALL}{Fore.CYAN}{row[1]}{Fore.YELLOW}
                Product Cost: ...................{Style.RESET_ALL}{Fore.CYAN}{row[2]}{Fore.YELLOW}
                Product Description: ............{Style.RESET_ALL}{Fore.CYAN}{row[3]}{Fore.YELLOW}
                ''')
            cursor.close()
            conn.close()
        else:
            print('Sorry! Your database is empty')

    except(Exception, mysql.connector..Error) as error:
        print('Error while fetching data from database', error)
