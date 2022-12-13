import sqlite3
from sqlite3 import Error

def initConnect(path):
    connect = None
    try:
        connect = sqlite3.connect(path)
        print("Connected!")
    except Error as e:
        print(e)
        print("Connection failed!")
    return connect

def createDbTable(connect):
    req= "CREATE TABLE IF NOT EXISTS chat( id integer PRIMARY KEY, user text NOT NULL, massage text NOT NULL);"
    connect.execute(req)

def prepareDb(dbname):
    connect = initConnect(dbname)
    createDbTable(connect)
    connect.close()

def addMassageToDb(dbname, user, massage):
    connect = initConnect(dbname)
    req = "INSERT INTO chat(`user`, `massage`) VALUES('{}', '{}')".format(user, massage)
    cursor = connect.cursor()
    cursor.execute(req)
    connect.commit()
    connect.close()
    
def getMassage(dbname):
    connect = initConnect(dbname)
    req = "SELECT `user` , `massage` FROM chat;"
    cursor = connect.cursor()
    cursor.execute(req)
    rows = cursor.fetchall()
    connect.close()
    return rows

def HtmlTableGenerator(rows):
    gentable = "<table>"
    for row in rows:
        tdClassCounter=0
        gentable += "<tr>"
        for cell in row:
            gentable += "<td class='tdclass"+str(tdClassCounter)+"'>" + str(cell) + "</td>"
            tdClassCounter+=1
        gentable += "</tr>"
    gentable += "</table>"
    return gentable


