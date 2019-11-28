# !/usr/bin/python3
from tkinter import *

import tkinter

top = Tk()
li = [IntVar(), IntVar()]


def sel():
    d = ["Music", "Video"]
    res = ""
    i = 0
    for l in li:
        if l.get():
            res += d[i]
            res += " "
            i += 1
    print(res)
    label.config(text=res)


C1 = Checkbutton(top, text="Music",
                 variable=li[0],
                 onvalue=1,
                 offvalue=0,
                 height=5,
                 width=20,
                 command=sel)
C2 = Checkbutton(top,
                 text="Video",
                 variable=li[1],
                 onvalue=1,
                 offvalue=0,
                 height=5,
                 width=20,
                 command=sel)
label = Label(top)
C1.pack()
C2.pack()
label.pack()
top.mainloop()
