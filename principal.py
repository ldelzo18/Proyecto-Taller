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

        self.aviso = Label(self.frame,text="Bienvenido al Sistema de Ventas EASYBUY!",bg= 'sky blue',font=("Comic Sans MS",12))
        self.aviso.grid(row=0,column=0,pady=8)

        self.logo = Label(self.frame, image = self.miLogo)
        self.logo.grid(row=1,column=0) 

        self.aviso1= Label(self.frame,text='Please choose your language preference\nEliga su idioma de preferencia',bg= 'sky blue',font=("Comic Sans MS",12))
        self.aviso1.grid(row=2,column=0,pady=8)

        self.botonEn = Button(self.frame, text='English',width=15,heigh=5,command=lambda: self.interfaz_In())
        self.botonEn.grid(row=3,column=0,pady=8)

        self.botonEs = Button(self.frame,text='Español',width=15,heigh=5,command= lambda: self.interfaz_Es())
        self.botonEs.grid(row=4,column=0,pady=8)  

    #Interfaz en español
    def interfaz_Es(self):
        #============================================= Carrito de compra ================================================#
        carrito = []
        #================================================================================================================#
        root2 = Toplevel()
        root2.title("Sistema de Ventas")
        root2.geometry("1400x600")
        root2.config(relief="ridge",bd=10)
        root2.resizable(False,False)
        root2.configure(bg="pale turquoise")

        logo = PhotoImage(file ="Img/python.gif")#Variable logo que hace referencia a python.gif en carpeta Img
        logo_usil = PhotoImage(file="Img/usil2.gif")#Variable logo_usil que hace referencia a usil2.gif en carpeta Img

        titulo_pagina = Label(root2,text = "CARRITO",bg = "pale turquoise",font = ("Comic Sans MS", 16))
        titulo_pagina.grid(row=0,column=0,padx=20)

        label2 = Label(root2,text = "CATEGORIAS",bg = "pale turquoise",font = ("Comic Sans MS", 16))
        label2.grid(row=0,column=13,padx=20)

        text_espacio = Text(root2,width=95,heigh=32,wrap=WORD)
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

        #=============Logo Python====================================#
        imagen_python = Canvas(root2,width=148,heigh=200)
        imagen_python.create_image(0,0,anchor=NW,image=logo)
        imagen_python.image = logo #Second reference
        imagen_python.grid(row=4,column=14)
        #============================================================#

        #=============Logo Usil======================================#
        imagen_python2 = Canvas(root2,width=142,heigh=150)
        imagen_python2.create_image(0,0,anchor=NW,image=logo_usil)
        imagen_python2.image = logo_usil
        imagen_python2.grid(row=4,column=13)
        #============================================================#

        #boton_manager = Button(root2,text="Manager",width=18,heigh=3)
        #boton_manager.grid(row=3,column=12,rowspan=2)

        boton_eliminar = Button(root2,text="Eliminar producto",width=18,heigh=3,command=lambda:interfaz_eliminar(carrito,'es'))
        boton_eliminar.grid(row=4,column=12,rowspan=2)

        boton_Imprimir_Carrito = Button(root2,text="Imprimir boleta",width=18,heigh=3,command=lambda: funcion_imprimir(text_espacio,carrito))
        boton_Imprimir_Carrito.grid(row=7,column=12,padx=15,rowspan=2)

        boton_Pagar = Button(root2,text="Pagar",width=18,heigh=3,command=lambda:interfaz_pagar(carrito,'es'))
        boton_Pagar.grid(row=7,column=13,padx=15,rowspan=2)

        boton_finalizar = Button(root2,text="Finalizar",width=18,heigh=3,command=quit)
        boton_finalizar.grid(row=7,column=14,padx=15,rowspan=2)

        #Interfaz en Ingles
    def interfaz_In (self):
        #====================================Carrito===================================================#
        carrito = []
        #==============================================================================================#
        root2 = Toplevel()
        root2.title("Sale System")
        root2.geometry("1300x600")
        root2.config(relief="ridge",bd=10)
        root2.resizable(False,False)
        root2.configure(bg="pale turquoise")

        titulo_pagina = Label(root2,text = "SHOPPING CART",bg = "pale turquoise",font = ("Comic Sans MS", 16))
        titulo_pagina.grid(row=0,column=0,padx=20)
        
        label2 = Label(root2,text = "CATEGORIES",bg = "pale turquoise",font = ("Comic Sans MS", 16))
        label2.grid(row=0,column=13,padx=20)
        
        text_espacio = Text(root2,width=78,heigh=32,wrap=WORD)
        text_espacio.grid(row=1,column=0,padx=10,rowspan=9,sticky=E)

        logo = PhotoImage(file ="Img/python.gif")#Variable logo que hace referencia a python.gif en carpeta Img
        logo_usil = PhotoImage(file="Img/usil2.gif")#Variable logo_usil que hace referencia a usil2.gif en carpeta Img

        boton_Bebidas_ingles = Button(root2,text="DRINKS",width= 18,heigh=5,command=lambda: botones_bebidas_en(root2,carrito))
        boton_Bebidas_ingles.grid(row=1,column=12,padx=15)

        boton_Abarrotes_ingles = Button(root2,text="GROCERIES",width=18,heigh=5,command=lambda: botones_abarrotes_en(root2,carrito))
        boton_Abarrotes_ingles.grid(row=1,column=13,padx=15)

        boton_Congelados_ingles = Button(root2,text="FROZEN",width=18,heigh=5,command=lambda: botones_congelados_en(root2,carrito))
        boton_Congelados_ingles.grid(row=1,column=14,padx=15)

        boton_Comida_Preparada_ingles = Button(root2,text="PREPARED FOOD",width=18,heigh=5,command=lambda: botones_comida_preparada_en(root2,carrito))
        boton_Comida_Preparada_ingles.grid(row=2,column=12,padx=15)

        boton_Cuidado_Personal_ingles = Button(root2,text="PERSONAL CARE",width=18,heigh=5,command=lambda: botones_cuidado_personal_en(root2,carrito))
        boton_Cuidado_Personal_ingles.grid(row=2,column=13,padx=15)

        #=============Logo Python====================================#
        imagen_python = Canvas(root2,width=148,heigh=200)
        imagen_python.create_image(0,0,anchor=NW,image=logo)
        imagen_python.image = logo #Second reference
        imagen_python.grid(row=4,column=14)
        #============================================================#

        #=============Logo Usil======================================#
        imagen_python2 = Canvas(root2,width=142,heigh=150)
        imagen_python2.create_image(0,0,anchor=NW,image=logo_usil)
        imagen_python2.image = logo_usil
        imagen_python2.grid(row=4,column=13)
        #============================================================#

        boton_Imprimir_Carrito_ingles = Button(root2,text="CART PRINT",width=18,heigh=3,command=lambda: funcion_imprimir(text_espacio,carrito))
        boton_Imprimir_Carrito_ingles.grid(row=7,column=12,padx=15,rowspan=2)
        
        boton_finalizar_ingles = Button(root2,text="QUIT",width=18,heigh=3,command=quit) 
        boton_finalizar_ingles.grid(row=7,column=13,padx=15,rowspan=2)
        
        boton_Pagar_ingles = Button(root2,text="PAY",width=18,heigh=3,command=lambda:interfaz_pagar(carrito,'en'))
        boton_Pagar_ingles.grid(row=7,column=14,padx=15,rowspan=2)

#========================================== Main =============================================================================#
root.resizable(False,False)
root.title("Sistema de Ventas")
root.configure(bg = "deep sky blue")
root.geometry("400x430")
root.config(relief="ridge",bd=15)
a = principal(root)
root.mainloop()
#=============================================================================================================================#