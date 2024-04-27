import requests
import json

class weather_data():
    key = "c70ccfb2c56143f5893175705242604"

    def __init__(self, city, days,exact_date):
        self.city = city
        self.days = days
        self.exact_date = exact_date


    def get_current_weather_data(self):
        url = "http://api.weatherapi.com/v1/forecast.json"
        params = {'key': self.key,
                  'q': self.city
                  }
        r = requests.get(url, params)
        s_code = r.status_code
        current = r.content
        current_dict = json.loads(current)
        current_dict_beauty = json.dumps(current_dict, indent=4, ensure_ascii=False)
        print(f'Status code is {s_code}')
        print(current_dict_beauty)




    def get_weather_forecast(self):
        url = "http://api.weatherapi.com/v1/current.json"
        params = {'key': self.key,
                  'q': self.city,
                  'days': self.days
                  }
        r = requests.get(url, params)
        s_code = r.status_code
        forecast = r.content
        forecast_dict = json.loads(forecast)
        forecast_dict_beauty = json.dumps(forecast_dict, indent=4, ensure_ascii=False)
        print(f'Status code is {s_code}')
        print(forecast_dict_beauty)



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
        future_dict_beauty = json.dumps(future_dict, indent=4, ensure_ascii=False)
        print(f'Status code is {s_code}')
        print(future_dict_beauty)



city_weather = weather_data("Almaty", 2,"2024-05-26")
city_weather.get_current_weather_data()
city_weather.get_weather_forecast()
city_weather.get_future_forecast()





