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
        self.root.config(bg="lightgray")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Produit")

        self.var_recherche_type = StringVar()
        self.var_recherche_text = StringVar()
        self.var_nom = StringVar()
        self.var_categorie = StringVar()
        self.var_status = StringVar()
        self.var_fournisseur = StringVar()
        self.var_prix = StringVar()
        self.var_quantite = StringVar()
        self.var_idProduit = StringVar()

        #  Création de la table produit

        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS produit ( id INTEGER PRIMARY KEY AUTOINCREMENT, categorie text, fournisseur text, nom text, prix text, quantite text, status text)")
        con.commit()

        # Une autre maniere de recupere la liste des fournisseurs

        self.Liste_Fournisseur = []
        self.getListeFournisseur()

        Label(self.root, text="PRODUIT", font=("Helvetica", 14, "bold"), bg="#e4e8ff", fg="black").place(x=0, y=0,
                                                                                                         relwidth=1,
                                                                                                         height=50)
        # ListeFrame = tableau
        ProduitFrame = Frame(self.root, bd=3, relief=RIDGE)
        ProduitFrame.place(x=10, y=60, height=450, width=320)
        Label(ProduitFrame, text="Détail produit", font=("Helvetica", 11, "bold"), bg="#e4e8ff", fg="black").place(x=0,
                                                                                                                   y=0,
                                                                                                                   relwidth=1,
                                                                                                                   height=50)

        Label(ProduitFrame, text="Catégorie :", fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(
            x=10, y=90)
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute("select nom from categorie")
        categories = cur.fetchall()

        entreCategorie = ttk.Combobox(ProduitFrame, textvariable=self.var_categorie, values=categories,
                                      font=("times new roman", 10, "bold"), state="r")
        entreCategorie.set("Select")
        entreCategorie.place(x=120, y=90, width=140)

        Label(ProduitFrame, text="Fournisseur :", fg="black", font=("times new roman", 12, "bold"),
              cursor="hand2").place(x=10, y=120)
        entreFournisseur = ttk.Combobox(ProduitFrame, textvariable=self.var_fournisseur, values=self.Liste_Fournisseur,
                                        font=("times new roman", 10, "bold"), state="r")
        entreFournisseur.set("Select")
        entreFournisseur.place(x=120, y=120, width=140)

        Label(ProduitFrame, text="Nom :", fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,
                                                                                                                  y=150)
        Entry(ProduitFrame, textvariable=self.var_nom, font=("times new roman", 10, "bold"), bd=2).place(x=120, y=150,
                                                                                                         width=140)

        Label(ProduitFrame, text="Prix:", fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=10,
                                                                                                                  y=180)
        Entry(ProduitFrame, textvariable=self.var_prix, font=("times new roman", 10, "bold"), bd=2).place(x=120, y=180,
                                                                                                          width=140)

        Label(ProduitFrame, text="Quantité:", fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(
            x=10, y=210)
        Entry(ProduitFrame, textvariable=self.var_quantite, font=("times new roman", 10, "bold"), bd=2).place(x=120,
                                                                                                              y=210,
                                                                                                              width=140)

        Label(ProduitFrame, text="Status:", fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(
            x=10, y=240)
        entreStatus = ttk.Combobox(ProduitFrame, textvariable=self.var_status, values=("Activé", "Désactivé"),
                                   font=("times new roman", 10, "bold"), state="r")
        entreStatus.set("Select")
        entreStatus.place(x=120, y=240, width=140)

        self.btnAjouter = Button(ProduitFrame, command=self.ajouter, text="Ajouter", state="normal",
                                 font=("Helvetica", 9, "bold"), fg="white", bg="green", cursor="hand2")

        self.btnAjouter.place(x=10, y=300, width=70)

        self.btnModifier = Button(ProduitFrame, command=self.modifier, text="Modifier", state="disabled",
                                  font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")

        self.btnModifier.place(x=85, y=300, width=70)

        self.btnReinstaller = Button(ProduitFrame, command=self.reinstaliser, text="Réinstaller",
                                     font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")

        self.btnReinstaller.place(x=160.5, y=300, width=70)

        self.btnSupprimer = Button(ProduitFrame, command=self.supprimer, text="Supprimer", state="disabled",
                                   font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")

        self.btnSupprimer.place(x=239, y=300, width=70)

        # frame recherche
        rech_frame = LabelFrame(self.root, text="Recherche produit", bd=2, relief=RIDGE, bg="white",
                                font=("times new roman", 12, "bold"))

        rech_frame.place(x=335, y=65, width=560, height=90)

        recherche_option = ttk.Combobox(rech_frame, values=["categorie","fournisseur","nom"], textvariable=self.var_recherche_type,
                                        font=("times new roman", 10, "bold"), state="r", justify=CENTER)
        recherche_option.set("Select")
        recherche_option.place(x=10, y=10, width=150)
        # var_recherche_nom
        Entry(rech_frame, font=("times new roman", 10, "bold"), textvariable=self.var_recherche_text, bd=2).place(x=178,
                                                                                                                 y=10,
                                                                                                                 width=180)

        Button(rech_frame, command=self.recherche, text="Rechercher:", font=("Helvetica", 9, "bold"), fg="white",
               bg="blue", cursor="hand2").place(x=360, y=10, width=100)

        Button(rech_frame, text="Tout",command=self.afficher, font=("Helvetica", 9, "bold"), fg="black", bg="lightgrey",
               cursor="hand2").place(x=464, y=10, width=50)

        # ListeFrame = tableau
        ListeFrame = Frame(self.root, bd=3, relief=RIDGE)
        ListeFrame.place(x=340, y=160, height=350, width=550)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeProduit = ttk.Treeview(ListeFrame, columns=(
        "id", "categorie", "fournisseur", "nom", "prix", "quantite", "status"), yscrollcommand=scrolly.set,
                                         xscrollcommand=scrollx)
        scrollx.config(command=self.ListeProduit.xview)
        scrolly.config(command=self.ListeProduit.yview)
        self.ListeProduit.heading("id", text="id")
        self.ListeProduit.heading("categorie", text="Categorie")
        self.ListeProduit.heading("fournisseur", text="Fournisseur")
        self.ListeProduit.heading("nom", text="Nom")
        self.ListeProduit.heading("prix", text="Prix")
        self.ListeProduit.heading("quantite", text="Quantite")
        self.ListeProduit.heading("status", text="Status")

        self.ListeProduit.pack(fill=BOTH, expand=1)

        self.ListeProduit["show"] = "headings"
        self.ListeProduit.bind("<ButtonRelease-1>", self.getProduit)
        self.afficher()  # fonction afficher tout

    def supprimer(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            op = messagebox.askyesno("Confirmer", "Voulez-vous vraiment supprimer ?")
            if op == True:
                cur.execute("delete from produit where id=?", (self.var_idProduit.get()))
                con.commit()
                self.afficher()
                messagebox.showinfo("Succès", "Suppression éffectué")
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def modifier(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            data = (

                self.var_categorie.get(),
                self.var_fournisseur.get(),
                self.var_nom.get(),
                self.var_prix.get(),
                self.var_quantite.get(),
                self.var_status.get(),
                self.var_idProduit.get()

            )
            cur.execute(
                "update produit set categorie=?, fournisseur=?, nom=? , prix=?, quantite=?, status=? where id=?",
                data
            )
            # print(data)
            con.commit()
            self.afficher()
            self.reinstaliser()
            messagebox.showinfo("Succès", "La modification a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    # On recupere les données de fournisseur c'est une autre manière de récuperer les données d'une autre table
    def getListeFournisseur(self):
        self.Liste_Fournisseur.append("vide")
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:

            cur.execute("select nom from fournisseur")
            fournisseurs = cur.fetchall()
            # print(fournisseurs)

            if len(fournisseurs) > 0:
                del self.Liste_Fournisseur[:]
                ##self.Liste_Fournisseur.append("Select")
                for i in fournisseurs:
                    self.Liste_Fournisseur.append(i[0])


        except EXCEPTION as ex:

            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def ajouter(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_nom.get() == "" or self.var_prix.get == "" or self.var_status.get == "" or self.var_quantite.get == "":
                messagebox.showerror("Erreur", "Veuillez saisir dans les champs")
            else:

                # on va tester si le nom existe ou pas
                cur.execute("select *from produit where nom=?", (self.var_nom.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Erreur", "Le nom existe déja")
                else:
                    # si l'id n'existe pas
                    cur.execute(
                        "insert into produit(categorie, fournisseur, nom, prix, quantite, status) values(?,?,?,?,?,?)",
                        (

                            self.var_categorie.get(),
                            self.var_fournisseur.get(),
                            self.var_nom.get(),
                            self.var_prix.get(),
                            self.var_quantite.get(),
                            self.var_status.get(),

                        ))
                    con.commit()
                    self.afficher()
                    self.reinstaliser()
                    messagebox.showinfo("Succès", "L'ajout a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def afficher(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            # on va tester si l'id existe
            cur.execute("select *from produit")
            rows = cur.fetchall()
            self.ListeProduit.delete(*self.ListeProduit.get_children())
            for row in rows:
                self.ListeProduit.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def getProduit(self, ex):

        self.btnAjouter.config(state="disabled")  # lorsqu'on sur le button ajout les autres boutton se deactive
        self.btnModifier.config(state="normal")
        self.btnSupprimer.config(state="normal")

        r = self.ListeProduit.focus()
        contenu = self.ListeProduit.item(r)
        row = contenu["values"]
        # print(row)
        self.var_idProduit.set(row[0]),
        self.var_categorie.set(row[1])
        self.var_fournisseur.set(row[2]),
        self.var_nom.set(row[3]),
        self.var_prix.set(row[4]),
        self.var_quantite.set(row[5]),
        self.var_status.set(row[6]),

    def reinstaliser(self):
        self.var_idProduit.set(""),
        self.var_categorie.set("Select")
        self.var_fournisseur.set("Select"),
        self.var_nom.set(""),
        self.var_prix.set(""),
        self.var_quantite.set(""),
        self.var_status.set("Select"),

    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_recherche_text.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:

                cur.execute("select * from produit where " + self.var_recherche_type.get() +" LIKE '%" + self.var_recherche_text.get() + "%'")
                #print(self.var_recherche_text.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeProduit.delete(*self.ListeProduit.get_children())
                    for row in rows:
                        self.ListeProduit.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun utilisateur a été trouvé ")


        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Produit(root)
    root.mainloop()
