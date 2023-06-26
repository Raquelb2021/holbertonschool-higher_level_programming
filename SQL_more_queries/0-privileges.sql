-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root', password='password', host='localhost')
cursor = cnx.cursor()

# Define the users to check
users = ['user_0d_1', 'user_0d_2']

# Loop through the users and show their privileges
for user in users:
    print(f"Privileges for user {user}:")
    cursor.execute(f"SHOW GRANTS FOR '{user}'@'localhost'")
    for row in cursor:
        print(row[0])
    print()

# Close the cursor and connection
cursor.close()
cnx.close()

