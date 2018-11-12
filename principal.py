from tkinter import *
from tkinter import ttk
from botones_funciones import *
from otras_Funciones import *
from funciones_mysql import *

root = Tk()

class principal:
  
    def __init__(self,master): 
        
        self.frame = Frame(master,bg= 'sky blue',width=70,heigh=70) 
        self.frame.pack()

        self.miLogo = PhotoImage(file="Img/Logo2.gif")

        self.aviso = Label(self.frame,text="Bienvenido al Sistema de Ventas SuperMarket!",bg= 'sky blue',font=("Comic Sans MS",12))
        self.aviso.grid(row=0,column=0,pady=8)

        self.logo = Label(self.frame, image = self.miLogo)
        self.logo.grid(row=1,column=0) 

        self.aviso1= Label(self.frame,text='Bienvenido a EasyBuy!\nEliga su idioma de preferencia',bg= 'sky blue',font=("Comic Sans MS",12))
        self.aviso1.grid(row=2,column=0,pady=8)

        self.botonEn = Button(self.frame, text='English',width=15,heigh=5,command=quit)
        self.botonEn.grid(row=3,column=0,pady=8)

        self.botonEs = Button(self.frame,text='Español',width=15,heigh=5,command= lambda: self.interfaz_Es())
        self.botonEs.grid(row=4,column=0,pady=8)  

    def interfaz_Es(self):
        #============================================= Atributos ========================================================#
        carrito = []

        #================================================================================================================#
        root2 = Toplevel()
        root2.title("Sistema de Ventas")
        root2.geometry("1300x600")
        root2.config(relief="ridge",bd=10)
        root2.resizable(False,False)
        
        root2.configure(bg="pale turquoise")


        titulo_pagina = Label(root2,text = "CATEGORIAS",bg = "pale turquoise",font = ("Comic Sans MS", 16))
        titulo_pagina.grid(row=0,column=0,padx=20)

        text_espacio = Text(root2,width=78,heigh=32,wrap=WORD)
        text_espacio.grid(row=1,column=0,padx=10,rowspan=9,sticky=E)

        boton_Bebidas = Button(root2,text="BEBIDAS",width= 18,heigh=5,command=lambda: botones_bebidas_es(root2,carrito))
        boton_Bebidas.grid(row=1,column=12,padx=15)

        boton_Abarrotes = Button(root2,text="ABARROTES",width=18,heigh=5,command=lambda: botones_abarrotes_es(root2,carrito))
        boton_Abarrotes.grid(row=1,column=13,padx=15)

        boton_Congelados = Button(root2,text="CONGELADOS",width=18,heigh=5,command=lambda: botones_congelados_es(root2,carrito))
        boton_Congelados.grid(row=1,column=14,padx=15)

        boton_Comida_Preparada = Button(root2,text="COMIDA PREPARADA",width=18,heigh=5,command=lambda: botones_comida_preparada_es(root2,carrito))
        boton_Comida_Preparada.grid(row=2,column=12,padx=15)

        boton_Cuidado_Personal = Button(root2,text="CUIDADO PERSONAL",width=18,heigh=5,command=lambda: botones_cuidado_personal_es(root2,carrito))
        boton_Cuidado_Personal.grid(row=2,column=13,padx=15)

        boton_Imprimir_Carrito = Button(root2,text="Imprimir Carrito",width=18,heigh=3,command=lambda: funcion_imprimir(text_espacio,carrito))
        boton_Imprimir_Carrito.grid(row=5,column=13,padx=15)

        retornar_precio('Inka Kola 500 ml')

#========================================== Main =============================================================================#
root.resizable(False,False)
root.title("Sistema de Ventas")
root.configure(bg = "deep sky blue")
root.geometry("400x430")
root.config(relief="ridge",bd=15)
a = principal(root)
root.mainloop()
#=============================================================================================================================#