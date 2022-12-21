import sqlite3
from sqlite3 import Error
from flask import request

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
    req= "CREATE TABLE IF NOT EXISTS pcinfo(id integer PRIMARY KEY);"
    connect.execute(req)

def prepareDb(dbname):
    connect = initConnect(dbname)
    createDbTable(connect)
    connect.close()
    
def addOptColumToDb(dbname):
    db=dbname.split(".")[0]
    connect = initConnect(dbname)
    req= "DROP TABLE "+db
    connect.execute(req)
    req= "CREATE TABLE IF NOT EXISTS pcinfo(id integer PRIMARY KEY);"
    connect.execute(req)
    print("TABLE DROPED")
    for element in request.args: 
        requestdb = "ALTER TABLE "+str(db)+" ADD COLUMN "+str(element)+" text NULL"
        connect.execute(requestdb)
        connect.commit()
        print(element + " colum was created")

def getMassage(dbname):
    connect = initConnect(dbname)
    req = "SELECT * FROM pcinfo WHERE id=1 ;"
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

def addOneOptinToDb(dbname, option, text):
    connect = initConnect(dbname)
    cursor = connect.cursor()
    req="INSERT INTO pcinfo(`"+option+"`) VALUES('{}')".format(str(text))
    cursor.execute(req)
    req= "UPDATE pcinfo SET "+option+"='"+str(text)+"' WHERE id=1"
    cursor.execute(req)
    req= "DELETE FROM pcinfo WHERE id>1"
    cursor.execute(req)
    connect.commit()
    connect.close()

