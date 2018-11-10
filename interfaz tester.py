#============================================================Imports===================================================================#
from tkinter import *
from interfaces import *
#======================================================================================================================================#

#============================================================Main class================================================================#
class main:

    def __init__(self,master):
        self.geometry("600x600")
        self.resizable(False,False)
        self.configure(bg = "white")
        self.title("Sistema de ventas")

        frame = Frame(master)
        frame.pack()

        miLogo=PhotoImage(file="Img/Logo2.gif")

        self.aviso = Label(frame,text="Bienvenido al Sistema de Ventas SuperMarket!")
        self.logo = Label(frame, image = miLogo).place(x=90,y=40)

        self.aviso2 = Label(frame,text='       Bienvenido a OXXO!\nEliga su idioma de preferencia',font=("Comic Sans MS",12)).place(x=40,y=95)
        self.botonEn = Button(frame, text='English',command=gIEnglish).place(x=100,y=160)
        self.botonEs = Button(frame,text='Español',command=gISpanish).place(x=100,y=210)

root = Tk()
a = main(root)
root.mainloop()
#=====================================================Fin de Main==========================================================================#
