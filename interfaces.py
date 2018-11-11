#================================================================Imports==============================================================#
from tkinter import *
from tkinter import ttk
from funciones_botones import *
#====================================================================================================================================#
#=======================================================Variables====================================================================#
list_Productos = ["nada","nada"]
#====================================================================================================================================#
#======================================================Funcion imprimir==============================================================#

#====================================================================================================================================#
#======================================================Funcion gISpanish=============================================================#
def gISpanish():
    root = Toplevel()
    root.title("Sistema de Ventas")
    root.geometry("600x600")
    root.resizable(False,False)

    miLogo=PhotoImage(file="Img/Logo2.gif")

    miLabel = ttk.Label(root,text = "CATEGORIAS", font = ("TIMES NEW ROMAN", 16))
    miLabel.grid(row=0,column=0,padx=20)   

    miBoton1 = ttk.Button(root, text = "Bebidas", width= 18,command =botones_bebidas_es)
    miBoton1.grid(row=1,column=0,padx=20,pady=5)

    miBoton2 = ttk.Button(root, text = "Abarrotes",width=18,command =botones_abarrotes_es)
    miBoton2.grid(row=2,column=0,padx=20)

    miBoton3 = ttk.Button(root, text = "Congelados",width=18,command =botones_congelados_es)
    miBoton3.grid(row=3,column=0,padx=20)

    miBoton4 = ttk.Button(root, text = "Comida Preparada",width=18,command =botones_comida_preparada_es)
    miBoton4.grid(row=4,column=0,padx=20)

    miBoton5 = ttk.Button(root, text = "Cuidado Personal",width=18,command =botones_cuidado_personal_es)
    miBoton5.grid(row=5,column=0,padx=20)

    txt = Text(root,width=50,heigh=35,wrap=WORD)
    txt.grid(row=0,column=1,rowspan=7,sticky=E)

    miBoton6 = ttk.Button(root, text = "Imprimir",width=15,command = quit)
    miBoton6.grid(row=6,column=0,padx=20)

    root.mainloop()
#========================================================================================================================#
#==================================================Funcion gIEnglish=====================================================#
def gIEnglish():
 

    root = Toplevel()
    root.title("Sales System")
    root.geometry("600x600")

    miLabel = ttk.Label(root,text = "CATEGORIES", font = ("TIMES NEW ROMAN", 16))
    miLabel.grid(row=0,column=0,padx=20)   

    miBoton1 = ttk.Button(root, text = "Drinks", width= 18,command =botones_bebidas_en)
    miBoton1.grid(row=1,column=0,padx=20,pady=5)

    miBoton2 = ttk.Button(root, text = "Groceries",width=18,command =botones_abarrotes_en)
    miBoton2.grid(row=2,column=0,padx=20)

    miBoton3 = ttk.Button(root, text = "Frozen Products",width=18,command =botones_congelados_en)
    miBoton3.grid(row=3,column=0,padx=20)

    miBoton4 = ttk.Button(root, text = "Ready to eat!",width=18,command =botones_comida_preparada_en)
    miBoton4.grid(row=4,column=0,padx=20)

    miBoton5 = ttk.Button(root, text = "Personal Care",width=18,command =botones_cuidado_personal_en)
    miBoton5.grid(row=5,column=0,padx=20)

    miBoton6 = ttk.Button(root, text = "Pay",width=15,command = quit)
    miBoton6.grid(row=6,column=0,padx=20)

    txt = Text(root,width=50,heigh=35,wrap=WORD)
    txt.grid(row=0,column=1,rowspan=7,sticky=E)

    root.mainloop() 
    #============================================================================================================================#