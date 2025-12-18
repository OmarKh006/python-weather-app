# 🌦️ Weather App (Python Tkinter)

A simple desktop **Weather Application** built using **Python**, **Tkinter**, and the **OpenWeatherMap API**. The app allows users to search for a city and displays real-time weather information such as temperature, humidity, wind speed, pressure, and precipitation.

---

## ✨ Features

- Clean and simple **Tkinter GUI**
- Fetches live weather data using **OpenWeatherMap API**
- Displays:

  - 🌡️ Temperature (°C)
  - 💧 Humidity (%)
  - 🌬️ Wind Speed (km/h)
  - 🧭 Atmospheric Pressure (hPa)
  - ☔ Precipitation Probability (%)

- Input validation with error handling
- Centered, fixed-size window for better UI experience

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Requests** (HTTP requests)
- **OpenWeatherMap API**

---

## 📂 Project Structure

```
weather-app/
│
├── weather_app.py   # Main application file
├── README.md        # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- Internet connection

Install required dependency:

```bash
pip install requests
```

---

### 2️⃣ Get an API Key

1. Create an account at **OpenWeatherMap**
2. Generate a free API key
3. Replace the API key in the code:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

⚠️ **Note:** Do not share your real API key publicly.

---

### 3️⃣ Run the Application

```bash
python weather_app.py
```

---

## 🖥️ How It Works

1. User enters a city name
2. App sends a request to OpenWeatherMap **forecast API**
3. Data is fetched and cleaned using the `Backend` class
4. Weather details are displayed on the GUI
5. Invalid city names trigger an error message

---

## 📊 Data Source

- Endpoint used: `https://api.openweathermap.org/data/2.5/forecast`
- Units: Metric

---

## ⚠️ Error Handling

- Handles invalid city names
- Displays API error messages when requests fail
- Prevents app crashes due to bad responses

---

## 🧠 Future Improvements

- Add weather icons
- Display 5-day forecast
- Auto-detect user location
- Dark mode UI
- Cache API responses
- Convert app to `.exe`

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👤 Author

**Omar Khairy**
Python & Web Development Learner

Feel free to review the code and suggest improvements 🚀
