#prueba
from tkinter import *
from tkinter import ttk

sis = Tk()
sis.resizable(True,True)
sis.geometry("300x350")
sis.configure(bg = "white")
sis.title("Sistema de ventas")


ttk.Label(sis,text='Bienvenido a Tambo!\nEliga su idioma de preferencia:').place(x=65,y=50)
ttk.Button(sis, text='English', command=quit).place(x=100,y=200)
ttk.Button(sis,text='Español',command=quit).place(x=100,y=150)








sis.mainloop()
