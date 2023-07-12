from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import time
import os  # elle nous permet de faire des actions au niveau du system


class categorie:

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x580+300+50")
        self.root.title("Catégorie")
        self.root.minsize(620, 450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle

        #self.var_recherche_texte = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_idCategorie = StringVar()
        self.var_nom = StringVar()

        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS categorie( id INTEGER PRIMARY KEY AUTOINCREMENT, nom text)")
        con.commit()
        
        Label(self.root, text="Gestion de Catégorie produit",  font=("Helvetica", 14, "bold"), bg="#e4e8ff", fg="black").place(x=0, y=0, relwidth=1, height=50)
         
          # 2eme ligne de formulaire
        Label(self.root, text=" Saisir Catégorie Produit:",bg="white", font=("times new roman", 12, "bold"), cursor="hand2").place(x=30,  y=70)
           
        Entry(self.root,bg="lightyellow",textvariable=self.var_nom ,font=("times new roman", 12, "bold"), bd=2).place(x=30, y=95,  width=200)
                                                                                                    


        Label(self.root, text=" Saisir Catégorie Produit:",bg="white", font=("times new roman", 12, "bold"), cursor="hand2").place(x=450,  y=70)
           
        Entry(self.root,bg="lightyellow",textvariable=self.var_recherche_txt,font=("times new roman", 12, "bold"), bd=2).place(x=450, y=95,  width=200)

        
        Button(self.root, text="Recherche", command=self.recherche,font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2").place(x=660, y=95)
        

        Button(self.root, text="tout",command=self.afficher, font=("Helvetica", 9, "bold"), bg="lightgray",  cursor="hand2").place(x=746, y=95, width=50)
        
        self.btnAjouter = Button(self.root, command=self.ajouter, text="Ajouter", state="normal",font=("Helvetica", 9, "bold"), bg="green", cursor="hand2")
                               
        self.btnAjouter.place(x=30, y=130, width=70)

        self.btnModifier = Button(self.root, text="Modifier",command=self.modifier, state="disabled", font=("Helvetica", 9, "bold"), fg="white", bg="blue", cursor="hand2")                    
        self.btnModifier.place(x=157, y=130, width=70)

        self.btnReinstaller = Button(self.root,text="Réinstaller",command=self.reinstaliser, font=("Helvetica", 9, "bold"), fg="black", bg="yellow", cursor="hand2")
                                    
        self.btnReinstaller.place(x=30, y=160, width=70)

        self.btnSupprimer = Button(self.root, text="Supprimer",command=self.supprimer, state="disabled",font=("Helvetica", 9, "bold"), fg="black", bg="red", cursor="hand2")
                                   
        self.btnSupprimer.place(x=157, y=160, width=70)


        self.cat1 = Image.open(r"dossier_images\cat1.png")
        self.cat1 = self.cat1.resize((300,250),Image.LANCZOS)
        self.cat1 = ImageTk.PhotoImage(self.cat1)

        self.labelCategorie = Label(self.root, bd=7,relief=RAISED,image=self.cat1)
        self.labelCategorie.place(x=10, y=200)
    

    
        # ListeFrame = tableau
        ListeFrame = Frame(self.root, bd=3, relief=RIDGE)
        ListeFrame.place(x=350, y=140, height=150,width=500)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeCategorie = ttk.Treeview(ListeFrame, columns=("id", "nom"), yscrollcommand=scrolly.set, xscrollcommand=scrollx)
                                                     
        scrollx.config(command=self.ListeCategorie.xview)
        scrolly.config(command=self.ListeCategorie.yview)
        self.ListeCategorie.heading("id", text="id")
        self.ListeCategorie.heading("nom", text="Nom")
        self.ListeCategorie.pack(fill=BOTH, expand=1)

        self.ListeCategorie["show"] = "headings"
        self.ListeCategorie.bind("<ButtonRelease-1>",self.getCategorie)
        self.afficher()  # fonction afficher tout

     
    def afficher(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            # on va tester si l'id existe
            cur.execute("select *from categorie")
            rows = cur.fetchall()
            self.ListeCategorie.delete(*self.ListeCategorie.get_children())
            for row in rows:
                self.ListeCategorie.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}") 

  
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    
    
    def modifier(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            data = (

                self.var_nom.get(),
                self.var_idCategorie.get()

            )
            cur.execute(
                "update categorie set nom=? where id=?",
                data
            )
            #print(data) 
            con.commit()
            self.afficher()
            messagebox.showinfo("Succès", "La modification a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

       
    def ajouter(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if  self.var_idCategorie.get == "":
                messagebox.showerror("Erreur", "Veuillez une categorie qui existe dans le tableau")
            else:
                # on va tester si le nom existe ou pas
                cur.execute("select *from categorie where nom=?", (self.var_nom.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Erreur", "Le nom existe déja")
                else:
                    # si l'id n'existe pas
                    cur.execute(
                        "insert into categorie(nom) values(?)",
                        (
                            self.var_nom.get(),
    
                        ))
                    con.commit()
                    self.afficher()
                    self.reinstaliser()
                    messagebox.showinfo("Succès", "L'ajout a été effectué avec succcess")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    
    def reinstaliser(self):
        self.var_idCategorie.set(""),
        self.var_nom.set(""),

    def getCategorie(self, ex):

        self.btnAjouter.config(state="disabled")  # lorsqu'on sur le button ajout les autres boutton se deactive
        self.btnModifier.config(state="normal")
        self.btnSupprimer.config(state="normal")

        #self.txtId.config(state="readonly")
        # on va se concentré sur la listemploye
        r = self.ListeCategorie.focus()
        contenu = self.ListeCategorie.item(r)
        row = contenu["values"]
        # print(row)
        self.var_idCategorie.set(row[0]),
        self.var_nom.set(row[1])

    
    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.var_recherche_txt.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:
                cur.execute("""select * from categorie where nom =?""", (self.var_recherche_txt.get(),))
                   
                #print(self.var_recherche_type.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeCategorie.delete(*self.ListeCategorie.get_children())

                    for row in rows:
                        self.ListeCategorie.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", "Aucun utilisateur a été trouvé ")


        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    

    def supprimer(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:

            if  self.var_nom.get == "":
                messagebox.showerror("Erreur", "Veuillez saisir le nom")
            else:
                # on va recupere l'id
                cur.execute("select *from categorie where id=?", (self.var_idCategorie.get(),))
                row = cur.fetchone()
                # s il n existe pas alors
                if row == None:
                    messagebox.showerror("Erreur", "L'id existe ou la categorie n'existe pas ")
                  
                else:
                    op = messagebox.askyesno("Confirmer", "Voulez-vous vraiment supprimer ?")
                    if op == True:
                        cur.execute("delete from categorie where id=?",(self.var_idCategorie.get()))
                        con.commit()
                        self.afficher()
                        self.reinstaliser()
                        messagebox.showinfo("Succès", "Suppression éffectué")
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")



    




# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = categorie(root)
    root.mainloop()
