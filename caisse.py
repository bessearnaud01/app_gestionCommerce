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
        self.root.geometry("1200x580+20+20")
        self.root.minsize(620, 450)
        self.root.config(bg="lightgray")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Caisse")

        # Déclaration de variable
        self.var_idProduit = StringVar()
        self.var_recherche_text = StringVar()
        self.var_nom = StringVar()
        self.var_prix = StringVar()
        self.var_quantite = StringVar()
        self.var_status = StringVar()

        self.icon_title = ImageTk.PhotoImage(file=r"C:dossier_images\logo.png")
        Label(self.root, text="Caisse Magasin", image=self.icon_title, font=("Helvetica",14, "bold"),fg="orange", bg="#e4e8ff",
              anchor="w", padx=9, compound=LEFT).place(x=0, y=0, relwidth= 75, height=95)
            
        Button(self.root, text="Déconnecter",command=self.login, font=("Helvetica", 12, "bold"), bg="orange",fg="white",cursor="hand2").place(x= 1030,y=20)
                                                                                                              
        Label(self.root, text="Bienvenu Chez BNAB \t\t Date: DD-MM-YYYY\t\t Heure: HH:MM:SS",
              font=("Helvetica", 12, "bold"), bg="#454545", fg="white").place(x=0, y=100, relwidth=1, height=50)
        
        # Creation de la fénêtre produit
        ListeProduit = Frame(self.root, bd=3, relief=RIDGE)
        ListeProduit.place(x=0, y=150, height=430,width= 380)
        Label(ListeProduit, text="Tous les produits",font=("Helvetica", 12, "bold"), bg="orange", fg="white").place(x=0, y=0, relwidth=1, height=30)
        # creation de la fénêtre ListeProduitRecherche   
        ListeProduitRecherche = Frame(ListeProduit, bd=3, relief=RIDGE)
        ListeProduitRecherche.place(x=30, y=40, height=80,width=300)

        Label(ListeProduitRecherche, text="Recherche Produit",font=("Helvetica", 10, "bold"),fg="black").place(x=100, y=0)
        Label(ListeProduitRecherche, text="Nom :",font=("Helvetica", 10, "bold"),fg="black").place(x=0, y=30)
        Entry(ListeProduitRecherche,textvariable=self.var_recherche_text,font=("times new roman", 12, "bold"), bd=2).place(x=45, y=30, width=100)

        Button(ListeProduitRecherche, text="Recherche",command=self.recherche, font=("Helvetica",8, "bold"), bg="orange",fg="white",cursor="hand2").place(x=150,y=30,width=80)
                                                                                                    
        Button(ListeProduitRecherche, text="Tous", font=("Helvetica",8, "bold"), bg="lightgray",fg="white",cursor="hand2").place(x=233,y=30,width=50)
                                                                                                    
        # Tablau de produit
        
          # ListeFrame = tableau
        ListeFrame = Frame(ListeProduit, bd=3, relief=RIDGE)
        ListeFrame.place(x=10, y=120, height=235, width=350)

        scrolly = Scrollbar(ListeFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeTableau = ttk.Treeview(ListeFrame, columns=(
        "id", "nom", "prix", "quantite", "status"), yscrollcommand=scrolly.set,
                                         xscrollcommand=scrollx)
        scrollx.config(command=self.ListeTableau.xview)
        scrolly.config(command=self.ListeTableau.yview)
        self.ListeTableau.heading("id", text="id", anchor=W)
       
        self.ListeTableau.heading("nom", text="Nom", anchor=W)
        self.ListeTableau.heading("prix", text="Prix",anchor=W )
        self.ListeTableau.heading("quantite", text="Quantite", anchor=W)
        self.ListeTableau.heading("status", text="Status", anchor=W)

        self.ListeTableau.pack(fill=BOTH, expand=1)

        self.ListeTableau["show"] = "headings"
        self.ListeTableau.bind("<ButtonRelease-1>")
        self.afficher()
       
        Label(ListeProduit, text="Note :'Entrer 0 quantité pour retirer le produit du panier'",font=("Helvetica", 10),fg="red").pack(side=BOTTOM,fill=X)
    
        # declaration de la fénêtre client

        ListeClient = Frame(self.root, bd=3, relief=RIDGE)
        ListeClient.place(x=370, y=150, height=430,width=500)
        Label(ListeClient, text="Information du client",font=("Helvetica", 12, "bold"), bg="orange", fg="white").place(x=0, y=0, relwidth=1, height=30)

        Button(ListeClient, text="Déconnecter", font=("Helvetica", 12, "bold"), bg="orange",fg="white",cursor="hand2").place(x=6000,y=20)

       
        
        ListeClientRecherche = Frame(ListeClient, bd=3, relief=RIDGE)
        ListeClientRecherche.place(x=20, y=40, height=80,width=450)

        Label(ListeClientRecherche, text="Recherche client",font=("Helvetica", 10, "bold"),fg="black").place(x=170, y=0)
        Label(ListeClientRecherche, text="Nom :",font=("Helvetica", 10, "bold"),fg="black").place(x=40, y=30)
        Entry(ListeClientRecherche,textvariable=self.var_recherche_text,font=("times new roman", 12, "bold"), bd=2).place(x=100, y=30, width=100)

        Label(ListeClientRecherche, text="Contact :", font=("Helvetica",10, "bold"),fg="black",cursor="hand2").place(x=165,y=30,width=100)
                                                                                                    
        Entry(ListeClientRecherche, font=("Helvetica",10, "bold"), bg="white",fg="black",cursor="hand2").place(x=270,y=30,width=100)
                                                                                                    

    
        FenetreCalculatrice = Frame(ListeClient, bd=3, relief=RIDGE)
        FenetreCalculatrice.place(x=0, y=120, height=243,width=170)

                
        ECRAN = Entry(FenetreCalculatrice, width=24, bg ="black", fg="white", relief=SUNKEN, bd=5).place(x=3, y=8)

        # // Bouttons //
        B1 = Button(FenetreCalculatrice, text="1", width=3, height=2, bg="grey", fg="white").place(x=3, y=40) # Boutton 1
        B2 = Button(FenetreCalculatrice, text="2", width=3, height=2, bg="grey", fg="white").place(x=40, y=40) # Boutton 2
        B3 = Button(FenetreCalculatrice, text="3", width=3, height=2, bg="grey", fg="white").place(x=80, y=40) # Boutton 3
        B4 = Button(FenetreCalculatrice, text="4", width=3, height=2, bg="grey", fg="white").place(x=3, y=90) # Boutton 4
        B5 = Button(FenetreCalculatrice, text="5", width=3, height=2, bg="grey", fg="white").place(x=40, y=90) # Boutton 5
        B6 = Button(FenetreCalculatrice, text="6", width=3, height=2, bg="grey", fg="white").place(x=80, y=90) # Boutton 6
        B7 = Button(FenetreCalculatrice, text="7", width=3, height=2, bg="grey", fg="white").place(x=3, y=140) # Boutton 7
        B8 = Button(FenetreCalculatrice, text="8", width=3, height=2, bg="grey", fg="white").place(x=40, y=140) # Boutton 8
        B9 = Button(FenetreCalculatrice, text="9", width=3, height=2, bg="grey", fg="white").place(x=80, y=140) # Boutton 9
        BC = Button(FenetreCalculatrice, text="C", width=3, height=2, bg="gold", fg="red", relief=RIDGE).place(x=3, y=190) # Boutton C (Clear)
        B0 = Button(FenetreCalculatrice, text="0", width=3, height=2, bg="grey", fg="white").place(x=40, y=190) # Boutton 0
        BF = Button(FenetreCalculatrice, text=".", width=3, height=2, bg="grey", fg="white").place(x=80, y=190) # Boutton = (égale)

        BP = Button(FenetreCalculatrice, text="+", width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=120, y=40) # Boutton + (addition)
        BS = Button(FenetreCalculatrice, text="-", width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=120, y=80) # Boutton - (soustacrtion)
        BD = Button(FenetreCalculatrice, text="/", width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=120, y=120) # Boutton / (division)
        BM = Button(FenetreCalculatrice, text="X", width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=120, y=160) # Boutton X (multiplication)
        BE = Button(FenetreCalculatrice, text="=", width=4, height=1, bg="blue", fg="white", relief=RIDGE).place(x=120, y=205) # Button = (égale)

        
    

        ListeFrameClient = Frame(ListeClient, bd=3, relief=RIDGE)
        ListeFrameClient.place(x=170, y=120, height=243, width=320)

        scrolly = Scrollbar(ListeFrameClient, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrameClient, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        
        self.ListeTableauClient = ttk.Treeview(ListeFrameClient, columns=(
        "id", "nom", "prix", "quantite", "status"), yscrollcommand=scrolly.set,
                                         xscrollcommand=scrollx)
        scrollx.config(command=self.ListeTableauClient.xview)
        scrolly.config(command=self.ListeTableau.yview)
        self.ListeTableauClient.heading("id", text="id", anchor=W)
        self.ListeTableauClient.heading("nom", text="Nom", anchor=W)
        self.ListeTableauClient.heading("prix", text="Prix",anchor=W )
        self.ListeTableauClient.heading("quantite", text="Quantite", anchor=W)
        self.ListeTableauClient.heading("status", text="Status", anchor=W)
        self.ListeTableauClient.pack(fill=BOTH, expand=1)

        self.ListeTableauClient["show"] = "headings"
        self.ListeTableauClient.bind("<ButtonRelease-1>")




        ListeClientRecherche = Frame(ListeProduit, bd=3, relief=RIDGE)
        ListeClientRecherche.place(x=30, y=40, height=80,width=300)

        Label(ListeClientRecherche, text="Recherche Produit",font=("Helvetica", 10, "bold"),fg="black").place(x=100, y=0)
        Label(ListeClientRecherche, text="Nom :",font=("Helvetica", 10, "bold"),fg="black").place(x=0, y=30)
        Entry(ListeClientRecherche,textvariable=self.var_recherche_text,font=("times new roman", 12, "bold"), bd=2).place(x=45, y=30, width=100)

        Button(ListeClientRecherche, text="Recherche",command=self.recherche, font=("Helvetica",8, "bold"), bg="orange",fg="white",cursor="hand2").place(x=150,y=30,width=80)
                                                                                                    
        Button(ListeClientRecherche, text="Tous", font=("Helvetica",8, "bold"), bg="lightgray",fg="white",cursor="hand2").place(x=233,y=30,width=50)
                                                                                                    


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
