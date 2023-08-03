
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import tempfile  # les fichiers
import sqlite3
import os  # elle nous permet de faire des actions au niveau du system


class Caisse:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x615+0+0")
        self.root.minsize(620, 450)
        self.root.config(bg="lightgray")
        self.root.focus_force()  # elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Caisse")

        # Declaration du panier

        
        self.cart_list = []
        self.ck_print = 0
        # Variable pour afficher les calcules ds l'entry
        self.var_Calulatrice = StringVar()
        self.var_produit_text_nom = StringVar()
        self.var_NomClient = StringVar()
        self.var_Contact = StringVar()

        self.icon_title = ImageTk.PhotoImage(file=r"C:dossier_images\logo.png")
        Label(self.root, text="Caisse Magasin", image=self.icon_title, font=("times new roman", 14, "bold"), fg="black",
              bg="#e4e8ff",
              anchor="w", padx=9, compound=LEFT).place(x=0, y=0, relwidth=75, height=95)

        Button(self.root, text="Déconnecter", command=self.login, font=("times new roman", 12, "bold"), bg="orange",
               fg="black", cursor="hand2").place(x=1100, y=20)

        Label(self.root, text="Bienvenu Chez BNAB \t\t Date: DD-MM-YYYY\t\t Heure: HH:MM:SS",
              font=("times new roman", 12, "bold"), bg="#454545", fg="white").place(x=0, y=100, relwidth=1, height=50)

        # Creation de la fénêtre produit
        ListeProduit = Frame(self.root, bd=3, relief=RIDGE, )
        ListeProduit.place(x=0, y=150, height=430, width=380)
        Label(ListeProduit, text="Tous les produits", font=("times new roman", 12, "bold"), bg="orange",
              fg="black").pack(side=TOP, fill=X)

        # creation de la fénêtre ListeProduitRecherche   
        ListeProduitRecherche = LabelFrame(ListeProduit, bd=3, relief=RIDGE, text="Recherche Produit", font=("times new roman", 12, "bold"))
                                          
        ListeProduitRecherche.place(x=30, y=40, height=70, width=300)

        Label(ListeProduitRecherche, text="Nom :", font=("times new roman", 10, "bold"), fg="black").place(x=0, y=10)
        Entry(ListeProduitRecherche, textvariable=self.var_produit_text_nom, font=("times new roman", 10, "bold"),  bd=2).place(x=45, y=10, width=100)
            

        Button(ListeProduitRecherche, text="Recherche", command=self.recherche, font=("times new roman", 8, "bold"),
               bg="orange", fg="black", cursor="hand2").place(x=150, y=10, width=80)

        Button(ListeProduitRecherche, command=self.afficher, text="Tous", font=("times new roman", 8, "bold"),
               bg="lightgray", fg="black", cursor="hand2").place(x=233, y=10, width=50)

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
        self.ListeTableau.heading("prix", text="Prix", anchor=W)
        self.ListeTableau.heading("quantite", text="Quantite", anchor=W)
        self.ListeTableau.heading("status", text="Status", anchor=W)

        # elle sert à diminue la taille d'une colonne en python     
        self.ListeTableau.column('id', minwidth=100, width=120, stretch=False)
        self.ListeTableau.column('nom', minwidth=100, width=120, stretch=False)
        self.ListeTableau.column('prix', minwidth=100, width=120, stretch=False)
        self.ListeTableau.column('status', minwidth=100, width=120, stretch=False)

        self.ListeTableau.pack(fill=BOTH, expand=1)

        self.ListeTableau["show"] = "headings"
        self.ListeTableau.bind("<ButtonRelease-1>", self.getProduit)
        self.afficher()

        Label(ListeProduit, text="Note :'Entrer 0 quantité pour retirer le produit du panier'",
              font=("times new roman", 10), fg="red").pack(side=BOTTOM, fill=X)

        # declaration de la fénêtre client

        ListeClient = Frame(self.root, bd=3, relief=RIDGE)
        ListeClient.place(x=370, y=150, height=350, width=560)
        Label(ListeClient, text="Liste des clients", font=("times new roman", 12, "bold"), bg="orange",
              fg="black").pack(side=TOP, fill=X)

        Button(ListeClient, text="Déconnecter", font=("times new roman", 12, "bold"), bg="orange", fg="black",
               cursor="hand2").place(x=6000, y=20)

        ListeClientRecherche = LabelFrame(ListeClient, bd=3, text="Recherche employé",
                                          font=("times new roman", 12, "bold"))
        ListeClientRecherche.place(x=40, y=40, heigh=65, width=410)

        Label(ListeClientRecherche, text="Nom :", font=("times new roman", 10, "bold"), fg="black").place(x=10, y=9, width=100)
                                                                                                         

        Entry(ListeClientRecherche,textvariable=self.var_NomClient, font=("times new roman", 10, "bold"), bg="white", fg="black", cursor="hand2").place( x=90, y=9, width=100)

           
        Label(ListeClientRecherche, text="Contact :", font=("times new roman", 10, "bold"), fg="black",
              cursor="hand2").place(x=165, y=9, width=100)

        Entry(ListeClientRecherche,textvariable=self.var_Contact, font=("times new roman", 10, "bold"), bg="white", fg="black", cursor="hand2").place(
            x=270, y=12, width=100)

        FenetreCalculatrice = Frame(ListeClient, bd=3, relief=RIDGE)
        FenetreCalculatrice.place(x=0, y=120, height=243, width=170)

        self.ECRAN = Entry(FenetreCalculatrice, textvariable=self.var_Calulatrice, width=24, bg="black", fg="white",
                           relief=SUNKEN, bd=5).place(x=3, y=8)

        # // Bouttons //
        self.B1 = Button(FenetreCalculatrice, text="1", width=3, height=2, bg="grey", command=lambda: self.get_input(1),
                         fg="white").place(x=3, y=40)  # Boutton 1
        self.B2 = Button(FenetreCalculatrice, text="2", width=3, height=2, bg="grey", command=lambda: self.get_input(2),
                         fg="white").place(x=40, y=40)  # Boutton 2
        self.B3 = Button(FenetreCalculatrice, text="3", width=3, height=2, bg="grey", command=lambda: self.get_input(3),
                         fg="white").place(x=80, y=40)  # Boutton 3
        self.B4 = Button(FenetreCalculatrice, text="4", width=3, height=2, bg="grey", command=lambda: self.get_input(4),
                         fg="white").place(x=3, y=90)  # Boutton 4
        self.B5 = Button(FenetreCalculatrice, text="5", width=3, height=2, bg="grey", command=lambda: self.get_input(5),
                         fg="white").place(x=40, y=90)  # Boutton 5
        self.B6 = Button(FenetreCalculatrice, text="6", width=3, height=2, bg="grey", command=lambda: self.get_input(6),
                         fg="white").place(x=80, y=90)  # Boutton 6
        self.B7 = Button(FenetreCalculatrice, text="7", width=3, height=2, bg="grey", command=lambda: self.get_input(7),
                         fg="white").place(x=3, y=140)  # Boutton 7
        self.B8 = Button(FenetreCalculatrice, text="8", width=3, height=2, bg="grey", command=lambda: self.get_input(8),
                         fg="white").place(x=40, y=140)  # Boutton 8
        self.B9 = Button(FenetreCalculatrice, text="9", width=3, height=2, bg="grey", command=lambda: self.get_input(9),
                         fg="white").place(x=80, y=140)  # Boutton 9
        self.BC = Button(FenetreCalculatrice, text="C", command=self.clear_input, width=3, height=2, bg="gold",
                         fg="red", relief=RIDGE).place(x=3, y=190)  # Boutton C (Clear)
        self.B0 = Button(FenetreCalculatrice, text="0", width=3, height=2, bg="grey", command=lambda: self.get_input(0),
                         fg="white").place(x=40, y=190)  # Boutton 0
        self.BF = Button(FenetreCalculatrice, text=".", width=3, height=2, command=lambda: self.get_input("."),
                         bg="grey", fg="white").place(x=80, y=190)  # Boutton = (égale)

        self.BP = Button(FenetreCalculatrice, text="+", width=4, height=2, bg="gold",
                         command=lambda: self.get_input("+"), fg="black", relief=GROOVE).place(x=120,
                                                                                               y=40)  # Boutton + (addition)
        self.BS = Button(FenetreCalculatrice, text="-", width=4, height=2, bg="gold", fg="black",
                         command=lambda: self.get_input("-"), relief=GROOVE).place(x=120,
                                                                                   y=80)  # Boutton - (soustacrtion)
        self.BD = Button(FenetreCalculatrice, text="/", width=4, height=2, bg="gold", fg="black",
                         command=lambda: self.get_input("/"), relief=GROOVE).place(x=120, y=120)  # Boutton / (division)
        self.BM = Button(FenetreCalculatrice, text="X", width=4, height=2, bg="gold", fg="black",
                         command=lambda: self.get_input(" * "), relief=GROOVE).place(x=120,
                                                                                     y=160)  # Boutton X (multiplication)
        self.BE = Button(FenetreCalculatrice, text="=", width=4, height=1, bg="blue", fg="white",
                         command=self.resulat_input, relief=RIDGE).place(x=120, y=205)  # Button = (égale)

        # Deéclaration du panier
        FrameCart = Frame(self.root, bd=3, relief=RIDGE, bg="orange")
        FrameCart.place(x=544.05, y=270, height=30, width=325)

        self.ProduitTotalLabel=Label(FrameCart, text="Produit Total du panier: [0] ", font=("times new roman", 10, "bold"), bg="orange",  fg="black", cursor="hand2")
        self.ProduitTotalLabel.place(x=0, y=0)
            

        # Déclaration du  nombre de produit en stock
        self.LabelnombreStock = Label(FrameCart, text="En stock :", font=("times new roman", 10, "bold"), fg="black", bg="orange")
                                     
        self.LabelnombreStock.place(x=220, y=0)

        ListeFrameClient = Frame(ListeClient, bd=3, relief=RIDGE)
        ListeFrameClient.place(x=170, y=145, height=215, width=325)

        scrolly = Scrollbar(ListeFrameClient, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx = Scrollbar(ListeFrameClient, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.ListeTableauClient = ttk.Treeview(ListeFrameClient, columns=(
            "id", "nom", "prix", "quantite", "stock"), yscrollcommand=scrolly.set,
                                               xscrollcommand=scrollx)
        scrollx.config(command=self.ListeTableauClient.xview)
        scrolly.config(command=self.ListeTableauClient.yview)
        self.ListeTableauClient.heading("id", text="id", anchor=W)
        self.ListeTableauClient.heading("nom", text="Nom", anchor=W)
        self.ListeTableauClient.heading("prix", text="Prix", anchor=W)
        self.ListeTableauClient.heading("quantite", text="Quantite", anchor=W)
        self.ListeTableauClient.heading("stock", text="Stock", anchor=W)
        self.ListeTableauClient.pack(fill=BOTH, expand=1)

        # elle sert à diminue la taille d'une colonne en python     
        self.ListeTableauClient.column('id', minwidth=100, width=120, stretch=False)
        self.ListeTableauClient.column('nom', minwidth=100, width=120, stretch=False)
        self.ListeTableauClient.column('prix', minwidth=100, width=120, stretch=False)
        self.ListeTableauClient.column('stock', minwidth=100, width=120, stretch=False)


        self.ListeTableauClient["show"] = "headings"
        self.ListeTableauClient.bind("<ButtonRelease-1>",self.getTableauClient)
       
        # Formulaire sous de produit en bas du tableau

        FrameProduitCart = Frame(self.root, bd=3, relief=RIDGE, bg="orange")
        FrameProduitCart.place(x=370, y=515, height=65, width=500)
 
        # self.var_recherche_texte = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_idProduit = StringVar()
        self.var_produit_nom = StringVar()
        self.var_produit_prix = StringVar()
        self.var_produit_quantite = StringVar()
        self.var_stock = StringVar()
        

        Label(FrameProduitCart, text="Nom :", font=("times new roman", 10, "bold"), fg="black", bg="orange").place(x=5,y=2)
                                                                                                                

        Entry(FrameProduitCart, font=("times new roman",8, "bold"), textvariable=self.var_produit_nom, bg="white",
              fg="black", cursor="hand2", state="readonly").place(x=5, y=20, width=80)

        Label(FrameProduitCart, text="prix du produit:", font=("times new roman", 10, "bold"), fg="black",
              bg="orange").place(x=100, y=2)

        Entry(FrameProduitCart, font=("times new roman", 8, "bold"), textvariable=self.var_produit_prix, bg="grey",
              fg="black", state="readonly", cursor="hand2").place(x=100, y=20, width=85)

        Label(FrameProduitCart, text="Quantite:", font=("times new roman", 10, "bold"), fg="black", bg="orange").place(
            x=200, y=2)

        Entry(FrameProduitCart, font=("times new roman", 8, "bold"), textvariable=self.var_produit_quantite,
              bg="#D3D3D3", fg="black", cursor="hand2").place(x=200, y=20, width=85)

        Button(FrameProduitCart, text="Réinitialiser", font=("times new roman", 10, "bold"), bg="grey", fg="black",
               cursor="hand2").place(x=290, y=15, width=80)

        Button(FrameProduitCart, text="Ajouter | Modifier",command=self.ajout_modifier, font=("times new roman", 10, "bold"), bg="yellow",
               fg="black", cursor="hand2").place(x=375, y=15, width=117)

        # Fénêtre facture

        FrameFacture = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        FrameFacture.place(x=868, y=150, height=300, width=404)

        Label(FrameFacture, text="Zone de facture du client", font=("times new roman", 12, "bold"), bg="orange",
              fg="black").pack(side=TOP, fill=X)

        FactureScrolly = Scrollbar(FrameFacture, orient=VERTICAL)
        FactureScrolly.pack(side=RIGHT, fill=Y)

        self.TextEspaceFacture = Text(FrameFacture, yscrollcommand=FactureScrolly.set)
        self.TextEspaceFacture.pack(fill=BOTH, expand=1)

        FactureScrolly.config(command=self.TextEspaceFacture.yview)

        FrameFacture1 = Frame(self.root, bd=3, relief=RIDGE, bg="orange")
        FrameFacture1.place(x=870, y=450, height=128, width=403)

        self.LabelFactureMontant = Label(FrameFacture1, text="Montant brute \n [0] :", font=("times new roman", 9, "bold"),fg="white", bg="blue")
        self.LabelFactureMontant.place(x=10, y=5, height=50, width=115)
                                  

        self.LabelRemise = Label(FrameFacture1, text="Rémise \n [0] :", font=("times new roman", 9, "bold"), fg="black", bg="red")
        self.LabelRemise.place(x=140, y=5, height=50, width=115)
                                

        self.LabelMontantApyer = Label(FrameFacture1, text="Montant net à payer \n [0] :",font=("times new roman", 9, "bold"), fg="black", bg="green")
        self.LabelMontantApyer.place(x=275, y=5,   height=50,  width=115) 
                                                                                                       
                                                                                                          

        self.Btn_reinitilialiser = Button(FrameFacture1, text="Réinitialiser", font=("times new roman", 10, "bold"),
                                          bg="grey", fg="black", cursor="hand2").place(x=15, y=80, width=80)

        self.Btn_imprimer = Button(FrameFacture1, text="Imprimer", font=("times new roman", 10, "bold"), bg="green",
                                   fg="black", cursor="hand2").place(x=158, y=80, width=80)

        self.Btn_generer = Button(FrameFacture1,command=self.genererFacture, text="Générer", font=("times new roman", 10, "bold"), bg="yellow",
                                  fg="black", cursor="hand2").place(x=290, y=80, width=80)

        Label(self.root,
              text="Développer par Arnaud Besse \t\t besseberenger@outlook.com \t\t +41 77 206 23 65\n\t\tCopyright 2023",
              font=("Helvetica", 10, "bold"), bg="#454545", fg="white").pack(side=BOTTOM, fill=X)

    def getProduit(self, ex):

        r = self.ListeTableau.focus()
        contenu = self.ListeTableau.item(r)  # ListeTableau est le premier tableau
        row = contenu["values"]
        # print(row)c
        self.var_idProduit.set(row[0]),
        self.var_produit_nom.set(row[1]),
        self.var_produit_prix.set(row[2]),
        self.LabelnombreStock.config(text=f"En stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_produit_quantite.set(1),
    
    # elle recupere les donnees du produit et mettre ds la table 2 elle va nous servit d'ajouer ou modifier voir fontion ajouter_modifier
    def getTableauClient(self, ex):

        r = self.ListeTableauClient.focus()
        contenu = self.ListeTableauClient.item(r)  # ListeTableau est le premier tableau
        row = contenu["values"]
        # print(row)c
        self.var_idProduit.set(row[0]),
        self.var_produit_nom.set(row[1]),
        self.var_produit_prix.set(row[2]),
        self.var_produit_quantite.set(row[3])
        self.var_stock.set(row[4])
        self.LabelnombreStock.config(text=f" en stock [{str(row[4])}]")
      


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
    
    def genererFacture(self):
         if self.var_NomClient.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")
         # On peut pas generer une facture avec le panier libre

         elif len(self.cart_list)==0:
                messagebox.showerror("Erreur", "Ajouter des produits dans le panier")
         else:
              self.FunctionHeader_Facture()
              self.FunctionBody_Facture()
              #self.FunctionFooter_Facture()
              
              # On va stocker notre fichier fr sert à formater e t w va permettre lonrsqu'on ajoute un contenu les autres puisse être effacer
              fp = open(fr"Factures\{str(self.facture)}.txt)", "w")
              # on va écrire dans le fichier
              fp.write(self.TextEspaceFacture.get("1.0",END))
              fp.close()
              messagebox.showinfo("Sauvegarder","Enregistrement/Génerer éffectuer avec succès")
              # ça veut on génèrer une fois la facture
              self.ck_print = 1
    # fonction body
    def FunctionBody_Facture(self):

        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            for row in self.cart_list:
                id =  row[0]
                nom = row[1]
                 # on veut faire la modification de la base de données on va faire stock-quantite saisir
                 # On avait deja  si stock < quantite saisir tout en haut
                quantite = int(row[4])-int(row[3])
                if int(row[4])==int(row[3]):
                    status = "Inactive"
                if int(row[4])!=int(row[3]):
                     status ="Active"
                prix = float(row[2])*float(row[3])
                prix = str(prix)

                self.TextEspaceFacture.insert(END,"\n "+nom+"\t\t\t"+row[3]+"\t\t"+prix)
                cur.execute(
                "update produit set  quantite=?, status=? where id=?",(
                quantite,
                status,
                id,
                     
                ))
                con.commit()
            con.close()
            self.afficher()
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    # FunctionHeader_Facture cette fonction nous sert à faire de l'entête de notre facture
    def FunctionHeader_Facture(self):
        # on va generer la facture en fonction de l'heure
        self.facture = int(time.strftime("%H%M%S"))+ int(time.strftime("%d%m%Y")) # On va convertir les heure minutes second jour mois années entier pour avoir le numero de la facture 
        factureEntre =f'''
 Magasin BNAB 
 Tel:+ 41 77 203 23 65 
 Chemin des écoliers 1,1350 Orbe
 {str("="*46 )}
 Nom Client : {self.var_NomClient.get()}
 Telephone : {self.var_Contact.get()}
 N° de facture :{self.facture}\t\t\tDate :{str(time.strftime("%d/%m/%Y"))}
 {str("="*46 )}
 Nom du produit:\t\t\tQuantité:\t\tPrix:
 {str("="*46  )}
        '''
        self.TextEspaceFacture.delete("1.0",END)
        self.TextEspaceFacture.insert("1.0",factureEntre)

    # Fontion du premier tableau
    def recherche(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()

        try:
            if self.var_produit_text_nom.get() == "":
                messagebox.showerror("Erreur", "Le champs est vide")

            else:

                # nous avons faire les recherche des produits qui sont active ça veut les produits que le client n'a pas encore achete
                cur.execute(
                    "select  id , nom, prix, quantite, status from produit where nom " + " LIKE '%" + self.var_produit_text_nom.get() + "%' and status='Active'")
                # print(self.var_produit_text_nom.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ListeTableau.delete(*self.ListeTableau.get_children())
                    for row in rows:
                        self.ListeTableau.insert("", END, values=row)
                else:
                    messagebox.showerror("Erreur", " Aucun résultat")

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")

    def ajout_modifier(self):
        if self.var_idProduit.get()=="":
            messagebox.showerror("Erreur", "Selectionnez un produit")
        elif self.var_produit_quantite.get()=="":
            messagebox.showerror("Erreur", "La quantité est obligatoire")
            # On va  si la quantité demande est superieur au stock 
        elif int(self.var_produit_quantite.get())>int(self.var_stock.get()):
            messagebox.showerror("Erreur", "La quantité demander n'est pas disponible")
        
        else:
           
            prix_cal = self.var_produit_prix.get()
            cart_donne = [self.var_idProduit.get(), self.var_produit_nom.get(),self.var_produit_prix.get(),self.var_produit_quantite.get(),self.var_stock.get()]
            

            #####update
            present = "non"
            index_=0
            for row in self.cart_list:
                if self.var_idProduit.get()==row[0]:
                    present = "oui"
                    break
                index_+=1
            if present=="oui":
                op=messagebox.askyesno("Confirme","Le produit est déja présent\nTu veux vraiment modifier | Supprimer de la liste", parent = self.root)
                if op==True:
                    if self.var_produit_quantite.get()=="0":
                        
    	                #numbers = [2, 3, 5] elle sert à supprimer l' élement indexé numbers.pop(2) ,print(numbers)=> 1,2,3
                        self.cart_list.pop(index_)
                    else:
                        #On va indexé la quantite de produit quand veut changer
                        self.cart_list[index_][3]=self.var_produit_quantite.get()

            else:
                self.cart_list.append(cart_donne)

            self.afficher_cart()
            self.facture_modifier()

    # Elle calcule les montants de factures

    def facture_modifier(self):
        self.montant_facture = 0 
        self.net_payer = 0
        self.remise = 0

        for row in self.cart_list:
            self.montant_facture = self.montant_facture+(float(row[2])*int(row[3]))

        self.remise= (self.montant_facture*5)/100
        self.net_payer = self.montant_facture - self.remise

        self.LabelFactureMontant.config(text=f"Montant brute \n [{str(self.montant_facture)}]")
        self.LabelMontantApyer.config(text=f"Montant net à payer \n [{str(self.net_payer)}]")
        self.LabelRemise.config(text=f"Remise est \n [{str(self.remise)}]")
        self.ProduitTotalLabel.config(text=f"Nombre produit [{str(len(self.cart_list))}]")
    # Elle affiche le panier
    def afficher_cart(self):
        try:
            # nous avons que les éléments qui nous interesse dans la table produit qui ont pour status active
            self.ListeTableauClient.delete(*self.ListeTableauClient.get_children())
            for row in self.cart_list:
                self.ListeTableauClient.insert("", END, values=row)
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")
    

    #def actureModifier(self):
            
    # Les fontion de la calculatrice
    def get_input(self, num):
        # elle sert a recupere la valeur
        xnum = self.var_Calulatrice.get() + str(num)
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
