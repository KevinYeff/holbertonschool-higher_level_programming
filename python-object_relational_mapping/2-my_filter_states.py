#!/usr/bin/python3
"""
takes an argument as a value and displays the value that matchesargument
in the table from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], database=argv[3])
    # Creating a cursor to execute queries
    cursor = database.cursor()
    # value that matches the argument
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '{}'".format(argv[4]))
    # Retrieving the results of the consult
    for row in cursor.fetchall():
        print(row)
    # Closing
    cursor.close()
    database.close()
