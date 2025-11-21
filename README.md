# Python_MySQL_App
This is a student management system, having authentications, using Python Programming Language with Flask Web Backend Framwork . The data will be stored in MySQL database

### Configuration of MySQL DataBase##
MySQL is a Relational Database Management System (RDBMS) whereas the structured Query Language (SQL) is the language used for handling the RDBMS using commands i.e Creating, Inserting, Updating and Deleting (CRUD) the data from the databases. SQL commands are case insensitive i.e "CREATE" and "create" signify the same command.

In this article, we will discuss how to create a table in MySQL using Python.

Installation
To get started, you'll need to install the MySQL Connector for Python. This allows Python to interact with a MySQL database.

Open the command prompt or terminal.
Navigate to your Python script directory.
Run the following command to install the MySQL connector:
pip install mysql-connector

Python Mysql Connector Module Methods
1. connect()
This method is used to establish a connection with the MySQL server. It takes the following arguments:

user: Username associated with the MySQL server.
password: Password for authentication.
database: The database to connect to.
2. cursor()
This method creates a cursor in the system memory. The cursor is the workspace for executing SQL commands. It remains open for the entire session.

3. execute()
The execute() method takes an SQL query as an argument and executes it. You can use this method to perform operations like creating, inserting, updating, or deleting data.

Creating Database
A database is an organized collection of data stored in tables. These tables are designed to make data manipulation (like creation, insertion, updates, and deletions) easy and efficient.

SQL command for Creating Database:
CREATE DATABASE database_name;

## Example of creation of database##

import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="your_password"
)

# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
# Incase you get this error import mysql.connector 
pip install mysql-connector-python


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

What is a Table
The table is a collection of data organized in the form of rows and columns. Table is present within a database as you can see from the above image.

Rows are also called tuples
Columns are called the attributes of the table
SQL command for Creating a Table: 
As we have discussed that tables are created inside a database so we need to first make sure to select or move into to the database before creating a table. To select the "College" database use this command:

USE college;

This will select the "College" database, now we can proceed to create tables inside it. Here's how to create a table:

CREATE TABLE table_name
(
     column_name_1 column_Data_type, 
     column_name_2 column_Data_type, 
     :
     :
     column_name_n column_Data_type
);

SQL Data Types:

Numeric: INT, FLOAT, DOUBLE
Character/String: VARCHAR, CHAR, TEXT
Date/Time: DATE, TIME, DATETIME
Unicode: NCHAR, NVARCHAR
Binary: BLOB
For instance, let's suppose we have to create a table named "STUDENT" having two columns, here's how we can do it:

CREATE TABLE Student (
    Name VARCHAR(255),
    Roll_no INT
);

Creating a Table in MySQL Using Python
Let’s consider an example where we create a table named Student inside the "College" database. The Student table will have two columns: Name (for the student's name) and Roll_no (for the student's roll number).

Python Code to Create a Table:


import mysql.connector as SQLC

def CreateTable():
    # Connect to the College database
    DataBase = SQLC.connect(
        host="localhost",  # Server name
        user="root",       # MySQL username
        password="your_password",  # MySQL password
        database="College"  # Database name
    )

    # Create a cursor object
    Cursor = DataBase.cursor()

    # SQL query to create the table
    TableName = """CREATE TABLE Student (
                    Name VARCHAR(255),
                    Roll_no INT
                  );"""

    # Execute the query to create the table
    Cursor.execute(TableName)
    print("Student Table is Created in the Database")

# Calling the CreateTable function
CreateTable() 

