#!/usr/bin/python3
import MySQLdb
import sys

"""To run the script,
from the command line with the required arguments:
python3 1-filter_states.py mysql_username mysql_password database_name state_name
"""

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch all rows
    rows = cursor.fetchall()

    # print the rows
    for row in rows:
        print(row)

    # disconnect from server
    db.close()
