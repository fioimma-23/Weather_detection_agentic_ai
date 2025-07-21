# 🌦️ Weather Detection using Agentic AI

This is a modular, agent-based Python script that fetches real-time weather information using the OpenWeatherMap API. It uses [Microsoft Autogen](https://github.com/microsoft/autogen) to simulate agent interactions for decision-making based on weather data.

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/fioimma-23/Weather_detection_agentic_ai.git
cd Weather_detection_agentic_ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Open `weather_agent.py` or `main.py` and replace:

```python
API_KEY = "your_api_key_here"
```

with your actual API key from OpenWeatherMap.

### 4. Run the Script

```bash
python weather_agent.py
```

---

## 🔐 Get an OpenWeatherMap API Key

1. Go to [https://openweathermap.org/](https://openweathermap.org/)
2. Sign up or log in
3. Navigate to **API keys**
4. Generate a key
5. Replace `API_KEY` in the code with your generated key

---

## 📋 Example

```bash
Enter the city: Paris
Weather: Rain, Temp: 21°C
```

---

## 🤖 How It Works

### 1. WeatherAgent

- Sends an HTTP GET request to OpenWeatherMap API with the city name and API key
- Parses the returned JSON data

### 2. DecisionAgent

- Checks for errors in weather data
- If valid, extracts the main weather condition and temperature
- Returns a formatted result like:

```yaml
Weather: Clear, Temp: 29°C
```

---

## 💡 Features

- ✅ Agent-based modular design  
- 🌍 Real-time weather data  
- 🧠 Extendable for AI decision logic  
- 💡 Simple and clean structure

---

## 🛠️ Tech Stack

- Python 3.10+
- `requests` for API calls
- Microsoft Autogen
- OpenWeatherMap API
