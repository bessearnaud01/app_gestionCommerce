from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Employe:

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x580+300+50")
        self.root.minsize(620, 450)
        self.root.config(bg="#D3D3D3")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Employé")
       

        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS employe(id text PRIMARY KEY, nom text, prenom text, sexe text, naissance text, mail text,password text, contact text, adhesion text, type text,adresse text, salaire text) ")
        con.commit()

        # declaration de nos variables
        self.var_recherche_type = StringVar()
        self.var_recherche_txt = StringVar()
        self.id_employe = StringVar()
        self.var_nom = StringVar()
        self.var_prenom = StringVar()
        self.var_sexe = StringVar()
        self.var_dateNaissance = StringVar()
        self.var_type = StringVar()
        self.var_dateAdhesion = StringVar()
        self.var_contact = StringVar()
        self.var_mail = StringVar()
        self.var_password = StringVar()
        self.var_salaire = StringVar()

        # frame recherche
        rech_frame = LabelFrame(self.root, text="Recherche employé", bd=2, relief=RIDGE,bg="#D3D3D3", font=("times new roman", 12, "bold"))
                               
        rech_frame.place(x=180, y=10, width=650, height=90)

        recherche_option = ttk.Combobox(rech_frame, textvariable=self.var_recherche_type,
                                        values=("prenom", "nom", "mail", "contact"),
                                        font=("times new roman", 10, "bold"), state="r", justify=CENTER)
        # recherche_option.set("Choix")
        recherche_option.current(0)
        recherche_option.place(x=10, y=10, width=150)
        # var_recherche_txt
        Entry(rech_frame, textvariable=self.var_recherche_txt, font=("times new roman", 10, "bold"), bd=2).place(x=178, y=10,width=180)

                                                                                                                
                                                                                                                 
        Button(rech_frame, text="Recherche", command=self.recherche, font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2").place(x=375, y=6)
              

        Button(rech_frame, text="tout", command=self.afficher, font=("Helvetica", 9, "bold"), bg="lightgray",  cursor="hand2").place(x=470, y=6, width=50)
             

        Label(self.root, text="Formulaire Employé",bg="#D3D3D3", font=("times new roman", 15, "bold"),cursor="hand2").place(x=0, y=120, width=900)
              

        Label(self.root, text="Id employé :",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(  x=150, y=200)
          

        self.txtId = Entry(self.root,textvariable=self.id_employe, font=("times new roman", 12, "bold"), bd=2)
        self.txtId.place(x=240, y=200, width=150)

        Label(self.root, text="Sexe :", font=("times new roman", 12, "bold"),bg="#D3D3D3", cursor="hand2").place(x=390, y=200)
       
        entreSexe = ttk.Combobox(self.root, textvariable=self.var_sexe, values=("Masculin", "Féminin"), font=("times new roman", 10, "bold"), state="r")
                                
       
        # entreSexe.set("Choix")
        entreSexe.current(0)
        entreSexe.place(x=450, y=200, width=150)
        Label(self.root, text="Prénom :",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=600, y=200)
                                                                                                                 

        Entry(self.root, textvariable=self.var_prenom,font=("times new roman", 12, "bold"), bd=2).place(x=670, y=200,  width=120)

                                                                                                       
        Label(self.root, text="Contact :",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=600, y=230)
          

        Entry(self.root, textvariable=self.var_contact, font=("times new roman", 12, "bold"), bd=2).place(x=670, y=230, width=120)

                                                                                                         
        # 2eme ligne de formulaire
        Label(self.root, text="Nom:",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=150,  y=230)
                                                                                                            

        Entry(self.root, textvariable=self.var_nom,font=("times new roman", 12, "bold"), bd=2).place(x=190, y=230,  width=200)
                                                                                                    

        Label(self.root, text="Date de naissance :",bg="#D3D3D3", font=("times new roman", 12, "bold"),cursor="hand2").place(x=390, y=230)
              

        Entry(self.root, textvariable=self.var_dateNaissance, font=("times new roman", 12, "bold"), bd=2).place(x=530, y=230, width=70)
                                                                                                               
                                                                                                               
        Label(self.root, text="Date d'adhésion :",bg="#D3D3D3", font=("times new roman", 12, "bold"),cursor="hand2").place(x=600, y=260)
              
        Entry(self.root, textvariable=self.var_dateAdhesion, font=("times new roman", 12, "bold"), bd=2).place(x=730, width=60,y=260,)
                                                                                                           
                                                                                                              

        # line 3
        Label(self.root, text="Mail:",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=150,  y=260)
                                                                                                             

        Entry(self.root, textvariable=self.var_mail, font=("times new roman", 12, "bold"), bd=2).place(x=190, y=260, width=200)
                                                                                                      

        # Line 4
        Label(self.root, text="Password:",bg="#D3D3D3", font=("times new roman", 12, "bold"),
              cursor="hand2").place(x=390, y=260)
        Entry(self.root, textvariable=self.var_password ,font=("times new roman", 12, "bold"), bd=2).place(x=460, y=260, width=140)

                                                                                                          
        Label(self.root, text="Type :",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=600,y=290)

                                                                                                             
    
       
        entreType = ttk.Combobox(self.root, textvariable=self.var_type, values=("Admin", "Employe"), font=("times new roman", 10, "bold"), state="r")                      
        entreType.current(0)
        entreType.place(x=650, y=290, width=140)

        Label(self.root, text="Adresse:",bg="#D3D3D3", font=("times new roman", 12, "bold"), cursor="hand2").place(x=150,  y=290)
                                                                                                                

        self.txt_adresse = Text(self.root, font=("times new roman", 12, "bold"), bd=2)
        self.txt_adresse.place(x=220, y=290, width=170, height=70)

        Label(self.root, text="Salaire:", font=("times new roman", 12, "bold"),bg="#D3D3D3", cursor="hand2").place(x=390,  y=290)
                                                                                                                

        Entry(self.root, textvariable=self.var_salaire, font=("times new roman", 12, "bold"), bd=2).place(x=460, y=290, width=140)
                                                                                                         

        self.btnAjouter = Button(self.root, text="Ajouter", command=self.ajouter, state="normal",font=("Helvetica", 9, "bold"), bg="green", cursor="hand2")
                               
        self.btnAjouter.place(x=400, y=330, width=70)

        self.btnModifier = Button(self.root, text="Modifier", state="disabled", command=self.modifier, font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")

                                
        self.btnModifier.place(x=500, y=330, width=70)

        self.btnReinstaller = Button(self.root, text="Réinstaller", command=self.reinstaliser, font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")
                                    

        self.btnReinstaller.place(x=600, y=330, width=70)

        self.btnSupprimer = Button(self.root, text="Supprimer", command=self.supprimer, state="disabled",font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")
                                   

        self.btnSupprimer.place(x=700, y=330, width=70)

        # ListeFrame = tableau
        ListeFrame = Frame(self.root, bd=3, relief=RIDGE)
        ListeFrame.place(x=0, y=400, height=150, relwidth=1)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.Listemploye = ttk.Treeview(ListeFrame,
                                        columns=(
                                            "id", "nom", "prenom", "sexe", "naissance", "mail", "password", "contact",

                                            "adhesion", "type", "adresse", "salaire"
                                        ), yscrollcommand=scrolly.set, xscrollcommand=scrollx)

        scrollx.config(command=self.Listemploye.xview)
        scrolly.config(command=self.Listemploye.yview)
        self.Listemploye.heading("id", text="id")
        self.Listemploye.heading("nom", text="Nom")
        self.Listemploye.heading("prenom", text="Prénom")
        self.Listemploye.heading("sexe", text="Sexe")
        self.Listemploye.heading("naissance", text="naissance")
        self.Listemploye.heading("mail", text="Mail")
        self.Listemploye.heading("password", text="Password")
        self.Listemploye.heading("contact", text="Contact")
        self.Listemploye.heading("adhesion", text="Adhésion")
        self.Listemploye.heading("adresse", text="Adresse")
        self.Listemploye.heading("type", text="Type")
        self.Listemploye.heading("salaire", text="salaire")

        self.Listemploye.pack(fill=BOTH, expand=1)

        self.Listemploye["show"] = "headings"
        self.Listemploye.bind("<ButtonRelease-1>", self.getEmploye)
        self.afficher()  # fonction afficher tout

    def ajouter(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.id_employe.get() == "" or self.var_password.get == "":
                messagebox.showerror("Erreur", "Veuillez saisir un id et un mot de pass")
            else:
                # on va tester si l'id existe
                cur.execute("select *from employe where id=?", (self.id_employe.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Erreur", "L'id de l'employé existe déja")
                else:
                    # si l'id n'existe pas
                    cur.execute(
                        "insert into employe(id , nom , prenom , sexe , naissance , mail, password, contact, adhesion, type,adresse, salaire) values(?,?,?,?,?,?,?,?,?,?,?,?)",
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

    def afficher(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            # on va tester si l'id existe
            cur.execute("select *from employe")
            rows = cur.fetchall()
            self.Listemploye.delete(*self.Listemploye.get_children())
            for row in rows:
                self.Listemploye.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def getEmploye(self, ex):

        self.btnAjouter.config(state="disabled")  # lorsqu'on sur le button ajout les autres boutton se deactive
        self.btnModifier.config(state="normal")
        self.btnSupprimer.config(state="normal")

        self.txtId.config(state="readonly")
        # on va se concentré sur la listemploye
        r = self.Listemploye.focus()
        contenu = self.Listemploye.item(r)
        row = contenu["values"]
        # print(row)
        self.id_employe.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_prenom.set(row[2]),
        self.var_sexe.set(row[3]),
        self.var_dateNaissance.set(row[4]),
        self.var_mail.set(row[5]),
        self.var_password.set(row[6]),
        self.var_contact.set(row[7]),
        self.var_dateAdhesion.set(row[8]),
        self.var_type.set(row[9]),
        self.txt_adresse.delete("1.0", END),
        self.txt_adresse.insert(END, row[10]),
        self.var_salaire.set(row[11])

    def modifier(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            data = (

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
                self.id_employe.get()
            )
            cur.execute(
                "update employe set nom=? , prenom=? , sexe=? , naissance=? , mail=?, password=?, contact=?, adhesion=?, type=?,adresse=?, salaire=? where id=?",
                data
            )
            # print(data) elle permet de printer les produit
            con.commit()
            self.afficher()
            messagebox.showinfo("Succès", "La modification a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def supprimer(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            op = messagebox.askyesno("Confirmer", "Voulez-vous vraiment supprimer ?")
            if op == True:
                cur.execute("delete from employe where id=?", (self.id_employe.get()))
                con.commit()
                self.afficher()
                messagebox.showinfo("Succès", "Suppression éffectué")
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    

    def reinstaliser(self):
        self.id_employe.set(""),
        self.var_nom.set(""),
        self.var_prenom.set(""),
        self.var_sexe.set(""),
        self.var_dateNaissance.set(""),
        self.var_mail.set(""),
        self.var_password.set(""),
        self.var_contact.set(""),
        self.var_type.set("administrateur")
        self.var_dateAdhesion.set(""),
        self.txt_adresse.delete("1.0", END),
        self.var_salaire.set(""),
        self.var_recherche_type.set("nom")

    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_recherche_txt.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:
 
                cur.execute( "select * from employe where " + self.var_recherche_type.get() + " LIKE '%" + self.var_recherche_txt.get() + "%'")
                #print(self.var_recherche_type.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Listemploye.delete(*self.Listemploye.get_children())

                    for row in rows:
                        self.Listemploye.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun utilisateur a été trouvé ")


        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Employe(root)
    root.mainloop()
