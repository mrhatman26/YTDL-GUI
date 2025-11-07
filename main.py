import tkinter as t
from tkinter.ttk import *
from tkinter import messagebox
from gui import MainWindow, MainApplicationLayout
if __name__ == "__main__":
    window = MainWindow("640x370", "YTDL GUI")
    MainApplicationLayout(window).pack()
    window.mainloop()
