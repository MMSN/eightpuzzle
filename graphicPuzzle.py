from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y
    #tkimage = PhotoImage(file='green1gif.gif')
    #label = Label(frame, image=tkimage).pack() 
    #label.image = tkimage
    #label.pack() 
    img = PhotoImage(file="green1gif.gif")
    button = Button(root, image=img)
    button.img = img  # store a reference to the image as an attribute of the widget
    button.grid()

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
"""
#!/usr/bin/python

import Tkinter as tk
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()"""