import pyodbc
import re

CONNECTION_STRING = "{{cookiecutter.connection_string}}"

connection = pyodbc.connect(re.sub('Driver=\{.+?\};', 'Driver={SQL Server};', CONNECTION_STRING))
cursor = connection.cursor()
cursor.execute("select distinct FirstName, LastName from {{cookiecutter.namespace}}.{{cookiecutter.table}} order by LastName, FirstName")

row = cursor.fetchall()
print('\n'.join('{0[0]} {0[1]}'.format(r) for r in row))
