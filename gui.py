from tkinter import *
import requests


root = Tk() 
def apiCall():
    url = "https://api.adviceslip.com/advice"
    response = requests.request("GET", url)
    var.set(response.text)
    root.after(1000, apiCall)


var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

root.after(1000, apiCall)
label.pack()
root.mainloop() 