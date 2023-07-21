from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Caisse:

    def __init__(self, root):
        self.root = root
        self.root.geometry("950x580+300+20")
        self.root.minsize(620, 450)
        self.root.config(bg="lightgray")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Caisse")

        # Déclaration de variable
        self.var_recherche_text = StringVar()

        self.icon_title = ImageTk.PhotoImage(file=r"C:dossier_images\logo.png")
        Label(self.root, text="Caisse Magasin", image=self.icon_title, font=("Helvetica",14, "bold"),fg="white", bg="#e4e8ff",
              anchor="w", padx=9, compound=LEFT).place(x=0, y=0, relwidth= 75, height=95)
            
        Button(self.root, text="Déconnecter",command=self.login, font=("Helvetica", 12, "bold"), bg="orange",fg="white",cursor="hand2").place(x=800,y=20)
                                                                                                              
        Label(self.root, text="Bienvenu Chez BNAB \t\t Date: DD-MM-YYYY\t\t Heure: HH:MM:SS",
              font=("Helvetica", 12, "bold"), bg="#454545", fg="white").place(x=0, y=100, relwidth=1, height=50)
        
        # Creation de la fénêtre produit
        ListeProduit = Frame(self.root, bd=3, relief=RIDGE)
        ListeProduit.place(x=0, y=150, height=520,width=350)
        Label(ListeProduit, text="Tous les produits",font=("Helvetica", 12, "bold"), bg="orange", fg="white").place(x=0, y=0, relwidth=1, height=50)
        # creation de la fénêtre ListeProduitRecherche   
        ListeProduitRecherche = Frame(ListeProduit, bd=3, relief=RIDGE)
        ListeProduitRecherche.place(x=20, y=60, height=80,width=300)

        Label(ListeProduitRecherche, text="Recherche Produit",font=("Helvetica", 10, "bold"),fg="black").place(x=0, y=0)
        Label(ListeProduitRecherche, text="Nom :",font=("Helvetica", 10, "bold"),fg="black").place(x=0, y=30)
        Entry(ListeProduitRecherche,textvariable=self.var_recherche_text,font=("times new roman", 12, "bold"), bd=2).place(x=45, y=30, width=100)

        Button(ListeProduitRecherche, text="Recherche",command=self.recherche, font=("Helvetica",8, "bold"), bg="orange",fg="white",cursor="hand2").place(x=150,y=30,width=80)
                                                                                                    
        Button(ListeProduitRecherche, text="Tous", font=("Helvetica",8, "bold"), bg="lightgray",fg="white",cursor="hand2").place(x=233,y=30,width=50)
                                                                                                    
        # Tablau de produit
        
          # ListeFrame = tableau
        ListeFrame = Frame(ListeProduit, bd=3, relief=RIDGE)
        ListeFrame.place(x=0, y=150, height=190, width=350)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeTableau = ttk.Treeview(ListeFrame, columns=(
        "id", "categorie", "fournisseur", "nom", "prix", "quantite", "status"), yscrollcommand=scrolly.set,
                                         xscrollcommand=scrollx)
        scrollx.config(command=self.ListeTableau.xview)
        scrolly.config(command=self.ListeTableau.yview)
        self.ListeTableau.heading("id", text="id")
        self.ListeTableau.heading("categorie", text="Categorie")
        self.ListeTableau.heading("fournisseur", text="Fournisseur")
        self.ListeTableau.heading("nom", text="Nom")
        self.ListeTableau.heading("prix", text="Prix")
        self.ListeTableau.heading("quantite", text="Quantite")
        self.ListeTableau.heading("status", text="Status")

        self.ListeTableau.pack(fill=BOTH, expand=1)

        self.ListeTableau["show"] = "headings"
        self.ListeTableau.bind("<ButtonRelease-1>")
        self.afficher()

    
     
    
    def afficher(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            # on va tester si l'id existe
            cur.execute("select *from produit")
            rows = cur.fetchall()
            self.ListeTableau.delete(*self.ListeTableau.get_children())
            for row in rows:
                self.ListeTableau.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    
    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_recherche_text.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:

                cur.execute( "select * from produit where nom "  + " LIKE '%" + self.var_recherche_text.get() + "%'")
                #print(self.var_recherche_text.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeTableau.delete(*self.ListeTableau.get_children())
                    for row in rows:
                        self.ListeTableau.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun utilisateur a été trouvé ")


        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")



    def login(self):
        self.root.destroy()
        self.obj = os.system("python login.py")

              
if __name__ == '__main__':
    root = Tk()
    obj = Caisse(root)
    root.mainloop()
