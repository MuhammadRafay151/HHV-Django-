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
    def read(self, querry):
        cursor = connection.cursor()
        cursor.execute(querry)
        row = cursor.fetchall()
        connection.close()
        return row
    def Insert(self,Querry):
        cursor = connection.cursor()
        cursor.execute(Querry)
        connection.close()


