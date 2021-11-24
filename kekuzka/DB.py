import sqlite3


class DB():

    def __init__(self):
        self.sqlite_connection = sqlite3.connect('buffer.db')
        self.cursor = self.sqlite_connection.cursor()
    

    def read_data(self, delete_after_reading=False): 

        self.cursor.execute("SELECT * FROM main")
        data = self.cursor.fetchall()

        if len(data) > 0:
            print(data)

            if delete_after_reading:
                self.cursor.execute("DELETE FROM main")
                self.sqlite_connection.commit()

            return data

    
    def write_data(self, data):
       self.cursor.execute(f"INSERT INTO main (command) VALUES ('{data}')")
       self.sqlite_connection.commit() 

    
    