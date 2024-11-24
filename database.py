import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "admin1",
    "database": "korean" 
}

class Database: 
    def __init__(self):
        # try:
        #     self.connect = pymysql.connect(**DB_CONFIG)
        #     print("Успех")
        # except pymysql.MySQLError as e:
        #     print("Ошибка")
        #     self.connect = None
        self.connect = pymysql.connect(**DB_CONFIG)

    def create_tables(self): 
        queries = [
            """
                 CREATE TABLE IF NOT EXISTS user (
                 id INT AUTO_INCREMENT,
                 username VARCHAR(255) NOT NULL UNIQUE,
                 email VARCHAR(255) NOT NULL UNIQUE,
                 first_name VARCHAR(255) NOT NULL,
                 second_name VARCHAR(255) NOT NULL,
                 password VARCHAR(255) NOT NULL
                 )
            """
        ]
        with self.connect.cursor() as cursor:
            self.connect.ping(reconnect=True)
            for query in queries:
                cursor.execute(query)
            self.connect.commit()
            
if __name__ == "__main__":
    db = Database()