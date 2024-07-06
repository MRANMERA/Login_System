import mysql.connector
import sys
from mysql.connector import Error

class DBHelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-db-demo"
            )
            self.mycursor = self.conn.cursor()
        except Error as e:
            print(f"Failed to connect to database: {e}")
            sys.exit(0)
        else:
            print("Connected to database")

    def register(self, name, email, password):
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            self.mycursor.execute(query, (name, email, password))
            self.conn.commit()
        except Error as e:
            print(f"Failed to insert data: {e}")
            return -1
        else:
            return 1

    def search(self, email, password):
        try:
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            self.mycursor.execute(query, (email, password))
            return self.mycursor.fetchall()
        except Error as e:
            print(f"Failed to search data: {e}")
            return []

    def close_connection(self):
        self.mycursor.close()
        self.conn.close()
