# Change Colors in our Weather App
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Change Colors in our Weather App')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry('400x40')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=74741B5E-1C67-4EFF-BFF6-CDD787EB1196




try:
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=74741B5E-1C67-4EFF-BFF6-CDD787EB1196')
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
    
    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990060"
    elif category == "Hazardous":
        weather_color = "#660000"

    root.configure(background=weather_color)
    
    
    myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
    myLabel.pack()

except Exception as e:
    api = "Error..."



root.mainloop()