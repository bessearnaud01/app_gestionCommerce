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
        self.root.geometry("900x580+300+50")
        self.root.minsize(620, 450)
        self.root.config(bg="#D3D3D3")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Fournisseur")

        self.var_recherche_texte = StringVar()
        self.var_idfournisseur = StringVar()
        self.var_contact = StringVar()
        self.var_nom = StringVar()
        
        # Creation de la table fournisseurs 
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute( "CREATE TABLE IF NOT EXISTS fournisseur(id text PRIMARY KEY, nom text,contact text,description text) ")
        con.commit()

        rech_frame = LabelFrame(self.root, text="Recherche fournisseur", bd=2, relief=RIDGE,bg="white", font=("times new roman", 12, "bold"))
                               
        rech_frame.place(x=180, y=10, width=650, height=80)


        Label(rech_frame, text="Nom:", bg="white", font=("times new roman", 12, "bold"), cursor="hand2").place(x=190, y=10)
        Entry(rech_frame,bg="white",textvariable=self.var_recherche_texte, font=("times new roman", 12, "bold"), bd=2).place(x=250, y=10, width=150)
        

        Button(rech_frame,command=self.recherche, text="Rechercher:", font=("Helvetica", 9, "bold"),fg="white", bg="blue",cursor="hand2").place(x=410 , y=10, width=100)

        Button(rech_frame,command=self.afficher, text="Tout", font=("Helvetica", 9, "bold"),fg="black", bg="lightgrey",cursor="hand2").place(x= 520, y=10, width=50)
            
        Label(self.root, text="Formulaire Fournisseur", bg="#e4e8ff", font=("times new roman", 15, "bold"),cursor="hand2").place(x=0, y=100, relwidth=1)

        # Formulaire du fourniseur

        Label(self.root, text="Id fournisseur :", bg ="#D3D3D3",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=20, y=160)  
        self.id_Txtfournisseur=Entry(self.root,textvariable=self.var_idfournisseur, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2)
        self.id_Txtfournisseur.place(x=130, y=160, width=150)

        Label(self.root, text="Nom :", bg ="#D3D3D3",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=20, y=200) 
        Entry(self.root,textvariable=self.var_nom, font=("times new roman", 12, "bold"),bg="white", bd=2).place(x=130, y=200, width=150)

        
        Label(self.root, text="Contact :", bg ="#D3D3D3",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=20, y=230) 
        Entry(self.root,textvariable=self.var_contact, font=("times new roman", 12, "bold"),bg="white", bd=2).place(x=130, y=230, width=150)

        Label(self.root, text="description :", bg ="#D3D3D3",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=20, y=260) 
        self.txtDescription =Text(self.root, font=("times new roman", 12, "bold"),bg="#D3D3D3", bd=2)
        self.txtDescription.place(x=130, y=260, width=150,height=70)


        self.btnAjouter = Button(self.root,command=self.ajouter, text="Ajouter", state="normal",   font=("Helvetica", 9, "bold"),fg="white" ,bg="green", cursor="hand2")
                              
        self.btnAjouter.place(x=10, y=350, width=70)

        self.btnModifier = Button(self.root,command=self.modifier, text="Modifier", state="disabled", font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")

                                
        self.btnModifier.place(x=85, y=350, width=70)

        self.btnReinstaller = Button(self.root, command=self.reinstaliser,text="Réinstaller", font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")
                                    
        self.btnReinstaller.place(x=160.5, y=350, width=70)

        self.btnSupprimer = Button(self.root,command=self.supprimer, text="Supprimer", state="disabled",font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")
                                   
        self.btnSupprimer.place(x=239, y=350, width=70)


        # liste fourniseurs
        # ListeFrame = tableau
        ListeFrame = Frame(self.root, bd=3, relief=RIDGE)
        ListeFrame.place(x=300, y=150, height=180,width=600)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeFournisseurs = ttk.Treeview(ListeFrame,columns=( "id", "nom", "contact", "description" ), yscrollcommand=scrolly.set, xscrollcommand=scrollx)

        scrollx.config(command=self.ListeFournisseurs.xview)
        scrolly.config(command=self.ListeFournisseurs.yview)
        self.ListeFournisseurs.heading("id", text="id")
        self.ListeFournisseurs.heading("nom", text="Nom")
        self.ListeFournisseurs.heading("contact", text="Contact")
        self.ListeFournisseurs.heading("description", text="Description")
        self.ListeFournisseurs.pack(fill=BOTH, expand=1)

        self.ListeFournisseurs["show"] = "headings"
        self.ListeFournisseurs.bind("<ButtonRelease-1>",self.getFournisseur)
        self.afficher()  # fonction afficher tout


       
    def ajouter(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_idfournisseur.get() == "" or self.var_contact.get == "":
                messagebox.showerror("Erreur", "Veuillez saisir un id et un mot de pass")
            else:
                # on va tester si l'id existe
                cur.execute("select *from fournisseur where id=?", (self.var_idfournisseur.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Erreur", "L'id du fournisseur existe déja")
                else:
                    # si l'id n'existe pas
                    cur.execute(
                        "insert into fournisseur(id , nom , contact, description) values(?,?,?,?)",
                        (
                            self.var_idfournisseur.get(),
                            self.var_nom.get(),
                            self.var_contact.get(),
                            self.txtDescription.get("1.0", END),
    
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
            cur.execute("select *from fournisseur")
            rows = cur.fetchall()
            self.ListeFournisseurs.delete(*self.ListeFournisseurs.get_children())
            for row in rows:
                self.ListeFournisseurs.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}") 
     

    def getFournisseur(self, ex):

        self.btnAjouter.config(state="disabled")  # lorsqu'on sur le button ajout les autres boutton se deactive
        self.btnModifier.config(state="normal")
        self.btnSupprimer.config(state="normal")
        self.id_Txtfournisseur.config(state="readonly")
        # on va se concentré sur la listemploye
        r = self.ListeFournisseurs.focus()
        contenu = self.ListeFournisseurs.item(r)
        row = contenu["values"]
        # print(row)
        self.var_idfournisseur.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_contact.set(row[2]),
        self.txtDescription.delete("1.0", END),
        self.txtDescription.insert(END, row[3]),
    
    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_recherche_texte.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:
 
                cur.execute( "select * from fournisseur where nom "  + " LIKE '%" + self.var_recherche_texte.get() + "%'")
                #print(self.var_recherche_type.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeFournisseurs.delete(*self.ListeFournisseurs.get_children())

                    for row in rows:
                        self.ListeFournisseurs.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun utilisateur a été trouvé ")


        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    
    def supprimer(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            op = messagebox.askyesno("Confirmer", "Voulez-vous vraiment supprimer ?")
            if op == True:
                cur.execute("delete from fournisseur where id=?", (self.var_idfournisseur.get()))
                con.commit()
                self.afficher()
                messagebox.showinfo("Succès", "Suppression éffectué")
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
       
    
    def reinstaliser(self):
        self.var_idfournisseur.set(""),
        self.var_nom.set(""),
        self.var_contact.set(""),
        self.txtDescription.delete("1.0", END),

    

    def modifier(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            data = (

                self.var_nom.get(),
                self.var_contact.get(),
                self.txtDescription.get("1.0", END),
                self.var_idfournisseur.get()
            )
            cur.execute(
                "update fournisseur set nom=?, contact=?,description=?  where id=?",
                data
            )
            #print(data) 
            con.commit()
            self.afficher()
            messagebox.showinfo("Succès", "La modification a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


        rech_frame = LabelFrame(self.root, text="Recherche employé", bd=2, relief=RIDGE,bg="white", font=("times new roman", 12, "bold"))
                               
        rech_frame.place(x=180, y=10, width=650, height=90)

# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Fournisseur(root)
    root.mainloop()
