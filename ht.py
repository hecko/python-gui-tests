#!/usr/bin/env python3

import dateutil.parser
from dateutil import tz
import tkinter as tk
import time
import pytz
import requests


def update():
    try:
        url = "http://lorawan.sk:8000/api/node/kuyqiyvsetnsf43grs8ozumh5fipytqs"
        n = requests.get(url, timeout=5).json()
        chLabel2["text"] = str(round(n["keys"][0]["last_value"], 1)) + "°C"
        chLabel4["text"] = str(int(n["keys"][1]["last_value"])) + "%"
        last_point = dateutil.parser.parse(n["last_point"])
        chLabel5["text"] = str(last_point.astimezone(tz.tzlocal()))
    except Exception as e:
        print(e)
    root.after(50000, update)


root = tk.Tk()

chLabel2 = tk.Label(root, text="", font=("Helvetica", 100))
chLabel2.grid(row=0, column=0)

chLabel4 = tk.Label(root, text="", font=("Helvetica", 100))
chLabel4.grid(row=1, column=0)

chLabel5 = tk.Label(root, text="", font=("Helvetica", 20))
chLabel5.grid(row=2, column=0)

update()
root.mainloop()
