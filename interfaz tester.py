#============================================================Imports===================================================================#
from tkinter import *
from interfaces import *
#======================================================================================================================================#
#============================================================GUI Main Part==============================================================#
root = Tk()
root.resizable(False,False)
root.configure(bg = "deep sky blue")
root.title("Sistema de ventas")
root.geometry("400x400")
root.config(relief="ridge",bd=15)


frame = Frame(root,width = 70,heigh = 20,bg="sky blue")
frame.grid(row=1,column=1)
frame.pack()

miLogo=PhotoImage(file="Img/Logo2.gif")

aviso = Label(frame,text="Bienvenido al Sistema de Ventas SuperMarket!",font=("Comic Sans MS",12))
aviso.grid(row=0,column=0,pady=8)

logo = Label(frame, image = miLogo)
logo.grid(row=1,column=0)

aviso1= Label(frame,text='Bienvenido a EasyBuy!\nEliga su idioma de preferencia',font=("Comic Sans MS",12))
aviso1.grid(row=2,column=0,pady=8)

botonEn = Button(frame, text='English',width=15,heigh=5,command=gIEnglish)
botonEn.grid(row=3,column=0,pady=8)

botonEs = Button(frame,text='Español',width=15,heigh=5,command=gISpanish)
botonEs.grid(row=4,column=0,pady=8)

root.mainloop()
#=====================================================Fin de Main==========================================================================#
