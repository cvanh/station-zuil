# /usr/bin/env python
from dotenv import load_dotenv
import requests
import os
import tkinter as tk
import datetime
from utils.db import db
from PIL import Image, ImageTk
from io import BytesIO

load_dotenv()

# this class will help is fetch the data from the diffrent sources
class getters:
    def __init__(self,city) -> None:
        # define for which city we want to fetch data
        self.city = city

        # set up an database connection pool
        self.db = db()

        # fetch the data from the diffrent sources
        self.get_facilites()
        self.get_messages()
        self.get_weather_prediction()


    def get_messages(self):
        self.db.cur.execute(f"SELECT * FROM public.comments WHERE station ILIKE '%{self.city}%' ORDER BY time DESC LIMIT 5")
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

        # call the constructor for the getter class
        super().__init__(self.city)

        #setting title
        root.title(f"{self.city}'s station zuil")

        #setting window size
        width=1000
        height=500

        # get the screen size so we can calculate how to center the window
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()

        # align window to the center of the screen
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        self.draw_comments(root)
        self.draw_weather(root)
        self.draw_facilities(root)

    # stolen from: https://stackoverflow.com/questions/55874159/python-3-tkinter-image-from-url-not-displaying
    def draw_weather(self,root):
        # check which icon is needed for the weather type
        weather_type = self._weather_prediction["weather"][0]["icon"]

        URL = f"https://openweathermap.org/img/wn/{weather_type}@2x.png"
        req = requests.get(URL)

        im = Image.open(BytesIO(req.content))
        photo = ImageTk.PhotoImage(im)

        image = tk.Label(image=photo)
        image.image = photo
        image.grid(column=2,row=1)

        label = tk.Label(text="weather icon",width=15)
        
        label.grid(column=2,row=0)



    def draw_facilities(self,root):
        facilities = tk.Text(root,height=25, width=50)

        # draw all the facilities 
        facilities.insert("end",f"station city: {self.services['station_city']}  \n")
        facilities.insert("end",f"country: {self.services['country']}  \n")
        facilities.insert("end",f"ov bike: {self.services['ov_bike']}  \n")
        facilities.insert("end",f"elevator: {self.services['elevator']}  \n")
        facilities.insert("end",f"toilet: {self.services['toilet']}  \n")
        facilities.insert("end",f"pr: {self.services['park_and_ride']}  \n")

        facilities.grid(column=1,row=0)

        # disable text box input 
        facilities.config(state="disabled") 

    
    def draw_comments(self,root):
        comments = tk.Text(root,height=25, width=50)

        # loop trough all the comments and insert them     
        for comment in self.messages:
            date = datetime.datetime.utcfromtimestamp(comment["time"]).strftime('%Y-%m-%d')
            comments.insert("end",f"on {date} {comment['name']} said: {comment['message']} \n")

        comments.grid(column=0,row=0)

        # disable text box input 
        comments.config(state="disabled")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root,"Leiden")
    root.mainloop()