from weather_data_class import weather_data
import csv


city_weather = weather_data("Almaty", 2,"2024-05-26")
current_weather_data = city_weather.get_current_weather_data()
print(current_weather_data)

data = [
    ["City", "Country", "Date", "Temperature (C)", "Weather condition", "Humidity", "Wind speed (km/h)",
     "Wind direction"],
    [
        current_weather_data["location"]["name"],
        current_weather_data["location"]["country"],
        current_weather_data["location"]["localtime"],
        int(current_weather_data["current"]["temp_c"]),
        current_weather_data["current"]["condition"]["text"],
        int(current_weather_data["current"]["humidity"]),
        current_weather_data["current"]["wind_kph"],
        current_weather_data["current"]["wind_dir"]
    ]
]


with open("collected_weather_data.csv", "w", newline='') as csv_file:
    csv_file.write(str(data))

