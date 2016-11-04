import pyodbc
import re

CONNECTION_STRING = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:jsltdemo.database.windows.net,1433;Database=sqldemo;Uid=stevdo@jsltdemo;Pwd=au.rchA#P(8alh;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

connection = pyodbc.connect(re.sub('Driver=\{.+?\};', 'Driver={SQL Server};', CONNECTION_STRING))
cursor = connection.cursor()
cursor.execute("select distinct FirstName, LastName from SalesLT.Customer order by LastName, FirstName")

row = cursor.fetchall()
print('\n'.join('{0[0]} {0[1]}'.format(r) for r in row))
