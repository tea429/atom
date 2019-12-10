from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry('500x500')

paint = Canvas(top)

paint.pack()

def sendingMail():
    message = messagebox.showinfo("No Implementation","Sorry this hasn't been coded yet!")

sendMail = Button(paint, text="Send Mail", command = sendingMail)
sendMail.place(x=50,y=50)
sendMail.pack()
top.mainloop()
