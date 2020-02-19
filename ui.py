#!/usr/bin/python

import tkinter
from PIL import Image, ImageTk
top = tkinter.Tk()
top.geometry('2000x2000+35+35')
p1 = tkinter.PhotoImage(file = 'daxkoLogo.png') 
img = ImageTk.PhotoImage(file="daxkoLogo.png")
panelImg =  tkinter.Label(top, image = img)
panelImg.pack(side = "top", fill = "both", expand = "yes")
panelText=tkinter.Label(top, text="Face Recognition Based Attendance System",font=("Arial Bold", 28),fg="blue")
panelText.pack(side = "top", fill = "both", expand = "yes")
# Setting icon of master window 
top.iconphoto(False, p1) 
  
#top.iconbitmap('icon1.png')
fm=tkinter.Frame(top)
# Code to add widgets will go here...
top.title("Daxko Member Check In")

tkinter.Label(fm, text='Enter Name',font=("Arial Bold", 35),fg="red",pady=30).grid(row=0) 
tkinter.Label(fm, text='Enter ID',font=("Arial Bold", 35),fg="red").grid(row=1) 
e1 = tkinter.Entry(fm,width=40) 
e2 = tkinter.Entry(fm,width=40) 
e1.grid(row=0, column=1,ipady=10,pady=30) 
e2.grid(row=1, column=1,ipady=10)
b1= tkinter.Button(fm,text="Take Image",fg="yellow",bg="red",font=("Arial Bold", 35))
b2= tkinter.Button(fm,text="Train Image",fg="yellow",bg="red",font=("Arial Bold", 35))
b3= tkinter.Button(fm,text="Check in",fg="yellow",bg="red",font=("Arial Bold", 35))
b1.grid(row=2, column=0,pady=30)
b2.grid(row=2, column=2,pady=30)
b3.grid(row=3, column=1,pady=30)
fm.pack()
top.mainloop()