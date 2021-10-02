import sqlite3

con = sqlite3.connect("../assignment.db")
cur = con.cursor()

cur.execute("update assignment set ACCIDENT_DATE = REPLACE(ACCIDENT_DATE,'/','')")
cur.execute(
    "update assignment set ACCIDENT_DATE = substr(ACCIDENT_DATE, 4, 4) || '' || substr(ACCIDENT_DATE, 3, 1) || '' || substr(ACCIDENT_DATE, 1, 2) where length(ACCIDENT_DATE) = 7")
cur.execute(
    "update assignment set ACCIDENT_DATE = substr(ACCIDENT_DATE, 3, 4) || '' || substr(ACCIDENT_DATE, 2, 1) || '' || substr(ACCIDENT_DATE, 1, 2) where length(ACCIDENT_DATE) = 6")
cur.execute(
    "update assignment set ACCIDENT_DATE = substr(ACCIDENT_DATE, 5, 4) || '' || substr(ACCIDENT_DATE, 3, 2) || '' || substr(ACCIDENT_DATE, 1, 2) where length(ACCIDENT_DATE) = 8")
cur.execute("update assignment set ACCIDENT_TIME = substr(ACCIDENT_TIME,1,2)")
con.commit()