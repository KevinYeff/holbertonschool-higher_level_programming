#!/usr/bin/python3
"""
Lists all values with a name  starting with N (upper N) from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], database=argv[3])
    # Creating a cursor to execute queries
    cursor = database.cursor()
    # Sorting in ascending order by id and list all the
    # values starting with an N
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%'  ORDER BY id ASC;")
    # Retrieving the results of the consult
    for row in cursor.fetchall():
        print(row)
    # Closing
    cursor.close()
    database.close()
