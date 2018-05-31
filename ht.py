#!/usr/bin/env python3

import tkinter as tk
import time

def update():
    chLabel1['text'] = time.time()
    chLabel2['text'] = time.time()
    chLabel3['text'] = time.time()
    root.after(1000, update)

root = tk.Tk()

chLabel1 = tk.Label(root, text="Channel group", font=('Helvetica', 30))
chLabel1.grid(row=0, column=0)

chLabel2 = tk.Label(root, text="Channel group", font=('Helvetica', 30))
chLabel2.grid(row=0, column=1)

chLabel3 = tk.Label(root,
    text="Channel group",
    height=5,
    font=('Helvetica', 30))
chLabel3.grid(row=1, column=0)

chLabel4 = tk.Label(root,
    text="Channel group",
    height=5,
    font=('Helvetica', 30))
chLabel4.grid(row=1, column=1)

update()

root.mainloop()

