from tkinter import Tk
from tkinter import Label
import time
import sys

main = Tk()
main.title("Digital Clock")

def getTime():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,getTime)



clock = Label(main, font=("Calibri", 90), bg="grey", fg="white" )
clock.pack()

getTime()
main.mainloop()
