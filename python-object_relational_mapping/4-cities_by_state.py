#!/usr/bin/python3
"""
Lists all cities by states from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], database=argv[3])
    # Creating a cursor to execute queries
    cursor = database.cursor()
    # value that matches the argument but safely
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    # Retrieving the results of the consult
    for row in cursor.fetchall():
        print(row)
    # Closing
    cursor.close()
    database.close()
