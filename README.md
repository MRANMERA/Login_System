# Login System

The MY_SYSTEM class integrates user registration and login via a CLI, using DBHelper for MySQL interactions. It connects to the database, allowing registration with name, email, and password stored via DBHelper's register. Login credentials are validated with DBHelper's search. After login, users manage profiles with view, edit, delete options. Exiting closes the DB connection via DBHelper's close_connection for proper resource handling.

- Features
User Registration: Allows new users to register with a name, email, and password.
User Login: Validates user credentials (email and password) against stored records in the database.
Profile Management: After login, users can view, edit, and delete their profiles.
Database Connection Management: Properly handles database connections using DBHelper.close_connection() for resource cleanup.

- Requirements
Python 3.x
mysql-connector-python library (pip install mysql-connector-python)
