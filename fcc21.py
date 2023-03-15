# Build A Weather App
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Build A Weather App')
root.iconbitmap('C:/Users/bhati/hello/Tkinter/home_house_icon_250568.ico')
root.geometry('400x40')
root.configure(background="green")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=74741B5E-1C67-4EFF-BFF6-CDD787EB1196




try:
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=74741B5E-1C67-4EFF-BFF6-CDD787EB1196')
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background="green")
myLabel.pack()

root.mainloop()