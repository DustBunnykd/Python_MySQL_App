import mysql.connector as SQLC

def CreateTable():
    # Connect to the College database
    DataBase = SQLC.connect(
        host="localhost",  # Server name
        user="root",       # MySQL username
        password="#W15w2020#",  # MySQL password
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