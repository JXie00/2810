import sqlite3
import pandas


def dbInitliase():
    con = sqlite3.connect("../assignment.db")
    df = pandas.read_csv("../Crash Statistics Victoria.csv")
    df.to_sql("assignment", con, if_exists='fail', index=False)