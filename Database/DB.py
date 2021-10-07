import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath("assignment"))
db_path = os.path.join(BASE_DIR, "assignment.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

def fetchInitData(type, increment=1):
    return cur.execute(
        "select * from assignment order by {} asc limit ({}-1)*50, 50".format(type, increment)).fetchall()


def hourlyAverageAccident(startDate, endDate):
    startDate = startDate.replace("/", "")
    endDate = endDate.replace("/", "")
    return cur.execute("select count(ACCIDENT_TIME), ACCIDENT_TIME from assignment group by ACCIDENT_TIME having ACCIDENT_DATE between '{}' and '{}'".format(startDate, endDate)).fetchall()


def getDataByDate(startDate, endDate):
    startDate = startDate.replace("/", "")
    endDate = endDate.replace("/", "")
    return cur.execute(
        "select * from assignment where ACCIDENT_DATE between '{}' and '{}' order by ACCIDENT_DATE asc".format(
            startDate, endDate)).fetchall()


def getDataByType(startDate, endDate, type="Collision"):
    startDate = startDate.replace("/", "")
    endDate = endDate.replace("/", "")
    return cur.execute(
        "select ACCIDENT_TYPE from assignment where ACCIDENT_DATE between '{}' and '{}' and ACCIDENT_TYPE like '%{}%' order by ACCIDENT_DATE asc".format(
            startDate, endDate, type)).fetchall()


def alcoholImpact():
    totalAccident = cur.execute("SELECT COUNT(*) FROM assignment").fetchall()
    alcoholAccident = cur.execute("select COUNT(*) from assignment where ALCOHOL_RELATED = 'Yes'").fetchall()
    return alcoholAccident[0][0] / totalAccident[0][0]


def LGARate():
    return cur.execute("select count(LGA_NAME_ALL), LGA_NAME_ALL from assignment group by LGA_NAME_ALL").fetchall()

def getAccidentType():
    return cur.execute("select distinct ACCIDENT_TYPE from assignment").fetchall()
