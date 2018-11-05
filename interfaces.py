from tkinter import *
from tkinter import ttk
from funciones_botones import *
def gISpanish():
    root = Tk()
    root.title("Sistema de Ventas")
    root.geometry("800x800")
    root.resizable(False,False)

    miLabel = ttk.Label(root, text = "Products", font = ("Arial", 19))
    miLabel.grid(row=0,column=1)

    miBoton1 = ttk.Button(root, text = "Bebidas",command =botones_bebidas_es)
    miBoton1.grid(row=2,column=1)

    miBoton2 = ttk.Button(root, text = "Abarrotes",command =botones_abarrotes_es)
    miBoton2.grid(row=2,column=2)

    miBoton3 = ttk.Button(root, text = "Congelados",command =botones_congelados_es)
    miBoton3.grid(row=3,column=1)

    miBoton4 = ttk.Button(root, text = "Comida Preparada",command =botones_comida_preparada_es)
    miBoton4.grid(row=3,column=2)

    miBoton5 = ttk.Button(root, text = "Cuidado Personal",command =botones_cuidado_personal_es)
    miBoton5.grid(row=4,column=1)

    miBoton6 = ttk.Button(root, text = "Pagar", command = quit)
    miBoton6.grid(row=4,column=2)

    
    root.mainloop()

def gIEnglish():
    root = Tk()
    root.title("Sales System")
    root.geometry("800x500")

    miLabel = ttk.Label(root, text = "Products", font = ("Arial", 19)).place(x = 40,y = 20)

    miBoton1 = ttk.Button(root, text = "Drinks",command =botones_bebidas_en).place(x=40, y=100)

    miBoton2 = ttk.Button(root, text = "Groceries",command =botones_abarrotes_en).place(x=40, y=180)

    miBoton3 = ttk.Button(root, text = "Frozen Food",command =botones_congelados_en).place(x=40, y=260)

    miBoton4 = ttk.Button(root, text = "Ready to take",command =botones_comida_preparada_en).place(x=40, y=340)

    miBoton5 = ttk.Button(root, text = "Personal Care",command =botones_cuidado_personal_en).place(x=40, y=420)

    miBoton6 = ttk.Button(root, text = "Pay", command = quit).place(x=520, y = 440)


    root.mainloop() 