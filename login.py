from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import time
import os  # elle nous permet de faire des actions au niveau du system
import email_password # Elle represente la classe

import smtplib
from email.mime.text import MIMEText

class Login:

    def __init__(self, root):
        self.root = root
        self.root.geometry("850x630+250+10")
        self.root.minsize(620, 450)
        self.root.config(bg="#e4e8ff")
        self.root.focus_force()# elle permet de ne pas travailler sur autre fénêtre que elle
        self.root.title("connexion")
        
        self.code_envoie = ""

        Label(self.root, text="Bienvenu chez BNAB Shop", bg="#e4e8ff", font=("times new roman",14, "bold"), cursor="hand2",relief=RIDGE).pack(side=TOP,fill=X)
        LoginFrame = Frame(self.root, bd=3, relief=RIDGE)
        LoginFrame.place(x=250, y=150, height=300,width=300)
        Label(LoginFrame, text="Connexion...", bg="#e4e8ff", font=("times new roman",14, "bold"), cursor="hand2",relief=RIDGE).pack(side=TOP,fill=X)

        Label(LoginFrame, text="Id-Employé:", font=("times new roman",14, "bold"), cursor="hand2").place(x=100,y=40)
        self.idTxt=Entry(LoginFrame, font=("times new roman", 12, "bold"), bd=2)
        self.idTxt.place(x=50, y=70,width=200)

        Label(LoginFrame, text="Mot de passe:", font=("times new roman",14, "bold"), cursor="hand2").place(x=90,y=105)
        self.password=Entry(LoginFrame, font=("times new roman", 12, "bold"), show="*",bd=2)
        self.password.place(x=50, y=150,width=200)

        Button(LoginFrame,command=self.connexion, font=("times new roman", 13, "bold"),fg="white",bg="green",foreground="black", activebackground="green",text="Connexion..",bd=2).place(x=50, y=180,width=200)
        Button(LoginFrame,command=self.passwordOublieFenetre, font=("times new roman", 13, "bold"),fg="black",foreground="red", text="Mot de passe oublié..",bd=0).place(x=50, y=230,width=190)

    def code_valide(self):
        pass    
    # on va envoyer un mail au cas ou l'utilisateur à oublier son mot de passe
    def EnvoieMail(self,to_):

       s = smtplib.SMTP("stmp.gmail.com",587) # 587 represente le port
     
       # On va faire le transfert de couche
       s.starttls()
       email_ = email_password.email_ # email_password elle represente la classe email_password ou le fichier email_password.py
       password_ = email_password.password_
       # l'authentification on va utilise email_ et password_
       s.login(email_,password_)
       # Je vais transformer  int(time.strftime("%H%S%M")) et int(time.strftime("%d:%m:%Y ")) entière pour avoir un code d'envoie

       self.code_envoie = int(time.strftime("%H%S%M"))+int(time.strftime("%d:%m:%Y "))
       subj = "Shop BNAB code de Réinitialisation"
       msg = f"Bonjour Monsieur/Madame\n Votre code de réinitialisation est:{self.code_envoie}\n\n Merci d'avoir utiliser notre service"
       msg ="Subject:{}\n\n".format(subj,msg)
       s.sendmail(email_,to_,msg)
       # On va verifier
       chk = s.ehlo()
       # On verifier est:
       if chk[0] ==250:
           return's' # si le mail existe
       else:
           return'f' # si le mail n'existe pas
       
    # Fonction pour nous ouvrir une autre fénètre     
    
    def passwordOublieFenetre(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            cur.execute("select mail from employe where id=?",(self.idTxt.get(),))
            email = cur.fetchone()
            if email==None:
               messagebox.showerror("Erreur","Veuillez saisir correctement le formulaire")

            else:# elle sert à envoye le mail à l'utilisateur
                #chk = self.EnvoieMail(email[0])
                # Si le mail n'existe l'application va nous renvoyer un message
                chk=""
                if chk=="f":
                   messagebox("Erreur","Veuillez verifier votre connexion")
                else:
                    self.var_code = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_new_pass = StringVar()

                    self.root2 = Toplevel()
                    self.root2.title("Réinitialiser")
        
                    self.root2.geometry("400x400+500+100")
                    self.root2.focus_force()
                    #The grab_set () method also prevents users from interacting 
                    #with the main window. Summary Show additional windows by creating instances of the Toplevel class."""
                    self.root2.grab_set()
                    LabelTitre = Label(self.root2, text="Mot de passe oublié",fg="white", bg="red",relief=RIDGE, font=("times new roman", 14, "bold"), cursor="hand2").pack(side=TOP,fill=X)
                    # code
                    LabelCode = Label(self.root2, text="Saisir le code recu par mail",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=100,y=40)
                    txt_reset = Entry(self.root2,textvariable=self.var_code,fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=100,y=70,width=190)
                 
                    self.codeBtn=Button(self.root2, text="Valider",font=("Helvetica", 12, "bold"),fg="White",bg="green", cursor="hand2")
                    self.codeBtn.place(x=100,y=110,width=190)
                    Label(self.root2, text="Nouveau mot de passe",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=120,y=150)

                    self.txt_new_password = Entry(self.root2,fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=100,y=190,width=190)

                    Label(self.root2, text="Confirmation de mot de passe",fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=100,y=220)

                    self.txt_Confirmation_password = Entry(self.root2,fg="black", font=("times new roman", 12, "bold"), cursor="hand2").place(x=100,y=250,width=190)
                     
                    self.BtnConfirmation=Button(self.root2, text="Envoyer",font=("Helvetica", 12, "bold"),fg="White",bg="green", cursor="hand2").place(x=100,y=290,width=190)
                   
        except EXCEPTION as ex:
                   messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


    def connexion(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
          
            if self.idTxt.get()==""or self.password.get()=="":
               messagebox.showerror("Erreur","Veuillez saisir correctement le formulaire")

            else:
                cur.execute("select type from employe where id=? AND password=?",(self.idTxt.get(),self.password.get()))
                user = cur.fetchone()
                #print(user)
                # On va texter si l'utilisateur existe ou pas
                if user==None:
                    messagebox.showerror("Erreur","L'utilisateur n'existe pas")
                else:
                    if user[0]=="Admin": # On va tester si le type admin est existe
                       self.root.destroy()
                       os.system("python accueil.py")
                    else:
                        self.root.destroy()
                        os.system("python caisse.py")
        except EXCEPTION as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}")


   
        

# ss the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    obj = Login(root)
    root.mainloop()
