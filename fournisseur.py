from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Fournisseur:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1020x650+200+1")
        self.root.minsize(620, 450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Fournisseur")

        Label(self.root, text="Id employé :", bg="white", font=("times new roman", 12, "bold"), cursor="hand2").place(x=590, y=20)
          

        self.txtId = Entry(self.root,bg="lightyellow", font=("times new roman", 12, "bold"), bd=2)
        self.txtId.place(x=700, y=20, width=150)

        Button(self.root, text="Rechercher:", font=("Helvetica", 9, "bold"),fg="white", bg="blue",cursor="hand2").place(x=855, y=20, width=100)

        Button(self.root, text="Tout", font=("Helvetica", 9, "bold"),fg="black", bg="lightgrey",cursor="hand2").place(x= 960, y=20, width=50)
            
        # formulaire

        Label(self.root, text="Id fournisseur :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=40)  
        Entry(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=40, width=150)

        Label(self.root, text="Nom :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=80) 
        Entry(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=80, width=150)

        
        Label(self.root, text="Contact :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=120) 
        Text(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=120, width=150,height=50)




        
     

   



# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Fournisseur(root)
    root.mainloop()
