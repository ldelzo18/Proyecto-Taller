from tkinter import *
from tkinter import ttk

sis = Tk()
sis.title("Sistema de ventas automatizado")
sis.resizable(True,True)
sis.geometry("800x500")
sis.configure(bg = "beige")
ttk.Button(sis, text='Finalizar Compra', command=quit).pack(side=BOTTOM)
ttk.Button(sis, text='Añadir al carrito', command=quit).pack(side=BOTTOM)
ttk.Label(sis, text='Producto: ').pack(side=LEFT)







sis.mainloop()
