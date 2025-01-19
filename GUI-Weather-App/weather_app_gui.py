from tkinter import *
import requests as rq
from time import strftime, gmtime
from suntime import Sun, SunTimeException
from sys import exit

root = Tk()

root.title("Weather App")

root.geometry("600x400")

api = "ENTER YOUR API KEY HERE"

title_label = Label(root, text="Weather App", font=("Helvetica", 40, "bold"))
title_label.pack(pady=10)

blank_label = Label(root, text="")
blank_label.pack(pady=10)

city_input = Entry(root, width=100, borderwidth=5, font=("Helvetica", 20))







root.mainloop()
