from tkinter import Listbox
from tkinter import Button
from tkinter import *

app = Tk()

contacts = Listbox(app)
contacts.pack()

saveButton = Button(app,text='Save')
saveButton.place(x=50,y=50)

app.mainloop()