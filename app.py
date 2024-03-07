import pyodbc

# SQL Server connection settings
server = 'your_sql_server'
database = 'your_database'
trusted_connection = 'yes'
driver = 'ODBC Driver 17 for SQL Server'

# Connection string
conn_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

# Connect to SQL Server
try:
    connection = pyodbc.connect(conn_str)
    cursor = connection.cursor()
    print("Connected to SQL Server using Windows authentication")

    # Perform SQL operations here

    # Close the connection
    connection.close()
except Exception as e:
    print(f"Error: {e}")
