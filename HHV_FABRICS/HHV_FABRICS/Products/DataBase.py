# import pyodbc
# conn = pyodbc.connect(
#     "DRIVER={ODBC Driver 13 for SQL Server};"
#     "Server=DESKTOP-6996G2B;"
#     "Database=LMS;"
#     "Trusted_Connection=yes;"
# )
# print("Read")
# cursor = conn.cursor()
# cursor.execute("select * from employee")
# for row in cursor:
#     print(f'row = {row[0]}')
#     print()

from django.db import connection


class database:
    def read(self,querry):
        cursor = connection.cursor()
        cursor.execute(querry)
        row = cursor.fetchall()
        connection.close()
        return row
     
    def read_p(self,querry,data):
        cursor = connection.cursor()
        cursor.execute(querry,data)
        row = cursor.fetchall()
        connection.close()
        return row
    
    def Insert(self,Querry):
        cursor = connection.cursor()
        cursor.execute(Querry)
        connection.close()

    def Insert(self,Querry,Data):
        cursor = connection.cursor()
        cursor.execute(Querry,Data)
        connection.close()
    def Insert_ReadId(self,Querry,Data):
        cursor = connection.cursor()
        cursor.execute(Querry,Data)
        data=cursor.fetchone()[0]
        connection.close()
        return data
    def Delete(self,querry):
        cursor = connection.cursor()
        cursor.execute(querry)
        connection.close()
        return None
    def Update(self,querry,data):
        cursor = connection.cursor()
        cursor.execute(querry,data)
        connection.close()
        return None

