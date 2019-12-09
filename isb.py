'''
Importing required Tkinter
'''
from tkinter import *
from tkinter import messagebox
import os

PATH = os.getcwd()
'''
Definition of the Menubar-Functions, Load, Save, Quit, etc..
'''
'''
projectFiles = []
for item in os.getcwd():
    projectFiles.append(item)
for item in projectFiles:
    print(projectFiles[item])
'''
#clicked = StringVar()
#clicked.set(projectFiles[0])



def loadFile():
    print("Load File TODO State")

def saveFile():
    print("Save File TODO State")

def quitISB():
    quit()

def infBox():
    messagebox.showinfo("Information", "(c)2019 T. Kramer\n Version 1.0")



#########################################
window = Tk()
menu = Menu(window)
window.config(menu=menu, background="black")
window.title("ISB-Projektverwaltung")
window.geometry("800x600")
window.resizable(False, False)
#########################################

#projectSelection = OptionMenu(window,clicked,projectFiles)

projectList = Frame(master=window, bg="white")
projectList.place(x=10,y=10, width=250, height=500)
projectS = Listbox(projectList)
for root, dirs, files in os.walk(PATH):
    head, tail = os.path.split(PATH)
    for file in files:
        if file.endswith(".py"):
            projectS.insert(END,file)
        #projectS.insert(END, file)
projectS.pack()

projectInfoBox = Canvas(master=window, bg="white")
projectInfoBox.place(x=280,y=10,height=500, width=510)



###############Definition der Menueleiste
filemenu = Menu(menu)
projectmenu = Menu(menu)
configmenu = Menu(menu)
infomenu = Menu(menu)
########################################

#Aufbau der Menueleiste
menu.add_cascade(label="Datei", menu=filemenu)
menu.add_cascade(label="Projekt", menu=projectmenu)
menu.add_cascade(label="Konfiguration", menu=configmenu)
menu.add_cascade(label="Information", menu=infomenu)

filemenu.add_command(label="Laden", command=loadFile)
filemenu.add_command(label="Speichern", command=saveFile)
filemenu.add_command(label="Beenden", command=quitISB)
infomenu.add_command(label="Info", command= infBox)


##############
window.mainloop()
