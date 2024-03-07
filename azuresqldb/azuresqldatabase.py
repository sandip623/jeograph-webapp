import pyodbc

class AzureSqlDatabase:
    def __init__(self, server : str, database : str, username : str, password : str, driver : str):
        self.server = server
        self.database = database
        self.username = username 
        self.password = password
        self.driver = driver
        self.connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print(f"Connected to {self.server}...")
        except:
            print(f"Could not connect to the server...")

    def execute_query(self, query : str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()
        except pyodbc.Error as e:
            print(f"Error executing query", e)
    
    def disconnect(self):
        self.conn.close()
        print("Connection closed...")
