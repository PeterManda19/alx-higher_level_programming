#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database using a 'with' statement
    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as conn:
        # Create a cursor object to execute SQL statements
        with conn.cursor() as cursor:
            # Execute the SQL query to select all rows from the 'states' table and order them by id
            cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")

            # Fetch rows from the cursor in batches of 100 and print them
            while True:
                rows = cursor.fetchmany(100)
                if not rows:
                    break
                for row in rows:
                    print(row)
