#!/usr/bin/python3
""" Module that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import sys
    import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

db_connection = MySQLdb.connect(
    user=username,
    passwd=password,
    host='localhost',
    database=database_name,
    port=3306
)

db_cursor = db_connection.cursor()
db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = db_cursor.fetchall()
for row in rows:
    print(row)

db_connection.close()
