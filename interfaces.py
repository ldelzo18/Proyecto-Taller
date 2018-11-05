from tkinter import *
from tkinter import ttk
from funciones_botones import *
def gISpanish():
    root = Tk()
    root.title("Sistema de Ventas")
    root.geometry("800x400")
    root.resizable(False,False)

<<<<<<< HEAD
    miLabel = ttk.Label(root, text = "CATEGORIAS", font = ("TIMES NEW ROMAN", 19))
    miLabel.grid(row=0,column=1,pady=5,padx=10)
=======
    miLabel = ttk.Label(root, text = "Productos", font = ("Arial", 19))
    miLabel.grid(row=0,column=1)
>>>>>>> e8eb0e29e1259278465f82b7469bfbce91de6a6e

    miBoton1 = ttk.Button(root, text = "Bebidas", width= 18,command =botones_bebidas_es)
    miBoton1.grid(row=2,column=1,pady=15,padx=10)

    miBoton2 = ttk.Button(root, text = "Abarrotes",width=18,command =botones_abarrotes_es)
    miBoton2.grid(row=4,column=1,pady=15,padx=10)

    miBoton3 = ttk.Button(root, text = "Congelados",width=18,command =botones_congelados_es)
    miBoton3.grid(row=6,column=1,pady=15,padx=10)

    miBoton4 = ttk.Button(root, text = "Comida Preparada",width=18,command =botones_comida_preparada_es)
    miBoton4.grid(row=8,column=1,pady=15,padx=10)

    miBoton5 = ttk.Button(root, text = "Cuidado Personal",width=18,command =botones_cuidado_personal_es)
    miBoton5.grid(row=10,column=1,pady=15,padx=10)

    miBoton6 = ttk.Button(root, text = "Pagar",width=15,command = quit)
    miBoton6.grid(row=12,column=5,pady=15,padx=10)

<<<<<<< HEAD
    #entry_salida = Entry(root,state=DISABLED,width=80).place(x=280,y=50)
=======
>>>>>>> e8eb0e29e1259278465f82b7469bfbce91de6a6e

    root.mainloop()

def gIEnglish():
    root = Tk()
    root.title("Sales System")
    root.geometry("800x400")

    miLabel = ttk.Label(root, text = "CATEGORIES", font = ("TIMES NEW ROMAN", 19))
    miLabel.grid(row=0,column=1,pady=5,padx=10)

    miBoton1 = ttk.Button(root, text = "Drinks", width= 18,command =botones_bebidas_es)
    miBoton1.grid(row=2,column=1,pady=15,padx=10)

    miBoton2 = ttk.Button(root, text = "Groceries",width=18,command =botones_abarrotes_es)
    miBoton2.grid(row=4,column=1,pady=15,padx=10)

    miBoton3 = ttk.Button(root, text = "Frozen Foods",width=18,command =botones_congelados_es)
    miBoton3.grid(row=6,column=1,pady=15,padx=10)

    miBoton4 = ttk.Button(root, text = "Ready to Take!",width=18,command =botones_comida_preparada_es)
    miBoton4.grid(row=8,column=1,pady=15,padx=10)

<<<<<<< HEAD
    miBoton5 = ttk.Button(root, text = "Personal care",width=18,command =quit)
    miBoton5.grid(row=10,column=1,pady=15,padx=10)
=======
    miBoton5 = ttk.Button(root, text = "Personal Care",command =botones_cuidado_personal_en).place(x=40, y=420)
>>>>>>> e8eb0e29e1259278465f82b7469bfbce91de6a6e

    miBoton6 = ttk.Button(root, text = "Pay",width=15,command = quit)
    miBoton6.grid(row=12,column=5,pady=15,padx=10)


    root.mainloop() 