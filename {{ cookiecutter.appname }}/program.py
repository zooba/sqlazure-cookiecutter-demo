import pyodbc

CONNECTION_STRING = "{{cookiecutter.connection_string}}"

connection = pyodbc.connect(CONNECTION_STRING)

# Read all 
cursor = connection.cursor()
cursor.execute(
    "select LastName, Count(*) as 'Members' "
    "from {{cookiecutter.namespace}}.{{cookiecutter.table}} "
    "group by LastName "
    "having Count(*) > 3 "
    "order by 'Members' DESC")

row = cursor.fetchall()
print('Family Name        | Members')
print('-------------------+--------')
print('\n'.join('{0[0]:<19}|{0[1]:>8}'.format(r) for r in row))
