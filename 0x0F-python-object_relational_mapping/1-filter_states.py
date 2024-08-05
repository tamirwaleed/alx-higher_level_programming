#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa (filtered)'''

import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * \
                FROM states \
                WHERE name like 'N%' \
                ORDER BY id")
    results = cur.fetchall()
    for i in results:
        print(i)
    cur.close()
    con.close()
