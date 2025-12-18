import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/"
FONT = ('consolas', 12)

class Backend:
    def __init__(self, base_url, api_key):
        self.url = base_url
        self.api = api_key

    def validate(self, city):
        response = requests.get(self.url + f"forecast?q={city}&units=metric&appid={self.api}")
        if response.status_code == 200:
            return True
        else:
            print("API Error:", response.json().get("message", "Unknown error"))
        return False


    def getData(self, city):
        response = requests.get(self.url + f"forecast?q={city}&units=metric&appid={self.api}")
        data = response.json()
        return data

    def cleanData(self, city):
        jsonData = self.getData(city)

        temp = jsonData['list'][0]['main']['temp']
        pressure = jsonData['list'][0]['main']['pressure']
        humidity = jsonData['list'][0]['main']['humidity']
        windSpeed = jsonData['list'][3]['wind']['speed']
        precipitation = jsonData['list'][4]['pop']

        return {
            'temp': temp,
            'pressure': pressure,
            'humidity': humidity,
            'windSpeed': windSpeed * 3.6,
            'precipitation': precipitation * 100,
        }
    
weatherApp = Backend(BASE_URL, API_KEY)    
def main():
    cname = cityName.get().strip().lower().replace(" ", "+")
    if weatherApp.validate(cname):
        data = weatherApp.cleanData(cname)
        tempLabel.config(text=f"Temperature : {data['temp']} °C")
        humidityLabel.config(text=f"Humidity : {data['humidity']} %")
        windLabel.config(text=f"Wind Speed : {data['windSpeed']:.2f} km/h")
        pressureLabel.config(text=f"Pressure : {data['pressure']} hPa")
        precipitationLabel.config(text=f"Precipitation : {data['precipitation']} %")

    else:
        messagebox.showerror("Error", "Something went wrong, check city name !")    

window = tk.Tk()
window.title("Weather App")

cityName = tk.StringVar(window)

window_w = 600
window_h = 400
window.resizable(False, False)

window.update_idletasks()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

# to make sure that window is centered in the screen when running the code
x = int((screen_w / 2) - (window_w / 2))
y = int((screen_h / 2) - (window_h / 2))
window.geometry(f"{window_w}x{window_h}+{x}+{y}")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

searchFrame = tk.Frame(window)
searchFrame.grid(column=0, row=0, sticky="n", pady=20)

labelFrame = tk.Frame(window)
labelFrame.grid(column=0, row=1, sticky="nw", pady=20)

searchFrame.columnconfigure(0, weight=1)
searchFrame.columnconfigure(1, weight=1)
searchFrame.columnconfigure(2, weight=1)
searchFrame.rowconfigure(0, weight=1)

labelFrame.columnconfigure(0, weight=1)
labelFrame.rowconfigure(0, weight=1)
labelFrame.rowconfigure(1, weight=1)
labelFrame.rowconfigure(2, weight=1)
labelFrame.rowconfigure(3, weight=1)
labelFrame.rowconfigure(4, weight=1)

label = tk.Label(searchFrame, text="City : ", font=('consolas'))
label.grid(column=0, row=0)

cityInput = tk.Entry(searchFrame, textvariable=cityName, font=('consolas'))
cityInput.grid(column=1, row=0)

submitBtn = tk.Button(searchFrame, text="Search", command=main)
submitBtn.grid(column=2, row=0, pady=15)

tempLabel = tk.Label(labelFrame, text="Temperature : ... °C", font=FONT, anchor='w', justify='left')
tempLabel.grid(column=0, row=0, pady=8, sticky="w", padx=50)

humidityLabel = tk.Label(labelFrame, text="Humidity : ... %", font=FONT, anchor='w', justify='left')
humidityLabel.grid(column=0, row=1, pady=8, sticky="w", padx=50)

windLabel = tk.Label(labelFrame, text="Wind Speed : ... km/h", font=FONT, anchor='w', justify='left')
windLabel.grid(column=0, row=2, pady=8, sticky="w", padx=50)

pressureLabel = tk.Label(labelFrame, text="Pressure : ... hPa", font=FONT, anchor='w', justify='left')
pressureLabel.grid(column=0, row=3, pady=8, sticky="w", padx=50)

precipitationLabel = tk.Label(labelFrame, text="Precipitation : ... %", font=FONT, anchor='w', justify='left')
precipitationLabel.grid(column=0, row=4, pady=8, sticky="w", padx=50)


window.mainloop()