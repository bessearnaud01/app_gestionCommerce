from tkinter import *
from tkinter import ttk, messagebox

from tkinter import messagebox

import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Produit:

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x580+300+50")
        self.root.minsize(620, 450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Produit")

        Label(self.root, text="PRODUIT",  font=("Helvetica", 14, "bold"), bg="#e4e8ff", fg="black").place(x=0, y=0, relwidth=1, height=50)
          # ListeFrame = tableau
        ProduitFrame = Frame(self.root, bd=3, relief=RIDGE)
        ProduitFrame.place(x=10, y=60, height=450,width=350)
        Label(ProduitFrame, text="Détail produit",  font=("Helvetica", 11, "bold"), bg="#e4e8ff", fg="black").place(x=0, y=0, relwidth=1, height=50)
        
        Label(ProduitFrame, text="Catégorie :",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=90)
                                                                               
        entreType = ttk.Combobox(ProduitFrame, values=("Administrateur", "Employé"), font=("times new roman", 10, "bold"), state="r")                      
        entreType.set("Select")
        entreType.place(x=120, y= 90, width=140)

        Label(ProduitFrame, text="Fournisseur :",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=120)
                                                                               
        entreType = ttk.Combobox(ProduitFrame, values=("Administrateur", "Employé"), font=("times new roman", 10, "bold"), state="r")                      
        entreType.set("Select")
        entreType.place(x=120, y= 120, width=140)

        Label(ProduitFrame, text="Nom :",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=150)
        Entry(ProduitFrame, font=("times new roman", 10, "bold"), bd=2).place(x=120, y=150,width=140)

        Label(ProduitFrame, text="Prix:",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=180)
        Entry(ProduitFrame, font=("times new roman", 10, "bold"), bd=2).place(x=120, y=180,width=140)

        Label(ProduitFrame, text="Quantité:",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=210)
        Entry(ProduitFrame, font=("times new roman", 10, "bold"), bd=2).place(x=120, y=210,width=140)

        Label(ProduitFrame, text="Status:",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,y=240)
        entreType = ttk.Combobox(ProduitFrame, values=("Administrateur", "Employé"), font=("times new roman", 10, "bold"), state="r")                      
        entreType.set("Select")
        entreType.place(x=120, y= 240, width=140)


        
        self.btnAjouter = Button(ProduitFrame, text="Ajouter", state="normal",   font=("Helvetica", 9, "bold"),fg="white" ,bg="green", cursor="hand2")
                              
        self.btnAjouter.place(x=10, y=300, width=70)

        self.btnModifier = Button(ProduitFrame, text="Modifier", state="disabled", font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")

                                
        self.btnModifier.place(x=85, y=300, width=70)

        self.btnReinstaller = Button(ProduitFrame,text="Réinstaller", font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")
                                    
        self.btnReinstaller.place(x=160.5, y=300, width=70)

        self.btnSupprimer = Button(ProduitFrame, text="Supprimer", state="disabled",font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")
                                   
        self.btnSupprimer.place(x=239, y=300, width=70)







# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Produit(root)
    root.mainloop()
