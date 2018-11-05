#prueba
from tkinter import *

from interfaces import *

sis = Tk()
sis.resizable(False,False)
sis.geometry("300x300")#300x350
sis.configure(bg = "white")
sis.title("Sistema de ventas")

miLogo=PhotoImage(file="Img/Logo2.gif")


ttk.Label(sis,image=miLogo).place(x=90,y=40)
ttk.Label(sis,text='       Bienvenido a OXXO!\nEliga su idioma de preferencia',font=("Comic Sans MS",12)).place(x=40,y=95)
ttk.Button(sis, text='English',command=gIEnglish).place(x=100,y=160)
ttk.Button(sis,text='Español',command=gISpanish).place(x=100,y=210)


sis.mainloop()
