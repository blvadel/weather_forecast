import requests
import json


def get_current_weather():
    #http://api.weatherapi.com/v1/current.json?key=c70ccfb2c56143f5893175705242604&q=London&aqi=no
    url = 'http://api.weatherapi.com/v1/current.json'
    city =(input())
    params = {'key': 'c70ccfb2c56143f5893175705242604',
              'q' : city
    }
    r = requests.get(url, params)
    s_code = r.status_code
    result = r.content
    result_dict = json.loads(result)
    result_dict_beauty = json.dumps(result_dict, indent=4, ensure_ascii=False)
    print(f'Status code is {s_code}')
    print(result_dict_beauty)
    print(f'City - {result_dict["location"]["name"]}',
          f'Country - {result_dict["location"]["country"]}',
          f'Temperature - {int(result_dict["current"]["temp_c"])} C',
          f'Weather condition - {result_dict["current"]["condition"]["text"]}',
          f'Humidity - {int(result_dict["current"]["humidity"])}',
          f'Wind speed - {result_dict["current"]["wind_kph"]} km/h',
          f'Wind direction - {result_dict["current"]["wind_dir"]}', sep ='\n')


get_current_weather()