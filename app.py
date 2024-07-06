import sys
from dbhelper import DBHelper

class MY_SYSTEM:

    def __init__(self):
        self.db = DBHelper()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
1. Enter 1 to Register.
2. Enter 2 to Login.
3. Enter 3 to exit.
""")
            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            elif user_input == "3":
                self.db.close_connection()
                sys.exit(0)
            else:
                print("Invalid input, please try again.")

    def login_menu(self):
        input("""
1. Enter 1 to see profile.
2. Enter 2 to edit profile.
3. Enter 3 to delete profile.
4. Enter 4 to go back to main menu.
""")

    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        response = self.db.register(name, email, password)

        if response == 1:
            print("Registration successful")
        else:
            print("Registration failed")
    
    def login(self):
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        data = self.db.search(email, password)
        if len(data) == 0:
            print("Login failed, incorrect details")
        else:
            print("Login successful", data[0][1])
            self.login_menu()

if __name__ == "__main__":
    app = MY_SYSTEM()
