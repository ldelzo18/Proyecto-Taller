from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sistema de Ventas")
root.geometry("700x400")
miFrame = Frame(root,width = 900,height = 700)

miLabel = ttk.Label(root, text = "Productos", font = ("Arial", 19)).place(x = 40,y = 20)

miBoton1 = ttk.Button(root, text = "Bebidas",command =quit).place(x=40, y=60)

miBoton2 = ttk.Button(root, text = "Abarrotes",command =quit).place(x=40, y=100)

miBoton3 = ttk.Button(root, text = "Congelados",command =quit).place(x=40, y=140)

miBoton4 = ttk.Button(root, text = "Comida Preparada",command =quit).place(x=40, y=180)

miBoton5 = ttk.Button(root, text = "Cuidado Personal",command =quit).place(x=40, y=220)

miBoton6 = ttk.Button(root, text = "Pagar", command = quit).place(x=120, y = 300)

miBoton7 = ttk.Button(root, text = "Añadir", command =quit).place(x=270, y = 300)




root.mainloop()