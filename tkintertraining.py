#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colors.

author: Jan Bodar
last modified: January 2011
website: www.zetcode.com
"""

from Tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Colors")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        square1 = canvas.create_rectangle(30, 10, 120, 80, 
            outline="#fb0", fill="#fb0")
        square2 = canvas.create_rectangle(150, 10, 240, 80, 
            outline="#f50", fill="#f50")
        square3 = canvas.create_rectangle(270, 10, 370, 80, 
            outline="#05f", fill="#05f")
        
        square4 = canvas.create_rectangle(30, 100, 120, 170, 
            outline="#fb0", fill="#fb0")
        square5 = canvas.create_rectangle(150, 100, 240, 170, 
            outline="#f50", fill="#f50")
        square6 = canvas.create_rectangle(270, 100, 370, 170, 
            outline="#05f", fill="#05f")
               
        square7 = canvas.create_rectangle(30, 190, 120, 260, 
            outline="#fb0", fill="#fb0")
        square8 = canvas.create_rectangle(150, 190, 240, 260, 
            outline="#f50", fill="#f50")
        square9 = canvas.create_rectangle(270, 190, 370, 260, 
            outline="#05f", fill="#05f")       
        
        canvas.pack(fill=BOTH, expand=1)
        
    def key(self, event):
        print "pressed", repr(event.char)

    def callback(self, event):
        self.focus_set()
        print "clicked at", event.x, event.y


def main():
    
    root = Tk()
    ex = Example(root)
    root.geometry("400x400+300+300")
    #root = Frame(root, width=600, height=600)
    root.bind("<Key>", ex.key)
    root.bind("<Button-1>", ex.callback)
    #root.pack()
    root.mainloop()
    
    



if __name__ == '__main__':
    main()  
