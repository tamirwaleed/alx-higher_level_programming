#!/usr/bin/python3
''' lists all cities from the database hbtn_0e_0_usa (filtered)'''

import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities c\
                LEFT JOIN states s \
                ON c.state_id = s.id \
                ORDER BY id")
    results = cur.fetchall()
    answ = ""
    for i in results:
        if i[2] == sys.argv[4]:
            answ += i[1] + ", "
    print(answ[:-2])
    cur.close()
    con.close()
