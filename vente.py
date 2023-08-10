from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import os  # elle nous permet de faire des actions au niveau du system


class Vente:

    def __init__(self, root):
        self.root = root
       
        
        self.root.title("Ventes")
        self.root.geometry("900x580+200+50")
        self.root.minsize(620, 450)
        self.root.config(bg="#D3D3D3")
        self.root.focus_force()# elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("Vente")

        # Déclaration de variable
        self.var_numeroFacture = StringVar()
        self.listeFactures = []

        Label(self.root, text="CONSULTER LA FACTURE DES CLIENTS", bg="#e4e8ff", font=("times new roman",14, "bold"), cursor="hand2",relief=RIDGE).pack(side=TOP,fill=X)
        numeroFacture =Label(self.root, text="N° Facture :", bg="#D3D3D3", font=("times new roman",12, "bold"), cursor="hand2").place(x=50,y=52)
        Entry(self.root, textvariable=self.var_numeroFacture, font=("times new roman", 12, "bold"), bd=2).place(x=150, y=52,width=150)
        Button(self.root,command=self.recherche, text="Recherche",font=("times new roman", 9, "bold"), fg="black", bg="green", cursor="hand2").place(x=320, y=52,width=70)
        Button(self.root,command=self.clearAll, text="Réinitialiser",font=("times new roman", 9, "bold"), fg="black", bg="grey", cursor="hand2").place(x=400, y=52,width=70)

          # ListeFrame = tableau
        FrameVente = Frame(self.root, bd=3, relief=RIDGE)
        FrameVente.place(x=50, y=100, height=350,width=200)

        scrolly = Scrollbar(FrameVente, orient=VERTICAL)
        self.listeVentes = Listbox(FrameVente, font=("times new roman",8),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.listeVentes.yview)
        self.listeVentes.pack(fill=BOTH,expand=1)
        self.listeVentes.bind("<ButtonRelease-1>",self.getFacture)
        self.afficherFactures()
       

        # Espace facture
        FactureFrame = Frame(self.root, bd=3, relief=RIDGE)
        FactureFrame.place(x=260, y=100, height=350,width=300)
        
        Label(FactureFrame, text="La facture du client", bg="#e4e8ff", font=("times new roman",11, "bold"), cursor="hand2",relief=RIDGE).pack(side=TOP,fill=X)
        scrolly2 = Scrollbar(FactureFrame, orient=VERTICAL)
        self.EspaceFactureTxt = Text(FactureFrame, font=("times new roman",7, "bold"),yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.EspaceFactureTxt.yview)
        self.EspaceFactureTxt.pack(fill=BOTH,expand=1)

        # Affichage de l'image
        self.cat2 = Image.open(r"dossier_images\cat2.png")
        self.cat2 = self.cat2.resize((300,250),Image.LANCZOS)
        self.cat2 = ImageTk.PhotoImage(self.cat2)

        self.labelVente = Label(self.root, bd=7,relief=RAISED,image=self.cat2)
        self.labelVente.place(x=570, y=150)

     # On va afficher les factures

    def afficherFactures(self):
        del self.listeFactures[:]#On supprime le tableau
        self.listeVentes.delete(0,END) # On supprime la listeVentes
        for facture in os.listdir("Factures"):  # Factures est le dossier ou se trouve les factures
            if facture.split(".")[-1]=="txt": # ons
                #print(facture)
                self.listeVentes.insert(END,facture)
                self.listeFactures.append(facture.split(".")[0]) # ET après on ajoute le .

    # On va recupere les factures
    
    def getFacture(self,ev):
        index_ = self.listeVentes.curselection()
        nom_fichier = self.listeVentes.get(index_)
        fichier_ouvert =open(fr"Factures\{nom_fichier}","r")
        self.EspaceFactureTxt.delete("1.0",END)
        for facture in fichier_ouvert:
            self.EspaceFactureTxt.insert(END,facture)
        fichier_ouvert.close()
                             
    def clearAll(self):
        self.afficherFactures()
        self.EspaceFactureTxt.delete("1.0",END)
        self.var_numeroFacture.set("")

    def recherche(self) :
        if self.var_numeroFacture.get() =="":
            messagebox.showerror("Erreur","Veuillez saisir un numéro de facture")  
        else:
            # On va tester si la facture existe dans liste facture et les numeros de factures st uniques$
          
            if self.var_numeroFacture.get() in self.listeFactures :
                fichier_ouvert = open(fr"Factures\{self.var_numeroFacture.get()}.txt","r")
                

                self.EspaceFactureTxt.delete("1.0",END)

                for i in fichier_ouvert:
                    
                    self.EspaceFactureTxt.insert(END,i)
                     
                fichier_ouvert.close()
            else:
                messagebox.showerror("Erreur", "La facture n'existe pas")

            
                          
       


# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Vente(root)
    root.mainloop()
