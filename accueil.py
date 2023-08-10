from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import time
import os  # elle nous permet de faire des actions au niveau du system


class accueil:

    def __init__(self, root):
        self.root = root
        self.root.title("Accueil")
        self.root.geometry("1020x650+100+1")
        self.root.minsize(920, 650)
        self.icon_title = ImageTk.PhotoImage(
            file=r"dossier_images\logo.png")
        Label(self.root, text="Magasin BNAB", image=self.icon_title,fg="black", font=("times new roman", 15, "bold"), bg="#e4e8ff",
              anchor="w", padx=20, compound=LEFT).place(x=0, y=0, relwidth=100, height=100)

        Button(self.root, text="Déconnecter",command=self.login, font=("times new roman", 12, "bold"),fg="white" ,bg="orange", cursor="hand2").place(x=900,
                                                                                                                 y=20)

        self.LabelDate =Label(self.root, text="Bienvenu Chez BNAB \t\t Date: DD-MM-YYYY\t\t Heure: HH:MM:SS",
              font=("times new roman", 12, "bold"),bg="#454545",fg="white")
        self.LabelDate.place(x=0, y=100, relwidth=1, height=50)

        menu_frame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        menu_frame.place(x=0, y=149.9, width=200, height=450)
        self.image_menu = Image.open(r"dossier_images\menu.jpg")
        self.image_menu = self.image_menu.resize((200, 82), Image.LANCZOS)
        self.image_menu = ImageTk.PhotoImage(self.image_menu)
        self.Label_image_menu = Label(menu_frame, image=self.image_menu)
        self.Label_image_menu.pack(side=TOP, fill=X)

        self.iconeBarre = ImageTk.PhotoImage(file=r"dossier_images\side.png")
           

        Label(menu_frame, text="Bienvenu Chez BNAB", font=("times new roman", 10, "bold"), bg="orange", fg="white").pack(side=TOP, fill=X)
        
        
        btn_employe = Button(menu_frame, command=self.employe, text="Employés", image=self.iconeBarre, padx=10, anchor="w", compound=LEFT,   font=("times new roman",12, "bold"), bg="white", bd=5, cursor="hand2")
                            
                          
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_employe.pack(side=TOP, fill=X)

        btn_fournisseurs = Button(menu_frame, text="Fournisseurs",command=self.fournisseur, image=self.iconeBarre, padx=10, anchor="w",   compound=LEFT, font=("times new roman", 12, "bold"), bg="white", bd=5, cursor="hand2")
                               
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_fournisseurs.pack(side=TOP, fill=X)

        btn_categorie = Button(menu_frame, command=self.categorie, text="catégories", image=self.iconeBarre, padx=10, anchor="w", compound=LEFT,
                               font=("times new roman",12, "bold"), bg="white", bd=5, cursor="hand2", width=0.5)
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_categorie.pack(side=TOP, fill=X)

        btn_produit = Button(menu_frame, command=self.produit, text="Produits", image=self.iconeBarre, padx=10,anchor="w", compound=LEFT,
                             
                             font=("times new roman",12, "bold"), bg="white", bd=5, cursor="hand2")
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_produit.pack(side=TOP, fill=X)

        btn_Ventes = Button(menu_frame, command=self.vente, text="Ventes", image=self.iconeBarre, padx=10, anchor="w",
                            compound=LEFT, font=("times new roman",12, "bold"), bg="white", bd=5, cursor="hand2")       
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_Ventes.pack(side=TOP, fill=X)

        btn_Quitter = Button(menu_frame, text="Quitter", command=self.quitter, image=self.iconeBarre, padx=10,
                             anchor="w", compound=LEFT,font=("times new roman", 12, "bold"), bg="white", bd=5, cursor="hand2")
                             
        # anchor st utilisé pour definir ou le texte est postionné par rapport à un point de réference
        btn_Quitter.pack(side=TOP, fill=X)

        # tableau de bord
        self.total_employers = Label(self.root, text="Total Employé\n[0]", font=("times new roman", 12, "bold"),
                                     relief="raised", bg="green", bd=5, fg="white")
        self.total_employers.place(x=240, y=160, height=100, width=200)

        self.total_Fournisseurs = Label(self.root, text="Total Fournisseur\n[0]", font=("times new roman", 12, "bold"),
                                        relief="raised", bg="blue", bd=5, fg="white")
        self.total_Fournisseurs.place(x=790, y=160, height=100, width=200)

        self.total_produits = Label(self.root,text="Total produit\n[0]", font=("times new roman", 12, "bold"),
                                    relief="raised", bg="white", bd=5, fg="black")
        self.total_produits.place(x=510, y=280, height=100, width=200)

        self.total_vente = Label(self.root, text="Total vente\n[0]", font=("times new roman", 12, "bold"),
                                 relief="raised", bg="red", bd=5, fg="white")
        self.total_vente.place(x=240, y=400, height=100, width=200)

        self.total_categorie = Label(self.root, text="Total catégorie\n[0]", font=("times new roman", 12, "bold"),
                                     relief="raised", bg="orange", bd=5, fg="white")
        self.total_categorie.place(x=790, y=400, height=100, width=200)

        self.affichage() # des horaires les nombre de valeurs ds les tables

        Label(self.root,
              text="Développer par Arnaud Besse \t\t besseberenger@outlook.com \t\t +41 77 206 23 65\n\t\tCopyright 2023",
              font=("times new roman", 12, "bold"),bg="#454545", fg="white").pack(side=BOTTOM, fill=X)
        
    def affichage(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
          
 
                cur.execute( "select * from produit ")
                produits = cur.fetchall()
                self.total_produits.config(text=f"Total produit\n[{str(len(produits))}]")

                cur.execute( "select * from fournisseur ")
                fournisseurs = cur.fetchall()
                self.total_Fournisseurs.config(text=f"Total fournisseur\n[{str(len(fournisseurs))}]")
              
                cur.execute( "select * from categorie ")
                categories = cur.fetchall()
                self.total_categorie.config(text=f"Total categorie\n[{str(len(categories))}]")

                
                cur.execute( "select * from employe ")
                employes = cur.fetchall()
                self.total_employers.config(text=f"Total employe\n[{str(len(employes))}]")

                # On va calculer le nombre le nombre de fichiers qui existe ds notre dossier factures    
                nombreFactures = len(os.listdir("Factures"))

                self.total_vente.config(text=f"Total employe\n[{str(nombreFactures)}]")

                            # fonction la date et de l'heure
                heure = (time.strftime("%H:%M:%S"))
                date = (time.strftime("%d:%m:%Y "))
                self.LabelDate.config(text=f"Bienvenu Chez  BNAB \t\t Date : {str(date)}\t\t Heure : {heure}")
                self.LabelDate.after(200,self.affichage)


                        

        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


   
    def employe(self):
        self.obj = os.system("python employe.py")

    def categorie(self):
        self.obj = os.system("python categorie.py")

    def fournisseur(self):
         self.obj = os.system("python fournisseur.py")
       

    def vente(self):
        self.obj = os.system("python vente.py")

    def produit(self):
        self.obj = os.system("python produit.py")

    def quitter(self):
        self.root.destroy()

    def login(self):
        self.root.destroy()
        self.obj = os.system("python login.py")
       

    
    # Cette fonction permet d'aller sur la page register
    def window_register(self):
        self.window.destroy()
        self.obj = os.system("python login.py")
       
        


# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = accueil(root)
    root.mainloop()
