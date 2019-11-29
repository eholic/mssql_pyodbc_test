import pyodbc

if __name__ == '__main__':
    server = 'localhost'
    database = 'master'
    username = 'SA'
    password = '<YourStrong@Passw0rd>'

    cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={server}'
            f';DATABASE={database}'
            f';UID={username}'
            f';PWD={password}'
            )
    cursor = cnxn.cursor()

    query = cursor.execute('SELECT name, database_id, create_date '
                           'FROM sys.databases;')
    for r in query.fetchall():
        print(r)

    cursor.close()
    cnxn.close()
