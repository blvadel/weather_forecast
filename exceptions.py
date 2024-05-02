from weather_data_class import weather_data


try:
    city_weather = weather_data("Almaty", 2, "2024-05-26")
    print(city_weather.get_current_weather_data())

except:
    print("error")