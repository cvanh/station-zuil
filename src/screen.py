# /usr/bin/env python
from dotenv import load_dotenv
import requests
import os
from utils.db import db
load_dotenv()

# weather = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'")


class getters:
    def __init__(self,city) -> None:
        self.city = city

        self.db = db()
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

screen()