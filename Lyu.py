from tkinter import *
from sqlite3 import *
import time
from datetime import date


class MonAppli(Frame):
    
    listeAmis=[]
    listeAmis2=[]

    def say_hi(self):
        self.hi = "Hello, everyone! I'm a wishlist."
        print(self.hi)

    def ajouter(self) :
        elem=(self.nom.get(),self.prenom.get(),self.jour.get(),self.mois.get(),self.cadeau.get())
        c.execute('insert into stocks values (?,?,?,?,?)',elem)
        conn.commit()
        c.execute ("select * from stocks")
        rep = c.fetchall()
        self.content = rep
        print (rep)

    def supprimer(self) :
        elem=(self.nom.get(),self.prenom.get())
        c.execute('delete from stocks where nom = ? and prenom = ? ',elem)
        conn.commit()
        c.execute ("select * from stocks")
        rep = c.fetchall()
        print (rep)

    def trier(self) :
        elem=(self.jour.get(),self.mois.get())
        c.execute('select * from stocks where jour = ? and mois = ? ',elem)
        triée = c.fetchall()
        print (triée)

    def ordre_commenceAu1(self) :
        c.execute('select * from stocks order by mois , jour')
        rep=c.fetchall()
        for elem in rep:
            self.listeAmis.append(elem)
        print (self.listeAmis)
     
    def ordre_commenceAuJour(self) :
        c.execute("select * from stocks where(mois = strftime('%m', 'now') and jour = strftime('%d', 'now'))")
        rep=c.fetchall()
        c.execute("select * from stocks where jour > strftime('%d', 'now') and mois = strftime('%m', 'now') order by jour")
        rep1=c.fetchall()
        c.execute("select * from stocks where jour < strftime('%d', 'now') and mois = strftime('%m', 'now') order by jour")
        rep2=c.fetchall()
        c.execute("select * from stocks where mois > strftime('%m', 'now') order by mois, jour")
        rep3=c.fetchall()
        c.execute("select * from stocks where mois < strftime('%m', 'now') order by mois, jour")
        rep4=c.fetchall()
        for elem in rep:
            self.listeAmis2.append(elem)
        for elem in rep1:
            self.listeAmis2.append(elem)
        for elem in rep3:
            self.listeAmis2.append(elem)
        for elem in rep4:
            self.listeAmis2.append(elem)
        for elem in rep2:
            self.listeAmis2.append(elem)
        print (self.listeAmis2)

    def afficher(self) :
        conn.commit()
        c.execute ("select * from stocks")
        rep = c.fetchall()
        print (rep)  

    def createWidgets(self):

        Label(root,text = "Nom : ").grid(row=0,column=0,sticky=W,pady=3,padx=3) 
        self.nom = Entry(root)
        self.nom.grid(row=0,column=1,sticky=EW,pady=3,padx=8)
    
        Label(root,text = "Prénom : ").grid(row=1,column=0,sticky=W,pady=3,padx=3)
        self.prenom = Entry(root)
        self.prenom.grid(row=1,column=1,sticky=EW,pady=3,padx=8)
        
        Label(root,text = "Jour de naissance : ").grid(row=2,column=0,sticky=W,pady=3,padx=3)
        self.jour = Entry(root)
        self.jour.grid(row=2,column=1,sticky=EW,pady=3,padx=8)
        
        Label(root,text = "Mois de naissance : ").grid(row=3,column=0,sticky=W,pady=3,padx=3)        
        self.mois = Entry(root)
        self.mois.grid(row=3,column=1,sticky=EW,pady=3,padx=8)

        Label(root,text = "Idées de cadeaux : ").grid(row=4,column=0,sticky=W,pady=3,padx=3)
        self.cadeau = Entry(root)
        self.cadeau.grid(row=4,column=1,sticky=EW,pady=3,padx=8)

#        Label(root,text = "Le Resultat : ").grid(row=8,column=0,sticky=W,pady=3,padx=3)
#        self.resultat = Text(root)
#        self.resultat.grid(row=8,column=1,sticky=W,pady=3,padx=3)
#        self.resultat.insert(1,content)

#        Label(root,text = "Le Listbox : ").grid(row=8,column=0,sticky=W,pady=3,padx=3)
#        self.txt = Listbox(root)
#        self.txt.grid(row=8,column=1,sticky=W,pady=3,padx=3)
#        txt.insert(0,"Hi, everyone. I'm a wishlist ! ")
#        self.txt.delete(0, END)
#        for ami in self.gbd.getListeAmis():
#        self.ajouter()
#        self.txt.insert(END,self.content)
        


        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=6,column=2,sticky=W,pady=3,padx=3)

        self.ajoute = Button(self)
        self.ajoute["text"] = "AJOUTER"
        self.ajoute["command"] = self.ajouter
        self.ajoute.grid(row=6,column=3,sticky=W,pady=3,padx=3)

        self.supprime = Button(self)
        self.supprime["text"] = "SUPPRIMEER"
        self.supprime["command"] = self.supprimer
        self.supprime.grid(row=6,column=4,sticky=W,pady=3,padx=3)

        self.trie = Button(self)
        self.trie["text"] = "TRIER"
        self.trie["command"] = self.trier
        self.trie.grid(row=6,column=5,sticky=W,pady=3,padx=3)

        ordre1 = Button(self)
        ordre1["text"] = "ORDRE COMMENCANT AU 1er JANVIER"
        ordre1["command"] = self.ordre_commenceAu1
        ordre1.grid(row=6,column=6,sticky=W,pady=3,padx=3)

        ordre2 = Button(self)
        ordre2["text"] = "ORDRE COMMENCANT A LA DATE DU JOUR"
        ordre2["command"] = self.ordre_commenceAuJour
        ordre2.grid(row=6,column=7,sticky=W,pady=3,padx=3)  

        self.affiche = Button(self)
        self.affiche["text"] = "AFFICHER"
        self.affiche["command"] = self.afficher
        self.affiche.grid(row=6,column=8,sticky=W,pady=3,padx=3)

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=6,column=9,sticky=W,pady=3,padx=3)

        self.grid()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()


conn = connect('./wishlist.db')
c = conn.cursor()
c.execute('''create table if not exists stocks(nom,prenom,Jour de naissance, Mois de naissance, Idées de cadeaux)''')


#Liste = [('Lyu','Yishuo','30','7','PS4'),('Labraimi','Hamza','20','2','Livres'),('Laforest','Frédérique','1','1','De bons élèves')]
#for t in Liste :
#    c.execute('insert into stocks values (?,?,?,?,?)',t)
#conn.commit()

root = Tk()
app = MonAppli(master=root)
app.master.title("Wishlist")
app.mainloop()


root.destroy()











