from tkinter import*
import random

liste = ["Barcelona","Mand red","Real Madrid","Liverpool","Chelsea","City"]

def valider():
	score1 = random.randint(0,8)
	score2 = random.randint(0,8)

	entier1.set(score1)
	entier2.set(score2)

	if rsu1.get() > rsu2.get():	
		lbl = Label(sousCadreLeft1, text='Winners : '+equp1.get())
		lbl.grid(row=2,column=1,pady=20)
	elif rsu1.get() == rsu2.get():
		lbl = Label(sousCadreLeft1, text='Matchs Nul Pas de vainqueur')
		lbl.grid(row=2,column=1,pady=20)
	else:
		lbl = Label(sousCadreLeft1, text='Winners : '+equp2.get())
		lbl.grid(row=2,column=1,pady=20)

def equipe():
	equi1 = random.choice(liste)
	equi2 = random.choice(liste)

	eq1.set(equi1)
	eq2.set(equi2)

# def valider():
# 	if equp1.get() != "" and equp2.get() != "":
# 		lbl = Label(sousCadreLeft1, text='Winners : '+equp1.get())
# 		lbl.grid(row=2,column=1,pady=20)

def pronos():
	mylistBox.insert(END, equp1.get()+" "+rsu1.get() + '-'+rsu2.get()+' '+equp2.get())

def Commenter():
	mylistBox1.insert(END,entDroit.get())

1
root = Tk()
root.geometry("1000x600+5+20")
root.title("tPronos_plus")

#==================Definition des cadres==================

cadreTitre = Frame(root, width=1000, height=10, bd=4, relief='ridge')
cadreTitre.pack(side=TOP)

cadreRight = Frame(root, width=200, height=600, bd=4, relief='sunken')
cadreRight.pack(side=RIGHT)

cadreLeft = Frame(root, width=500, height=550, bd=4, relief='sunken')
cadreLeft.pack(side=LEFT)

#========================Sous cadre gauche Haut===================================
sousCadreLeft1 = Frame(cadreLeft, width=500, bd=4, height=200, relief='sunken')
sousCadreLeft1.pack(side=TOP)

#========================Cadre Droit====================================
Topsdroit = Frame(cadreRight,bg="white",relief=SUNKEN,bd=5,width=300,height=600)
Topsdroit.pack(side=TOP)

titreDroit=Label(Topsdroit,text='Pronositic',font='aria 15 bold',fg="steel blue",anchor=W)
titreDroit.place(x=50,y=20)

#listeBox
mylistBox=Listbox(Topsdroit,width=30,height=5,font=('times',13))
mylistBox.place(x=10,y=50)

mylistBox1=Listbox(Topsdroit,width=30,height=7,font=('times',13))
mylistBox1.place(x=10,y=250)

#AddEntry
labComment=Label(cadreRight,text="Laisser un commentaire",font='aria 10 bold')
labComment.place(x=5,y=480)

comment=StringVar()
entDroit=Entry(Topsdroit,textvariable=comment,width=70)
entDroit.place(x=5,y=500)

titreDroit2=Label(Topsdroit,text='Commentaire',font='aria 12 bold',fg="steel blue",anchor=W)
titreDroit2.place(x=10,y=200)

boutonComment=Button(cadreRight,text="Commenter",font=('aria 8 bold'),command=Commenter)
boutonComment.place(x=195,y=480)

#============================Text du titre=========================================
txtTitre = Label(cadreTitre, text="\t\tPronos_plus\t\t\t\t",fg="steel blue", font="Aria 20 bold")
txtTitre.grid(row=0,column=0)

#===========================Elements de gauche======================================
eq1 = StringVar()
equp1 = Entry(sousCadreLeft1, bd=8, textvariable=eq1, width=15)
equp1.grid(row=0,column=0,padx=15,pady=20)

entier1=IntVar()
entier2=IntVar()

rsu1 = Entry(sousCadreLeft1, bd=4, textvariable=entier1, width=5)
rsu1.grid(row=0, column=1)

rsu2 = Entry(sousCadreLeft1, bd=4, textvariable=entier2, width=5)
rsu2.grid(row=0, column=2, padx=20)


eq2 = StringVar()
equp2 = Entry(sousCadreLeft1, bd=8, textvariable=eq2, width=15)
equp2.grid(row=0, column=3, padx=15, pady=20)

# def Pronos():
# 	recup1=rsu1.get()
# 	# recup2=rsu2.get()
# 	lab.config(text='String'+str(recup1))

b1 = Button(sousCadreLeft1, text="Valider", command=valider, width=15, bd=2)
b1.grid(row=1, column=0, pady=15)

b2 = Button(sousCadreLeft1, text="Matchs", command=equipe, width=15, bd=2)
b2.grid(row=1, column=1, pady=15)
	
b3= Button(sousCadreLeft1, text="Pronos", command=pronos, width=15, bd=2)
b3.grid(row=1, column=2, pady=15)


#=========================Sous cadre gauche bas============================
sousCadreLeft2 = Frame(cadreLeft, width=500, bd=4, height=500, relief='ridge')
sousCadreLeft2.pack(side=BOTTOM)

content=Frame(sousCadreLeft2,width=500,height=400, bd=4)
content.grid(row=0,column=0)

photo=PhotoImage(file='pronosplus.png')
label=Label(content, image=photo,height=400) 
label.place(x=0,y=0)	

if __name__=='__main__':
	root.mainloop()