import autogen
import requests

class WeatherAgent(autogen.ConversableAgent):
    def get_weather(self, city, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return {"error"}

class DecisionAgent(autogen.ConversableAgent):
    def fetch_weather(self, weather_data):
        if 'error' in weather_data:
            return "Data unavailable"
        
        main = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']
        result = f"Weather: {main}, Temp: {temp}C"

        return result
    
weather_agent = WeatherAgent(name="WeatherAgent")
decision_agent = DecisionAgent(name="DecisionAgent")

def weather_detection(city, api_key):
    weather_data = weather_agent.get_weather(city, api_key)

    result = decision_agent.fetch_weather(weather_data)
    print(result)

if __name__ == "__main__":
    API_KEY = " " #your api key
    city = input("Enter the city: ")
    weather_detection(city, API_KEY)
