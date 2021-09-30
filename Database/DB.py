import sqlite3
con = sqlite3.connect("../assignment.db")


def FetchInitData(type) :
    cur = con.cursor()
    cur.execute("select * from assignment order by {} asc limit 50".format(type))
    res = cur.fetchall()
    return res

