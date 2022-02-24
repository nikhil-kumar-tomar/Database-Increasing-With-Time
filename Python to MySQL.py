import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='27682202', host='localhost', database='my'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
while True:
    FIRST_NAME=str(input("Enter your first name here:- "))
    LAST_NAME=str(input("Enter your last name here:- "))
    AGE=int(input("Enter your age here:- "))
    SEX=str(input("Enter your sex here:- "))
    INCOME=int(input("Enter your income here:- "))
    sql_enter='''INSERT INTO EMPLOYEE VALUES (%s, %s, %s, %s, %s )'''
    val=( FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    cursor.execute(sql_enter, val)
    conn.commit()
    x=str(input("Do you want to enter more data:- "))
    if x.upper()=='N' or x.upper()=='NO':
        break
#Closing the connection
conn.close()