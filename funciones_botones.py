from tkinter import *
from tkinter import ttk

def botones_bebidas_es():
    beb = Tk()
    beb.title("Catalogo de Bebidas")
    beb.geometry("1000x400")
    beb.resizable(False,False)
    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text = "Inca Kola").place(x=50, y = 180)
    cocaboton = Button(beb, text = "Coca Kola").place(x = 150, y = 180)
    fantaboton = Button(beb, text = "Fanta").place(x= 300, y = 180) 
   
   
    beb.mainloop()






def botones_bebidas_en():
    beb = Tk()
    beb.title("Drinks Catalogue")
    beb.geometry("1000x400")
    beb.resizable(False,False)
    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text = "Inca Kola").place(x=50, y = 180)
   cocaboton = Button(beb, text = "Coca Kola").place(x = 150, y = 180)
    fantaboton = Button(beb, text = "Fanta").place(x= 300, y = 180)     
    
    
    beb.mainloop()
    

