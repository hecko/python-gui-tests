#!/usr/bin/env python3

import tkinter as tk

def request_reading(event):
    outText.config(state=tk.NORMAL)
    outText.insert(tk.END, str(event) + " " + entry.get() + "\n")
    outText.insert(tk.END, str(listbox.curselection()) + "\n")
    outText.config(state=tk.DISABLED)
    return event

root = tk.Tk()

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)
listbox.grid(row=0, column=2, rowspan=2)

chLabel = tk.Label(root, text="Channel group")
chLabel.grid(row=0, column=0)

entry = tk.Entry(root, text="Enter something")
entry.insert(0, "default value")
entry.grid(row=2, column=1)

outText = tk.Text(root, bd=1, state=tk.DISABLED)
outText.grid(row=0, column=1, rowspan=2)

trigLabel = tk.Label(root, text="Trigger group")
trigButton = tk.Button(root,
    font=("Helvetica", 20),
    text="Trigger Settings",
)
trigButton.bind('<Button-1>', request_reading)
trigButton.grid(row=1, column=0)

horizLabel = tk.Label(root, text="Horizontal group")
horizButton = tk.Button(root, text="Horizontal settings")
horizButton.bind('<Button-1>', request_reading)
horizButton.grid(row=2, column=0)

root.mainloop()
