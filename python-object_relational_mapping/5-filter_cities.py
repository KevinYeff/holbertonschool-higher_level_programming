#!/usr/bin/python3
"""
Lists all cities by state from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to database
    database = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], database=argv[3])
    # Creating a cursor to execute queries
    cursor = database.cursor()
    # query that takes in the name of a state as argument
    cursor.execute(
        "SELECT cities.name \
        FROM cities INNER JOIN states ON cities.state_id = states.id \
        WHERE BINARY states.name = BINARY %s \
        ORDER BY cities.id ASC", (argv[4],))
    lists = []
    # Retrieving the results of the consult
    for row in cursor.fetchall():
        lists.append(row[0])
    print(", ".join(lists))
    # Closing
    cursor.close()
    database.close()
