import requests
import json

class weather_data():
    key = "c70ccfb2c56143f5893175705242604"

    def __init__(self, city, days,exact_date):
        self.city = city
        self.days = days
        self.exact_date = exact_date


    def get_current_weather_data(self):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {'key': self.key,
                  'q': self.city
                  }
        r = requests.get(url, params)
        s_code = r.status_code
        current = r.content
        current_dict = json.loads(current)
        current_dict_beauty = json.dumps(current_dict, indent=4, ensure_ascii=False)
        print(f'Status code is {s_code}')
        return current_dict




    def get_weather_forecast(self):
        url = "http://api.weatherapi.com/v1/forecast.json"
        params = {'key': self.key,
                  'q': self.city,
                  'days': self.days
                  }
        r = requests.get(url, params)
        s_code = r.status_code
        forecast = r.content
        forecast_dict = json.loads(forecast)
        print(f'Status code is {s_code}')
        return forecast_dict



    def get_future_forecast(self):
        url = 'http://api.weatherapi.com/v1/future.json?'
        params = {'key': self.key,
                  'q': self.city,
                  'dt': self.exact_date
                  }
        r = requests.get(url, params)
        s_code = r.status_code
        future = r.content
        future_dict = json.loads(future)
        print(f'Status code is {s_code}')
        return future_dict






