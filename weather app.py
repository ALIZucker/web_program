import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


print("salam")
root=tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.mainloop()