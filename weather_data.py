import requests
import requests.exceptions


def get_current_weather():
    #http://api.weatherapi.com/v1/current.json?key=c70ccfb2c56143f5893175705242604&q=London&aqi=no
    url = 'http://api.weatherapi.com/v1/current.json'
    city =(input())
    params = {'key': 'c70ccfb2c56143f5893175705242604',
              'q' : city,
              'aqi' : 'no'
    }
    r = requests.get(url, params)
    result = r.json()
    print(result)


get_current_weather()