import os
from os import system
import connection
from connection import conn
import colorama
from colorama import Fore, Style
from datetime import date

# THE FUNCTIONS FOR THE PROJECT

# DISPLAY PRODUCTS AVAILABLE FOR PURCHASE TEMPLATE


def displayProductTable():
    system('clear')
    tableName1 = "product_records"
    try:
        cursor = conn2.cursor()
        cursor.execute(
            f"SELECT * FROM {tableName1} ORDER BY product_id"
        )
        rows = cursor.fetchall()
        print(Style.RESET_ALL)
        if(rows):
            print(Fore.GREEN, 'PRODUCT INFO: ')
            print(Style.RESET_ALL)
            for row in rows:
                print(f'''{Fore.YELLOW}
                Product ID: .....................{Style.RESET_ALL}{Fore.CYAN}{row[0]}{Fore.YELLOW}
                Product Name: ...................{Style.RESET_ALL}{Fore.CYAN}{row[1]}{Fore.YELLOW}
                Product Cost: ...................{Style.RESET_ALL}{Fore.CYAN}{row[2]}{Fore.YELLOW}
                Product Description: ............{Style.RESET_ALL}{Fore.CYAN}{row[3]}{Fore.YELLOW}
                ''')
            cursor.close()
        else:
            print('Sorry! Your database is empty')

    except(Exception, psycopg2.Error) as error:
        print('Error while fetching data from database', error)


customerIDs = []

# DISPLAY TEMPLATE


def displayCustomerTable():
    system('clear')
    tableName1 = "customer_records"
    try:
        cursor = conn2.cursor()
        cursor.execute(
            f"SELECT * FROM {tableName1} ORDER BY customer_id"
        )
        rows = cursor.fetchall()
        print(Style.RESET_ALL)
        if(rows):
            print(Fore.GREEN, 'Customer INFO: ')
            print(Style.RESET_ALL)
            for row in rows:
                print(f'''{Fore.YELLOW}
                Customer ID: ........................{Style.RESET_ALL}{Fore.CYAN}{row[0]}{Fore.YELLOW}
                Customer First Name: ................{Style.RESET_ALL}{Fore.CYAN}{row[1]}{Fore.YELLOW}
                Customer Last Name: .................{Style.RESET_ALL}{Fore.CYAN}{row[2]}{Fore.YELLOW}
                Customer Phone: .....................{Style.RESET_ALL}{Fore.CYAN}{row[3]}{Fore.YELLOW}
                Customer Address: ...................{Style.RESET_ALL}{Fore.CYAN}{row[4]}{Fore.YELLOW}
                ''')
                customerIDs.append(row[0])
            cursor.close()
        else:
            print('Sorry! Your database is empty')

    except(Exception, psycopg2.Error) as error:
        print('Error while fetching data from database', error)
    return customerIDs[-1]


# Displays the Customer Table TEMPLATE

