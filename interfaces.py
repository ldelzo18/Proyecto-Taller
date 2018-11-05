from tkinter import *
from tkinter import ttk
from funciones_botones import *
def gISpanish():
    root = Tk()
    root.title("Sistema de Ventas")
    root.geometry("800x500")
    root.resizable(False,False)

    logoDrink = PhotoImage(file="Drinks.gif")

    miBoton1 = ttk.Button(root, text = "Bebidas",command =botones_bebidas_es).place(x=40, y=100)

    iBoton2 = ttk.Button(root, text = "Abarrotes",command =botones_abarrotes_es).place(x=40, y=180)

    miBoton3 = ttk.Button(root, text = "Congelados",command =botones_congelados_es).place(x=40, y=260)

    miBoton4 = ttk.Button(root, text = "Comida Preparada",command =quit).place(x=40, y=340)

    miBoton5 = ttk.Button(root, text = "Cuidado Personal",command =quit).place(x=40, y=420)

    miBoton6 = ttk.Button(root, text = "Pagar", command = quit).place(x=520, y = 440)

  

    root.mainloop()

def gIEnglish():
    root = Tk()
    root.title("Sales System")
    root.geometry("1100x800")

    miLabel = ttk.Label(root, text = "Products", font = ("Arial", 19)).place(x = 40,y = 20)

    miBoton1 = ttk.Button(root, text = "Drinks",command =botones_bebidas_en).place(x=40, y=60)

    miBoton2 = ttk.Button(root, text = "Groceries",command =botones_abarrotes_en).place(x=40, y=100)

    miBoton3 = ttk.Button(root, text = "Frozen Food",command =botones_congelados_en).place(x=40, y=140)

    miBoton4 = ttk.Button(root, text = "Ready to take",command =quit).place(x=40, y=180)

    miBoton5 = ttk.Button(root, text = "Personal Care",command =quit).place(x=40, y=220)

    miBoton6 = ttk.Button(root, text = "Pay", command = quit).place(x=120, y = 300)

    miBoton7 = ttk.Button(root, text = "Add", command =quit).place(x=270, y = 300)

    root.mainloop() 