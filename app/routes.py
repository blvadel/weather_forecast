from flask import Flask, request, jsonify
from weather_data import WeatherData
app = Flask(__name__)

@app.route("/")
def weather_forecast_main():
    return 'Weather Forecast, use "/weather", "/forecast", "exact_forecast"'

@app.route("/weather",methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Parameter "city" is required.'}), 400

    days = request.args.get('days')
    exact_date = request.args.get('exact_date')
    weather_data = WeatherData(city, days, exact_date)
    weather_info = weather_data.get_current_weather_data()
    return weather_info


@app.route("/forecast",methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    days = request.args.get('days')
    if not city or not days:
        return jsonify({'error': 'Parameters "city" and "days" are required.'}), 400

    exact_date = request.args.get('exact_date')
    weather_data = WeatherData(city, days, exact_date)
    weather_info = weather_data.get_weather_forecast()
    return weather_info


@app.route("/exact_forecast",methods=['GET'])
def get_exact_forecast():
    city = request.args.get('city')
    days = request.args.get('days')
    exact_date = request.args.get('exact_date')
    if not city or not exact_date:
        return jsonify({'error': 'Parameters "city" and "exact_date" are required.'}), 400
    weather_data = WeatherData(city, days, exact_date)
    weather_info = weather_data.get_future_forecast()
    return weather_info



if __name__ == '__main__':
    app.run(debug=True)