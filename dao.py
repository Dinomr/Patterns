import mysql.connector
class logicDatabase ():
    cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
    cnx.close()