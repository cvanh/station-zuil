import psycopg2, psycopg2.extras
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
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def disconnect(self):
        self.conn.close()
        self.cur.close()
    
    # use this one if you are making a insert query
    def insert(self,sql):
        print(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as err:
            print(err)

    # use this one if you are making a select query
    def select(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as err:
            print(err)