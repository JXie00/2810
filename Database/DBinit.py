import sqlite3
import pandas

con = sqlite3.connect("../assignment.db")
df = pandas.read_csv("Crash Statistics Victoria.csv")
df.to_sql("assignment", con, if_exists='append', index=False)

cur = con.cursor()
cur.execute("select OBJECTID from assignment")

res = cur.fetchall()
