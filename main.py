#imports
from Tkinter import *
from PIL import * 
from zipfile import *
from time import *

#file history

#file fo = "keys.txt"

#functions

def start():
    """This is start when archive open"""
    filePath = area.get()
    okMes.pack_forget()
    errMes.pack_forget()
    if is_zipfile(filePath):
        z = ZipFile(filePath, 'r')
        z.extractall()
        z.close()
        okMes.pack()
    else:
    	errMes.pack()
root = Tk()
#screen settings
errMes = Message(text="FILE not found or file is not ARHCIVE")
okMes = Message(text="FILE uziped success!")
img = PhotoImage(file = "zip.png")
root.geometry('300x200+40+80')
root.title("Zipper")

#elements
icon = Label(image=img)
lab = Label(text="Enter file name", font="Verdana 11")
btn = Button(text="UnZIP", command=start)
area = Entry(width=20)

#add to window

icon.pack()
lab.pack()
area.pack()
btn.pack()

root.mainloop()

#mainloop end
