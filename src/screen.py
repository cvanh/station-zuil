# /usr/bin/env python
from dotenv import load_dotenv
import requests
import os
from tkinter import *
from tkinter import ttk
# import tkinter as ttk
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
        
    

class screen(getters):
    def __init__(self) -> None:
        super().__init__("Arnhem")
        self.draw()

    def draw():
        root = Tk()
        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        meters = StringVar()
        ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", calculate)

        root.mainloop()

screen()