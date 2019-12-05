import pymysql

db = pymysql.connect("localhost","root","1234","TESTDB")

cursor =db.cursor()

sql = """
INSERT INTO EMPLOYEE(FIRST_NAME) 
        VALUES ('GOOD')
        """

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
