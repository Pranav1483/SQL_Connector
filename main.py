import mysql.connector
from mysql.connector import Error
import pandas as pd
import pwinput


def mysql_connection(host_name, user_name, password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=password)
        print("Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def mysql_database_connection(host_name, user_name, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=database)
        print("Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def create_database(mydb, query):
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        print("Database created Successfully")
    except Error as err:
        print(f"Error: '{err}'")


def write_query(mydb, query):
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        mydb.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(mydb, query):
    cursor = mydb.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


Host = input("Enter Name of Host : ")
Username = input("Enter Username : ")
Password = pwinput.pwinput(prompt="Enter Password : ")

conn = mysql_connection(Host, Username, Password)

n = int(input("\n1 - Create Database\n2 - Connect Database\n3 - Read Query\n4 - Write Query\n5 - Exit\n\nEnter Your "
              "Choice : "))

while (n == 1) or (n == 2) or (n == 3) or (n == 4):

    if n == 1:
        db_name = input("\nEnter Database Name : ")
        create_database(conn, "CREATE DATABASE "+db_name)
    elif n == 2:
        db_name = input("\nEnter Database Name : ")
        mydatabase = mysql_database_connection(Host, Username, Password, db_name)
    elif n == 3:
        q = input("\nEnter Query : ")
        text = read_query(mydatabase, q)
        for i in text:
            print(i)
    elif n == 4:
        q = input("\nEnter Query : ")
        write_query(mydatabase, q)

    n = int(input("\n1 - Create Database\n2 - Connect Database\n3 - Read Query\n4 - Write Query\n5 - Exit\n\nEnter "
                  "Your "
                  "Choice : "))
print("Thankyou")
