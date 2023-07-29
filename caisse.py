from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import tempfile # les fichiers
import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Caisse:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x620+20+20")
        self.root.minsize(620, 450)
        self.root.config(bg="lightgray")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Caisse")

        # Declaration du panier

        self.liste_carte = [] 
        self.ck_print = 0
        # Variable pour afficher les calcules ds l'entry
        self.var_Calulatrice =  StringVar()
        self.var_produit_text_nom = StringVar()
       

        self.icon_title = ImageTk.PhotoImage(file=r"C:dossier_images\logo.png")
        Label(self.root, text="Caisse Magasin", image=self.icon_title, font=("times new roman",14, "bold"),fg="black", bg="#e4e8ff",
              anchor="w", padx=9, compound=LEFT).place(x=0, y=0, relwidth= 75, height=95)
            
        Button(self.root, text="Déconnecter",command=self.login, font=("times new roman", 12, "bold"), bg="orange",fg="black",cursor="hand2").place(x= 1100,y=20)
                                                                                                              
        Label(self.root, text="Bienvenu Chez BNAB \t\t Date: DD-MM-YYYY\t\t Heure: HH:MM:SS",
              font=("times new roman", 12, "bold"), bg="#454545", fg="white").place(x=0, y=100, relwidth=1, height=50)
        
        # Creation de la fénêtre produit
        ListeProduit = Frame(self.root,bd=3, relief=RIDGE,)
        ListeProduit.place(x=0, y=150, height=430,width= 380)
        Label(ListeProduit, text="Tous les produits",font=("times new roman", 12, "bold"), bg="orange", fg="black").pack(side=TOP,fill=X)
        
       
        # creation de la fénêtre ListeProduitRecherche   
        ListeProduitRecherche = LabelFrame(ListeProduit, bd=3, relief=RIDGE,text="Recherche Produit",font=("times new roman", 12, "bold"))
        ListeProduitRecherche.place(x=30, y=40, height=70,width=300)

        Label(ListeProduitRecherche, text="Nom :",font=("times new roman", 10, "bold"),fg="black").place(x=0, y=10)
        Entry(ListeProduitRecherche,textvariable=self.var_produit_text_nom,font=("times new roman", 10 , "bold"), bd=2).place(x=45, y=10, width=100)

        Button(ListeProduitRecherche, text="Recherche",command=self.recherche, font=("times new roman",8, "bold"), bg="orange",fg="black",cursor="hand2").place(x=150,y=10,width=80)
                                                                                                    
        Button(ListeProduitRecherche,command=self.afficher, text="Tous", font=("times new roman",8, "bold"), bg="lightgray",fg="black",cursor="hand2").place(x=233,y=10,width=50)
                                                                                                    
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

        # elle sert à diminue la taille d'une colonne en python     
        self.ListeTableau.column('id', minwidth = 100, width = 120, stretch = False)
        self.ListeTableau.column('nom', minwidth = 100, width = 120, stretch = False)  
        self.ListeTableau.column('prix', minwidth = 100, width = 120, stretch = False)  
        self.ListeTableau.column('status', minwidth = 100, width = 120, stretch = False)  


        self.ListeTableau.pack(fill=BOTH, expand=1)

        self.ListeTableau["show"] = "headings"
        self.ListeTableau.bind("<ButtonRelease-1>")
        self.afficher()
       
        Label(ListeProduit, text="Note :'Entrer 0 quantité pour retirer le produit du panier'",font=("times new roman", 10),fg="red").pack(side=BOTTOM,fill=X)
    
        # declaration de la fénêtre client

        ListeClient = Frame(self.root, bd=3, relief=RIDGE)
        ListeClient.place(x=370, y=150, height=430,width=500)
        Label(ListeClient, text="Liste des clients",font=("times new roman", 12, "bold"), bg="orange", fg="black").pack(side=TOP,fill=X)
        

        Button(ListeClient, text="Déconnecter", font=("times new roman", 12, "bold"), bg="orange",fg="black",cursor="hand2").place(x=6000,y=20)

       
        
        ListeClientRecherche = LabelFrame(ListeClient, bd=3,text="Recherche employé", font=("times new roman", 12, "bold"))
        ListeClientRecherche.place(x=40, y=40, heigh=65,width=410)

        Label(ListeClientRecherche, text="Nom :",font=("times new roman", 10, "bold"),fg="black").place(x=10, y=9,width=100)
                                                                                                     
        Entry(ListeClientRecherche, font=("times new roman",10, "bold"), bg="white",fg="black",cursor="hand2").place(x=90,y=9,width=100)
        
        

        Label(ListeClientRecherche, text="Contact :", font=("times new roman",10, "bold"),fg="black",cursor="hand2").place(x=165,y=9,width=100)
                                                                                                    
        Entry(ListeClientRecherche, font=("times new roman",10, "bold"), bg="white",fg="black",cursor="hand2").place(x=270,y=12,width=100)
                                                                                                    
      
    
        FenetreCalculatrice = Frame(ListeClient, bd=3, relief=RIDGE)
        FenetreCalculatrice.place(x=0, y=120, height=243,width=170)
        

       
       
                
        self.ECRAN = Entry(FenetreCalculatrice, textvariable= self.var_Calulatrice,width=24, bg ="black", fg="white", relief=SUNKEN, bd=5).place(x=3, y=8)

        # // Bouttons //
        self.B1 = Button(FenetreCalculatrice, text="1", width=3, height=2, bg="grey",command=lambda:self.get_input(1),fg="white").place(x=3, y=40) # Boutton 1
        self.B2 = Button(FenetreCalculatrice, text="2", width=3, height=2, bg="grey",command=lambda:self.get_input(2), fg="white").place(x=40, y=40) # Boutton 2
        self.B3 = Button(FenetreCalculatrice, text="3", width=3, height=2, bg="grey",command=lambda:self.get_input(3) ,fg="white").place(x=80, y=40) # Boutton 3
        self.B4 = Button(FenetreCalculatrice, text="4", width=3, height=2, bg="grey",command=lambda:self.get_input(4), fg="white").place(x=3, y=90) # Boutton 4
        self.B5 = Button(FenetreCalculatrice, text="5", width=3, height=2, bg="grey",command=lambda:self.get_input(5), fg="white").place(x=40, y=90) # Boutton 5
        self.B6 = Button(FenetreCalculatrice, text="6", width=3, height=2, bg="grey",command=lambda:self.get_input(6), fg="white").place(x=80, y=90) # Boutton 6
        self.B7 = Button(FenetreCalculatrice, text="7", width=3, height=2, bg="grey",command=lambda:self.get_input(7) ,fg="white").place(x=3, y=140) # Boutton 7
        self.B8 = Button(FenetreCalculatrice, text="8", width=3, height=2, bg="grey",command=lambda:self.get_input(8), fg="white").place(x=40, y=140) # Boutton 8
        self.B9 = Button(FenetreCalculatrice, text="9", width=3, height=2, bg="grey",command=lambda:self.get_input(9), fg="white").place(x=80, y=140) # Boutton 9
        self.BC = Button(FenetreCalculatrice, text="C",command=self.clear_input, width=3, height=2, bg="gold", fg="red", relief=RIDGE).place(x=3, y=190) # Boutton C (Clear)
        self.B0 = Button(FenetreCalculatrice, text="0", width=3, height=2, bg="grey",command=lambda:self.get_input(0), fg="white").place(x=40, y=190) # Boutton 0
        self.BF = Button(FenetreCalculatrice, text=".", width=3, height=2,command=lambda:self.get_input("."), bg="grey", fg="white").place(x=80, y=190) # Boutton = (égale)

        self.BP = Button(FenetreCalculatrice, text="+", width=4, height=2, bg="gold", command=lambda:self.get_input("+"),fg="black", relief=GROOVE).place(x=120, y=40) # Boutton + (addition)
        self.BS = Button(FenetreCalculatrice, text="-", width=4, height=2, bg="gold", fg="black",command=lambda:self.get_input("-"), relief=GROOVE).place(x=120, y=80) # Boutton - (soustacrtion)
        self.BD = Button(FenetreCalculatrice, text="/", width=4, height=2, bg="gold", fg="black",command=lambda:self.get_input("/"), relief=GROOVE).place(x=120, y=120) # Boutton / (division)
        self.BM = Button(FenetreCalculatrice, text="X", width=4, height=2, bg="gold", fg="black",command=lambda:self.get_input(" * "), relief=GROOVE).place(x=120, y=160) # Boutton X (multiplication)
        self.BE = Button(FenetreCalculatrice, text="=", width=4, height=1, bg="blue", fg="white",command=self.resulat_input,relief=RIDGE).place(x=120, y=205) # Button = (égale)

        
    

      
        # Deéclaration du panier
        FrameCart = Frame(self.root, bd=3,relief=RIDGE,bg="orange")
        FrameCart.place(x=544.05, y= 270, height=30, width=325 )
        
        
        
        
        Label(FrameCart, text="Produit Total du panier: [0] ", font=("times new roman",10, "bold"),bg="orange",fg="black",cursor="hand2").place(x=0,y=0)

        
        # Déclaration du  nombre de produit en stock ici
        self.nombreStock=Label(FrameCart, text="En stock :",font=("times new roman", 10, "bold"),fg="black",bg="orange")
        self.nombreStock.place(x=220, y=0)




        ListeFrameClient = Frame(ListeClient, bd=3, relief=RIDGE)
        ListeFrameClient.place(x=170, y=145, height=215, width=325)



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

        # Formulaire sous de produit en bas du tableau

        FrameProduitCart = Frame(self.root, bd=3,relief=RIDGE,bg="orange")
        FrameProduitCart.place(x=370, y= 515, height=65, width=500 )
        
         #self.var_recherche_texte = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_idCategorie = StringVar()
        self.var_produit_nom = StringVar()
        self.var_produit_prix = StringVar()
        self.var_produit_quantite= StringVar()
        self.var_stock = StringVar()


        Label(FrameProduitCart, text="Nom :",font=("times new roman", 10, "bold"),fg="black",bg="orange").place(x=5, y=2)

        Entry(FrameProduitCart, font=("times new roman",10, "bold"),textvariable=self.var_produit_nom, bg="white",fg="black",cursor="hand2",state="readonly").place(x=5,y=20,width=80)

        Label(FrameProduitCart, text="prix du produit:",font=("times new roman", 10, "bold"),fg="black",bg="orange").place(x=100, y=2)

        Entry(FrameProduitCart, font=("times new roman",10, "bold"),textvariable=self.var_produit_prix,bg="grey",fg="black",state="readonly" ,cursor="hand2").place(x=100,y=20,width=85)


        Label(FrameProduitCart, text="Quantite:",font=("times new roman", 10, "bold"),fg="black",bg="orange").place(x=200, y=2)

        Entry(FrameProduitCart, font=("times new roman",10, "bold"),textvariable=self.var_produit_quantite, bg="#D3D3D3",fg="black",cursor="hand2").place(x=200,y=20,width=85)

        Button(FrameProduitCart,text="Réinitialiser",font=("times new roman",10, "bold") ,bg="grey",fg="black",cursor="hand2").place(x=290,y=15,width=80)

        Button(FrameProduitCart,text="Ajouter | Modifier",font=("times new roman",10, "bold") ,bg="yellow",fg="black",cursor="hand2").place(x=375,y=15,width=117)


        # Fénêtre facture


        FrameFacture = Frame(self.root, bd=3,relief=RIDGE, bg="white")
        FrameFacture.place(x=868, y=150, height=300, width=335 )

        Label(FrameFacture, text="Zone de facture du client",font=("times new roman", 12, "bold"), bg="orange", fg="black").pack(side=TOP,fill=X)
        
        FactureScrolly = Scrollbar(FrameFacture, orient=VERTICAL)
        FactureScrolly.pack(side=RIGHT, fill=Y)


        self.Txt_espace = Text(FrameFacture, yscrollcommand= FactureScrolly.set)
        self.Txt_espace.pack(fill=BOTH, expand=1)

        FactureScrolly.config(command=self.Txt_espace.yview)
        


        FrameFacture1 = Frame(self.root, bd=3,relief=RIDGE,bg="orange")
        FrameFacture1.place(x=870, y= 450, height=128, width=337 )


        self.LabelMontant=Label(FrameFacture1, text="Montant Facture \n [0] :",font=("times new roman", 9, "bold"),fg="white",bg="blue").place(x=10, y=5,height=50,width=95)

        self.LabelRemise =Label(FrameFacture1, text="Rémise \n [0] :",font=("times new roman", 9, "bold"),fg="black",bg="red").place(x=107, y=5,height=50,width=95)


        self.LabelMontantApyer = Label(FrameFacture1, text="Montant net à payer \n [0] :",font=("times new roman", 9, "bold"),fg="black",bg="green").place(x=209, y=5,height=50,width=115)



    
        self.Btn_reinitilialiser=Button(FrameFacture1,text="Réinitialiser",font=("times new roman",10, "bold") ,bg="grey",fg="black",cursor="hand2").place(x=15,y=80,width=80)

        self.Btn_imprimer = Button(FrameFacture1,text="Imprimer",font=("times new roman",10, "bold") ,bg="green",fg="black",cursor="hand2").place(x= 118,y=80,width=80)

        self.Btn_generer =Button(FrameFacture1,text="Générer",font=("times new roman",10, "bold") ,bg="yellow",fg="black",cursor="hand2").place(x=235,y=80,width=80)

      
        Label(self.root,
              text="Développer par Arnaud Besse \t\t besseberenger@outlook.com \t\t +41 77 206 23 65\n\t\tCopyright 2023",
              font=("Helvetica", 10, "bold"),bg="#454545", fg="white").pack(side=BOTTOM, fill=X)



    def afficher(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            # nous avons que les éléments qui nous interesse dans la table produit qui ont pour status active
            cur.execute("select id , nom, prix, quantite, status from produit where status='Active'")
            rows = cur.fetchall()
            self.ListeTableau.delete(*self.ListeTableau.get_children())
            for row in rows:
                self.ListeTableau.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    # Fontion du premier tableau
    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
      
        try:
            if self.var_produit_text_nom.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:

                # nous avons faire les recherche des produits qui sont active ça veut les produits que le client n'a pas encore achete
                cur.execute( "select  id , nom, prix, quantite, status from produit where nom "  + " LIKE '%" + self.var_produit_text_nom.get() + "%' and status='Active'")
                print(self.var_produit_text_nom.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeTableau.delete(*self.ListeTableau.get_children())
                    for row in rows:
                        self.ListeTableau.insert("", END, values=row)
                else:
                      messagebox.showerror("Erreur", " Aucun résultat")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    

    
    def get_input(self,num):
        # elle sert a recupere la valeur
        xnum = self.var_Calulatrice.get()+ str(num)
        # elle sert a modifier la valeur saisir
        self.var_Calulatrice.set(xnum)


    # cette fonction elle sert à nettoyer
    def clear_input(self):
        self.var_Calulatrice.set("")

    
    # La fonction eval() nous permet d’exécuter des chaînes de caractères en tant que instruction Python. Il accepte une chaîne de caractère et retourne un objet.
    def resulat_input(self):
        resulat = self.var_Calulatrice.get()
        self.var_Calulatrice.set(eval(resulat))

    # elle permet de recuperer les valeur de votre calulatrice
    def login(self):
        self.root.destroy()
        self.obj = os.system("python login.py")

              
if __name__ == '__main__':
    root = Tk()
    obj = Caisse(root)
    root.mainloop()
