import requests
import json
import schedule
import time
from constants import API_KEY, URL, TP

class WeatherData:
    key = API_KEY
    url = URL
    tp = TP
    def __init__(self, city, days,exact_date):
        self.city = city
        self.days = days
        self.exact_date = exact_date


    def get_current_weather_data(self):
        endpoint = 'current.json'
        params = {'key': self.key,
                  'q': self.city
                  }
        url = f"{URL}{endpoint}"
        r = requests.get(url, params)
        s_code = r.status_code
        current = r.content
        current_dict = json.loads(current)
        print(f'Status code is {s_code}')
        result = '\n'.join([
            f'City - {current_dict["location"]["name"]}',
            f'Country - {current_dict["location"]["country"]}',
            f'Date - {current_dict["location"]["localtime"]}',
            f'Temperature - {int(current_dict["current"]["temp_c"])} C',
            f'Weather condition - {current_dict["current"]["condition"]["text"]}',
            f'Humidity - {int(current_dict["current"]["humidity"])}',
            f'Wind speed - {current_dict["current"]["wind_kph"]} km/h',
            f'Wind direction - {current_dict["current"]["wind_dir"]}'
        ])
        print(result)
        return current_dict




    def get_weather_forecast(self):
        endpoint = 'forecast.json'
        params = {'key': self.key,
                  'q': self.city,
                  'days': self.days,
                  'tp': self.tp
                  }
        url = f"{URL}{endpoint}"
        r = requests.get(url, params)
        s_code = r.status_code
        forecast = r.content
        forecast_dict = json.loads(forecast)
        print(f'Status code is {s_code}')
        print(forecast_dict)
        return forecast_dict




    def get_future_forecast(self):
        endpoint = 'future.json'
        params = {'key': self.key,
                  'q': self.city,
                  'dt': self.exact_date,
                  'tp': self.tp
                  }
        url = f"{URL}{endpoint}"
        r = requests.get(url, params)
        s_code = r.status_code
        future = r.content
        future_dict = json.loads(future)
        print(f'Status code is {s_code}')
        return future_dict


    def schedule_weather(self):
        current_weather = self.get_current_weather_data()
        with open("collected_weather_data.csv", "a", newline='') as csv_file:
            csv_file.write(json.dumps(current_weather) + "\n")

    def start_scheduler(self):
        schedule.every(1).minutes.do(self.schedule_weather)
        while True:
            schedule.run_pending()
            time.sleep(1)


