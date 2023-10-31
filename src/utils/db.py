import psycopg2
from dotenv import load_dotenv
import os

class db:
    cur = None
    def __init__(self):
        load_dotenv()
        self.dbname = os.environ["DBNAME"]
        self.user = os.environ["DBUSER"]
        self.password = os.environ["DBPASSWORD"]
        self.dbhost = os.environ["DBHOST"]
        self.dbport = os.environ["DBPORT"]

        self.connect() 
    
    def connect(self):
        self.conn = psycopg2.connect(host=self.dbhost, port=self.dbport,dbname=self.dbname, user=self.user, password=self.password) 
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.close()
        self.cur.close()
    
    def execute(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as err:
            print(err)