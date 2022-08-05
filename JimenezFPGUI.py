# JimenezFP
# Programmer: Mark Jimenez
# Email: mjimenez43@cnm.edu
# Purpose: To create a password manager

import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from PasswordManager import PasswordManager



window = tk.Tk()


window.geometry("900x500")

window.title("Password Manager")


mainFile = open("Password.txt", "a+")
mainFile.seek(0)
mainpwd = mainFile.readline().rstrip()

def start_btn_click():
    startLabel.destroy()
    start.destroy()
    

    
    enterMP.place(relx = 0.5, rely = 0.57, anchor = CENTER)
    enterBMP.place(relx = 0.5, rely = 0.65, anchor = CENTER)
    
        
    if mainpwd == "":
        labelMP.place(relx = 0.5, rely = 0.5, anchor = CENTER )

    else:
        labelMP2.place(relx = 0.5, rely = 0.5, anchor = CENTER )
          

def enter_mp_click():

    if mainpwd == "":
        mainPassword = enterMP.get()
        mainFile.write(mainPassword)
        mainFile.close()
        pass    
        
    else:
        attempt = enterMP.get()    
        if attempt == mainpwd:
            pass
        else:
            mb.showerror("OOPS!", "Thats the incorrect password!")
            start.invoke()
                
            
    
    enterMP.get()
    view.place(x = 100, y = 0)
    add.place(x = 350, y = 0)
    stop.place(x = 600, y = 0)
    intro.place(x = 100, y = 117)
    enterBMP.destroy()
    enterMP.destroy()
    labelMP.destroy()
    labelMP2.destroy()


def view_btn_click():

    viewPwd.place(x = 100, y = 250)
    textFile = open("Password.txt", "r")
    stuff = textFile.read()
    viewPwd.insert(END, stuff)
    textFile.close()
    
    info.place_forget()
    enter.place_forget()



def add_btn_click():
    
    info.place(x = 100, y = 200)
    enter.place(x = 100, y = 235)
    enterBtn.place(x = 360, y = 265)
    
    viewPwd.place_forget()
    
    
def enter_btn_click():
    x = enter.get()
    info = x.split(",")
    user_info = PasswordManager()
    user_info.add(info)
    enter.delete(0, END)
    enter.place_forget()
    
    
def quit_btn_click():
    mb.showinfo("Until Next Time!", "Goodbye!")
    window.destroy()

startLabel = Label(window, text = "Welcome to Password Manager!\nClick ENTER to enter.")
startLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)

start = Button()
start.config(height = 1, width = 5, text = "ENTER", bg = "pink", command = start_btn_click)
start.place(relx = 0.5, rely = 0.5, anchor = CENTER)

view = Button()
view.config(height = 5, width = 20, text ="VIEW", bg = "pink", command = view_btn_click)


add = Button()
add.config(height = 5, width = 20, text = "ADD", bg = "pink", command = add_btn_click)


enterBtn = Button(height = 1, width = 10, text = "Enter", command = enter_btn_click)

viewPwd = Text(window, height = 10, width = 80, borderwidth = 1, relief = "solid")

stop = Button()
stop.config(height = 5, width = 20, text = "QUIT", bg = "pink", command = quit_btn_click)


intro = Label(window, text = "Please select a button\nSelect VIEW if you want to view your passwords\nSelect ADD if you want to add a new password\nSelect QUIT to quit the app.", 
bd = 1, relief = "solid", height = 5, width = 92)


enter = Entry(window, width = 106, borderwidth = 5)

info = Label(window, text = "Please enter a keyword for the account, followed by the username and the password in that order. \nPlease be comma separated! (Ex: Facebook, John_smith, password1234) :")
info.config( height = 2, width = 92)


labelMP = Label(window, text = "Please enter a master password: ")

labelMP2 = Label(window, text = "Please enter your master password: ")

enterMP = Entry(window, width = 50, borderwidth = 5, show = "*")


enterBMP = Button()
enterBMP.config(height = 1, width = 7, text = "ENTER", bg = "pink", command = enter_mp_click)

window.mainloop()
