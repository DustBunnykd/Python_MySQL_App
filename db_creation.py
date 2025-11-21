import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="#W15w2020#"
)

# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
Cursor.execute("CREATE DATABASE College")

print("College database is created")