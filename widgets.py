import tkinter as t
from tkinter.ttk import *
class Frame(t.Frame):
    def __init__(self, parent, border):
        if border is True:
            t.Frame.__init__(self, master=parent, highlightbackground="black", highlightthickness=1)
        else:
            t.Frame.__init__(self, master=parent)
        
class Label(t.Label):
    def __init__(self, parent, text, font=""):
        if font == "":
            t.Label.__init__(self, master=parent, text=text)
        else:
            t.Label.__init__(self, master=parent, text=text, font=font)

class Entry(t.Entry):
    def __init__(self, parent, justify, width):
        t.Entry.__init__(self, master=parent, justify=justify, width=width)

    def change_state(self, new_state):
        self.configure(state=new_state)

class Button(t.Button):
    def __init__(self, parent, text, command, width):
        t.Button.__init__(self, master=parent, text=text, command=command, width=width)

    def change_state(self, new_state):
        self.configure(state=new_state)

class Checkbutton(t.Checkbutton):
    def __init__(self, parent, variable, command=""):
        t.Checkbutton.__init__(self, master=parent, variable=variable, command=command)

    def change_state(self, new_state):
        self.configure(state=new_state)
