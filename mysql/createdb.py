import pymysql

db = pymysql.connect("localhost","root","1234","TESTDB")

cursor = db.cursor()

cursor.execute("drop table if exists EMPLOYEE")

sql = '''
CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)
'''

cursor.execute(sql)

db.close()
