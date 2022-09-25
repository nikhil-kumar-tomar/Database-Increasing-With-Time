import csv
import mysql.connector
from mysql.connector import Error

table_name = str(input("Enter Name of table to be created:- "))
def create_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hello',
                                             user='root',
                                             password='1234')
        if connection.is_connected():
            mySql_Create_Table_Query = """CREATE TABLE {} ( 
                                keyword varchar(765) NULL,
                                Avg_monthly_searches int(100) NULL,
                                Competition varchar(250) NULL) """.format(table_name)

        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print(table_name, "Table created successfully ")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def display_table():

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hello',
                                             user='root',
                                             password='27682202')
        if connection.is_connected():
            life=open('out.csv','w')
            cont=[]
            while True:
                mySql_insert_Table_Query = """select * from {} where Competition='Low' and Avg_monthly_searches>=500;""".format(table_name)
                cursor = connection.cursor()
                result = cursor.execute(mySql_insert_Table_Query)
                display = cursor.fetchall()
                connection.commit()
                for l in display:
                    cont.append(l)
                writer=csv.writer(life,delimiter=',')
                writer.writerows(cont)
                life.close()
                print(cont)
                print("Data inserted in file successfully")
                break

    except Error as e:
        print("Error while connecting to MySQL", e)



def csvfill_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hello',
                                             user='root',
                                             password='27682202')
        if connection.is_connected():
            print("The file is not stalled here, This part might take a bit of time")
            f=open('in.csv','r')
            reader=csv.reader(f)
            for row in reader:
                Inp_Id=row[0]
                Inp_Name=row[1]
                Inp_Prize=row[2]
                mySql_insert_Table_Query = """insert IGNORE into {} values ('{}',{},'{}')""".format(table_name,Inp_Id,Inp_Name,Inp_Prize)
                cursor = connection.cursor()
                result = cursor.execute(mySql_insert_Table_Query)
                connection.commit()
            print("data inserted into Table successfully ")
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    except Error as e:
        print("Error while connecting to MySQL", e)


def del_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hello',
                                             user='root',
                                             password='27682202')
        if connection.is_connected():
            mySql_insert_Table_Query = """drop table {}""".format(
                table_name)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_Table_Query)
            print("data deleted from Table successfully ")
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    except Error as e:
        print("Error while connecting to MySQL", e)

create_table()
csvfill_table()
display_table()
del_table()