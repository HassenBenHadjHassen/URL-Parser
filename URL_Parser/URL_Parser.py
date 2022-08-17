import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from tkinter import *
import time

app = Tk()
app.title("URL Parser")
app.geometry("300x200")

#URL
URL_text = StringVar()
URL_label = Label(app, text="Enter URL: ", font=("bold", 13), pady = 20)
URL_label.grid(row=0,column=0, sticky=W)
URL_entry = Entry(app, textvariable=URL_text)
URL_entry.grid(row=0,column=1)

#Button
button_pressed = StringVar()
button = Button(app, text="Submit", command=lambda: button_pressed.set("button pressed"))
button.grid(row=1, column=1)
button.wait_variable(button_pressed)

try:
    url = URL_entry.get()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    for tag in tags:
        with open("output.txt", "a") as f:
            finale = tag.get("href")
            print(finale, file=f)
    parseMessage = StringVar()
    parseMessage_label = Label(app, text="Parsing Completed!", font=("bold", 11), foreground="Green")
    parseMessage_label.grid(row=2,column=0)
except:
    errorMessage = StringVar()
    errorMessage_label = Label(app, text="An Error \n Has occured \n please close the \n app and retry", font=("bold", 11), foreground="Red")
    errorMessage_label.grid(row=2,column=0)
#Start program
app.mainloop()
