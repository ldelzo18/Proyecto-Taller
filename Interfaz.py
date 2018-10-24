from tkinter import *
from tkinter import ttk

sis = Tk()
sis.title("Sistema de ventas automatizado")
sis.resizable(True,True)
sis.geometry("800x500")
sis.configure(bg = "beige")


myButton1 = Button(sis, text="Finalizar Compra",width=20,command=quit)
myButton1.place(x=45, y=45)

ttk.Button(sis, text='Añadir al carrito', command=quit).pack(side=BOTTOM)
ttk.Label(sis, text='Producto: ').pack(side=LEFT)







sis.mainloop()
