#!/usr/bin/python3
import MySQLdb
import sys

"""To run the script,
from the command line with the required arguments:
python3 2-my_filter_states.py mysql_username mysql_password database_name state_name
"""

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # fetch all rows
    rows = cursor.fetchall()

    # print the rows
    for row in rows:
        print(row)

    # disconnect from server
    db.close()
