from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import os  # elle nous permet de faire des actions au niveau du system


class categorie:

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x750+0+1")
        self.root.minsize(620, 450)
        self.root.config(bg="#e4e8ff")
        self.root.focus_force()# elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Catégorie")


# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = categorie(root)
    root.mainloop()
