from tkinter import *
from PIL import Image, ImageTk #pip install pillow
import os
from tkinter import messagebox
import time
import sqlite3
import smtplib
import email_pass

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("850x630+250+10")
        self.root.minsize(620, 450)
        self.root.config(bg="#e4e8ff")
        self.root.title("Connexion")
        self.root.focus_force()

        self.code_envoie = ""

       
        login_frame = Frame(self.root, bd=3, relief=RIDGE)
        login_frame.place(x=250, y=150, height=300,width=300)

        Label(self.root, text="Bienvenu chez BNAB Shop", bg="white", font=("times new roman",14, "bold"), cursor="hand2",relief=RIDGE).pack(side=TOP,fill=X)
        title = Label(login_frame, text="Connexion", font=("times new roman", 12,"bold"), bg="#e4e8ff", fg="black",relief=RIDGE).pack(side=TOP, fill=X)
       

        lbl_id = Label(login_frame, text="ID-Employé:", font=("times new roman",12,"bold")).place(x=90,y=40)
        lbl_id = Label(login_frame, text="Mot de passe :", font=("times new roman",12,"bold")).place(x=50, y=105,width=200)

        self.txt_id_employe = Entry(login_frame, font=("times new roman", 12), bg="lightgray")
        self.txt_id_employe.place(x=50, y=70,width=200)


        self.txt_password = Entry(login_frame,show='*' ,font=("times new roman",12), bg="lightgray")
        self.txt_password.place(x=50, y=150,width=200)

        connecter_btn = Button(login_frame, text="Connexion",command=self.connexion, cursor="hand2", font=("times new roman",12, "bold"), bg="lightgray", fg="green").place(x=100, y=180)
        #activebackground="cyan"#
        obli_btn = Button(login_frame, text="Mot de passe oublié",command=self.passwor_oublie_fenetre ,cursor="hand2", font=("times new roman", 12),bd=0,fg="red").place(x=80, y=210)

    def passwor_oublie_fenetre(self):
        if self.txt_id_employe.get()=="":
            messagebox.showerror("Erreur","Veuillez saisir votre ID Employé")
        else:
            con = sqlite3.connect(database="services/data.db")
            cur = con.cursor()
            try:
                cur.execute("select mail from employe where id=?",(self.txt_id_employe.get(),))
                email = cur.fetchone()
                if email== None:
                    messagebox.showerror("Erreur","L'ID employé est invalide")
                else:
                    chk = self.envoie_mail(email[0])
                    if chk=="f":
                        messagebox.showerror("Erreur","Veillez verifier votre connexion")
                    else:
                        self.var_code = StringVar()
                        self.var_new_pass = StringVar()
                        self.var_conf_pass = StringVar()

                        self.root2 = Toplevel()
                        self.root2.title("Réinitialiser mot de passe")
                        self.root2.config(bg="white")
                        self.root2.geometry("400x400+500+100")
                        self.root2.focus_force()
                        #The grab_set () method also prevents users from interacting 
                        #with the main window. Summary Show additional windows by creating instances of the Toplevel class."""
                        self.root2.grab_set()

                        title = Label(self.root2, text="Mot de passe oublié", font=("algerian", 14, "bold"), bg="red").pack(side=TOP, fill=X)

                        ###Code
                        aff_code = Label(self.root2, text="Saisir le code reçu par mail", font=("times new roman", 12, "bold"), bg="white").place(x=70, y=50)
                        txt_reset = Entry(self.root2, textvariable=self.var_code, font=("times new roman", 12), bg="lightgray").place(x=70, y=100, width=200)
                        self.code_btn = Button(self.root2,command=self.code_valide ,text="Valider", cursor="hand2", font=("times new roman", 15, "bold"), bg="lightgray", fg="green")
                        self.code_btn.place(x=300, y=90)

                        ###nouveau mode de passe
                        nouveau_password = Label(self.root2, text="Nouveau Mot de passe", font=("times new roman", 12, "bold"), bg="white").place(x=70, y=150)
                        txt_new_pass = Entry(self.root2, font=("times new roman",15),textvariable=self.var_new_pass, bg="lightgray").place(x=70, y=200, width=250)

                         ###nouveau mode de passe
                        confirm_password = Label(self.root2, text="Confirme Mot de passe", font=("times new roman", 12, "bold"), bg="white").place(x=70, y=250)
                        txt_c_pass = Entry(self.root2, font=("times new roman",12),textvariable=self.var_conf_pass, bg="lightgray").place(x=70, y=300, width=250)


                        ###Modifier le mot de pass
                        self.changer_btn = Button(self.root2,text="Modifier", cursor="hand2", state=DISABLED, command=self.modifier, font=("times new roman",15,"bold"), bg="yellow")
                        self.changer_btn.place(x=160, y=350)


            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def connexion(self):
        con = sqlite3.connect(database="services/data.db")
        cur = con.cursor()
        try:
            if self.txt_id_employe.get()=="" or self.txt_password.get()=="":
                messagebox.showerror("Erreur","Veuillez donnez votre ID Employé et votre mot de passe")
            else:
                cur.execute("select type from employe where id =? AND password=?",(self.txt_id_employe.get(), self.txt_password.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror("Erreur","L'ID Employé/Mot de passe n'existe pas")
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python accueil.py")
                    else:
                        self.root.destroy()
                        os.system("python caisse.py")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def modifier(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Erreur","Veillez saisir votre mot de passe")
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Erreur","Le nouveau mot de passe et le confirme mot de passe doivent être identique")
        else:
            try:
                con = sqlite3.connect(database="services/data.db")
                cur = con.cursor()
                cur.execute("update employe set password=? where id=?", (self.var_new_pass.get(), self.txt_id_employe.get(),))
                con.commit()
                messagebox.showinfo("Succès", "Mot de passe modifié avec succès")
                self.root2.destroy()

            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
    # On va tester si le code envoyé est egale au code saisir  s'ils egaux on active self.changer_btn et desactive self.code_btn 
    def code_valide(self):
        
        if int(self.code_envoie)==int(self.var_code.get()):
            self.changer_btn.config(state=NORMAL)
            self.code_btn.config(state=DISABLED)
        else:
            messagebox.showerror("Erreur","Code Invalide")

    def envoie_mail(self, to_):
        s = smtplib.SMTP("smtp.gmail.com",587) # 587 represente le port
        s.starttls()
         # l'authentification on va utilise email_ et pass_ ses variable se trouve aussi dans le fichier email_pass.py et on les trouvent ds se mm fichier
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_, pass_)
        # Je vais transformer  int(time.strftime("%H%S%M")) et int(time.strftime("%d:%m:%Y ")) entière pour avoir un code d'envoie
        self.code_envoie = int(time.strftime("%H%S%M"))+int(time.strftime("%S"))

        subj = "Magasin Shop BNAB Code de reinitialisation"
        msg = f"Bonjour Monsieur/Madame\n\nVotre code de reinitialisation est : {self.code_envoie}\n\nMerci d'avoir utiliser notre service"
        msg = "Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_, to_, msg) # On va envoyer le mail 
        chk = s.ehlo() # EHLO ("Extended Hello") is the SMTP command the client uses to tell the server that it is an SMTP client ( HELO is the old SMTP protocol, while EHLO is the extended SMTP initialisation command).
       

        if chk[0]==250: # on si le mail est bien juste alors il est égale à 250 il retourne aussi 's' sinon il nous renvoie 'f'
            return 's'
        else:
            return 'f'

if __name__=="__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()