def displayCustomerPurchaseTable():
    system('clear')
    # tableName1 = "customer_records"
    # tableName2 = "purchase_records"
    # tableName3 = "product_records"
    try:
        cursor = conn2.cursor()
        cursor.execute(
            f'''
            SELECT o.purchase_date as "Date Purchased", 
            purchase_id as "Purchase ID", 
            o.product_id as "Product ID", 
            product_name as "Product Name", 
            product_cost as "Product Cost", 
            purchase_quantity as "Quantity Purchased", 
            purchase_total as "Order Total", 
            CONCAT(customer_firstname, ' ', customer_lastname) as "Customer Name", 
            customer_phone as "Customer Contact",
            c.customer_id as "Customer ID"
            FROM purchase_records o 
            INNER JOIN product_records p ON o.product_id = p.product_id 
            INNER JOIN customer_records c ON o.customer_id = c.customer_id 
            ORDER BY o.purchase_date
                    ''')
        rows = cursor.fetchall()
        print(Style.RESET_ALL)
        if(rows):
            print(Fore.GREEN, 'PURCHASE INFO: ')
            print(Style.RESET_ALL)
            for row in rows:
                print(f'''{Fore.YELLOW}
                Date Purchased: .....................{Style.RESET_ALL}{Fore.CYAN}{row[0]}{Fore.YELLOW}
                Purchase ID: ........................{Style.RESET_ALL}{Fore.CYAN}{row[1]}{Fore.YELLOW}
                Product ID: .........................{Style.RESET_ALL}{Fore.CYAN}{row[2]}{Fore.YELLOW}
                Product Name: .......................{Style.RESET_ALL}{Fore.CYAN}{row[3]}{Fore.YELLOW}
                Product Cost: .......................{Style.RESET_ALL}{Fore.CYAN}{row[4]}{Fore.YELLOW}
                Quantity Purchased: .................{Style.RESET_ALL}{Fore.CYAN}{row[5]}{Fore.YELLOW}
                Order Total: ........................{Style.RESET_ALL}{Fore.CYAN}{row[6]}{Fore.YELLOW}
                Customer Name: ......................{Style.RESET_ALL}{Fore.CYAN}{row[7]}{Fore.YELLOW}
                Customer Contact: ...................{Style.RESET_ALL}{Fore.CYAN}{row[8]}{Fore.YELLOW}
                Customer ID: ........................{Style.RESET_ALL}{Fore.CYAN}{row[9]}{Fore.YELLOW}
                ''')
            cursor.close()
        else:
            print('Sorry! Your database is empty')

    except(Exception, psycopg2.Error) as error:
        print('Error while fetching data from database', error)


# Inserts values into the Customer Table TEMPLATE

def insertCustomerTable(firstName, lastName, customerAge, customerPhone, customerAddress):
    tableName = "customer_records"
    print('I see you want to be a customer!')
    cursor = conn2.cursor()
    cursor.execute(
        f"INSERT INTO {tableName}(customer_firstname, customer_lastname, customer_age, customer_phone, customer_address) values ('{firstName}', '{lastName}', '{customerAge}', '{customerPhone}', '{customerAddress}')"
    )
    conn2.commit()
    print(
        f'Congrats, {firstName}, your account has been added to the database.')
    cursor = conn2.cursor()
    print('All done!')
    lastElement = displayCustomerTable()
    return lastElement

# CREASTE A NEW PURCHASE TEMPLATE


def insertPurchaseTable(count, customerID):
    tableName = "purchase_records"
    dateToday = date.today()
    displayProductTable()
    #counter = 1
    cursor = conn2.cursor()
    for i in range(count):
        print(
            f'Please answer the following questions for Purchase # {i + 1}:')
        productID = int(
            input('What is the product ID of the product you would like to purchase? >> '))
        if (productID == 1):
            price = 2999.99
        elif (productID == 2):
            price = 1500.95
        elif (productID == 3):
            price = 965.75
        elif (productID == 4):
            price = 1200.88
        elif(productID == 5):
            price = 250.99

        qty = int(
            input("What is quantity that you would like to purchase? >> "))
        total = qty * price
        cursor.execute(
            f"INSERT INTO {tableName}(customer_ID, product_ID, purchase_quantity, purchase_date, purchase_total) values ('{customerID}', '{productID}', '{qty}', '{dateToday}', '{total}')"
        )
        conn2.commit()
        print(f'The order has been added to the database')
    cursor = conn2.cursor()
    print('All done!')
    # displayCustomerPurchaseTable()

# UPDATE PURCHASE TEMPLATE


def updatePurchaseTable(count):
    tableName = "purchase_records"
    #counter = 1
    cursor = conn2.cursor()
    for i in range(count):
        print(f'For purchase # {i + 1} >> ')
        displayCustomerPurchaseTable()
        print('The most recent purchases are above')
        purchase = str(input(
            'For what purchase would you like to update the quantity? (purchase ID) >> '))
        fieldValue = str(
            input('What would you like the new quantity to be? >> '))
        cursor.execute(
            f"UPDATE {tableName} SET purchase_quantity={fieldValue} WHERE purchase_ID={purchase}"
        )
        conn2.commit()
        print(f'The quantity has been updated')
    cursor = conn2.cursor()
    print('All done!')
    displayCustomerPurchaseTable()
