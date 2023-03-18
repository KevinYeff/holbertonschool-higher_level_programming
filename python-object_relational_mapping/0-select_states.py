#!/usr/bin/python3
"""
Lists all values in a table named states from the database hbtn_0e_0_usa.
We need to make sure that the script is not executed when imported.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], database=argv[3])

    # Creating a cursor to execute queries
    cursor = database.cursor()
    # Sorting in ascending order by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Retrieving the results of the consult
    for row in cursor.fetchall():
        print(row)
    # Closing
    cursor.close()
    database.close()
