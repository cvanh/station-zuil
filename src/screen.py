# /usr/bin/env python
from dotenv import load_dotenv
import requests
import os
import tkinter as tk
import datetime
from utils.db import db
load_dotenv()

class getters:
    def __init__(self,city) -> None:
        # define for which city we want to fetch data
        self.city = city

        # set up an database connection pool
        self.db = db()

        # fetch the data
        self.get_facilites()
        self.get_messages()
        # self.get_weather_prediction()


    def get_messages(self):
        # TODO add station
        self.db.cur.execute(f"SELECT * FROM public.comments ORDER BY time DESC ")
        self.messages = self.db.cur.fetchall()
        return self.messages


    # get the facilities by the name of the city
    def get_facilites(self):
        self.db.cur.execute(f"SELECT * FROM station_service WHERE station_city = '{self.city}'")
        self.services = self.db.cur.fetchone()

        return self.services


    # get the weather prediction for the city
    def get_weather_prediction(self):
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.get_openweater_api_key}")
    
        if res.status_code != 200:
            raise LookupError("openweathermap didnt gave a http 200")
        
        self._weather_prediction = res.json()
        return self._weather_prediction

    # getter for the openweather api key that is stored in a .env
    @property 
    def get_openweater_api_key(self) -> str:
        return os.environ["OPENWEATHER_API_KEY"]
        
    

class App(getters):
    def __init__(self, root,city):
        self.city = city
        super().__init__(self.city)

        #setting title
        root.title(f"{self.city} station zuil")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.draw_comments(root)


    
    
    def draw_comments(self,root):
        comments = tk.Text(root,height=50, width=50)

        # loop trough all the comments and insert them     
        for comment in self.messages:
            date = datetime.datetime.utcfromtimestamp(comment["time"]).strftime('%Y-%m-%d')
            comments.insert("end",f"on {date} {comment['name']} said: {comment['message']} \n")

        comments.grid()

        # disable text box input 
        comments.config(state="disabled")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root,"Arnhem")
    root.mainloop()