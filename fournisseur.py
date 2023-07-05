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
        self.root.geometry("1020x550+150+1")
        self.root.minsize(620, 450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Fournisseur")

        self.var_recherche_type = StringVar()
        self.id_fourninsseur = StringVar()
        self.var_contact = StringVar()
        self.var_prenom = StringVar()
        self.var_sexe = StringVar()
        # Creation de la table fournisseurs 
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute( "CREATE TABLE IF NOT EXISTS fournisseur(id text PRIMARY KEY, nom text,contact text,description text) ")
        con.commit()

        rech_frame = LabelFrame(self.root, text="Recherche fournisseur", bd=2, relief=RIDGE,bg="white", font=("times new roman", 12, "bold"))
                               
        rech_frame.place(x=180, y=10, width=650, height=80)


        Label(rech_frame, text="Id fournisseur:", bg="white", font=("times new roman", 12, "bold"), cursor="hand2").place(x=140, y=10)
        self.txtId = Entry(rech_frame,bg="lightyellow", font=("times new roman", 12, "bold"), bd=2)
        self.txtId.place(x=250, y=10, width=150)

        Button(rech_frame, text="Rechercher:", font=("Helvetica", 9, "bold"),fg="white", bg="blue",cursor="hand2").place(x=410 , y=10, width=100)

        Button(rech_frame, text="Tout", font=("Helvetica", 9, "bold"),fg="black", bg="lightgrey",cursor="hand2").place(x= 520, y=10, width=50)
            
        Label(self.root, text="Formulaire Fournisseur", bg="cyan", font=("times new roman", 15, "bold"),cursor="hand2").place(x=0, y=100, width=1020)

        # Formulaire du fourniseur

        Label(self.root, text="Id fournisseur :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=160)  
        self.id_fourninsseur=Entry(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=160, width=180)

        Label(self.root, text="Nom :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=200) 
        textNom=Entry(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=200, width=180)

        
        Label(self.root, text="Contact :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=230) 
        Entry(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=230, width=180)

        Label(self.root, text="description :", bg ="white",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place( x=50, y=260) 
        self.txtDesription=Text(self.root, font=("times new roman", 12, "bold"),bg="lightyellow", bd=2).place(x=170, y=260, width=180,height=70)


        self.btnAjouter = Button(self.root, text="Ajouter", state="normal",   font=("Helvetica", 9, "bold"), bg="green", cursor="hand2")
                              
        self.btnAjouter.place(x=40, y=350, width=70)

        self.btnModifier = Button(self.root, text="Modifier", state="disabled", font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")

                                
        self.btnModifier.place(x=120, y=350, width=70)

        self.btnReinstaller = Button(self.root, text="Réinstaller", font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")
                                    
        self.btnReinstaller.place(x=200, y=350, width=70)

        self.btnSupprimer = Button(self.root, text="Supprimer", state="disabled",font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")
                                   
        self.btnSupprimer.place(x=280, y=350, width=70)


        # liste fourniseurs
        # ListeFrame = tableau
        ListeFrame = Frame(self.root, bd=3, relief=RIDGE)
        ListeFrame.place(x=360, y=150, height=200,width=650)

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
        self.ListeFournisseurs.bind("<ButtonRelease-1>")
        #self.afficher()  # fonction afficher tout


       
    def ajouter(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.id_employe.get() == "" or self.var_password.get == "":
                messagebox.showerror("Erreur", "Veuillez saisir un id et un mot de pass")
            else:
                # on va tester si l'id existe
                cur.execute("select *from fournisseur where id=?", (self.id_employe.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Erreur", "L'id de l'employé existe déja")
                else:
                    # si l'id n'existe pas
                    cur.execute(
                        "insert into fournisseur(id , nom , contact, description) values(?,?,?,?)",
                        (
                            self.id_employe.get(),
                            self.var_nom.get(),
                            self.var_prenom.get(),
                            self.var_sexe.get(),
                            self.var_dateNaissance.get(),
                            self.var_mail.get(),
                            self.var_password.get(),
                            self.var_contact.get(),
                            self.var_dateAdhesion.get(),
                            self.var_type.get(),
                            self.txt_adresse.get("1.0", END),
                            self.var_salaire.get(),

                        ))
                    con.commit()
                    self.afficher()
                    self.reinstaliser()
                    messagebox.showinfo("Succès", "L'ajout a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

        
     

   



# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Fournisseur(root)
    root.mainloop()
