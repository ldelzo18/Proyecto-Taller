from tkinter import *
from tkinter import ttk
from funciones_productos import *
from tkinter import messagebox
from funciones_mysql import *

def botones_bebidas_es(lastWindow,carrito_Bebidas):
    beb = Toplevel()
    beb.title("Catalogo de Bebidas")
    beb.geometry("800x400")
    beb.resizable(False,False)
    beb.title("Lista de bebidas")

    titulo_categoria = Label(beb,text="BEBIDAS",font = ("TIMES NEW ROMAN", 16))
    
    myLabel1 = ttk.Label(beb,text="Cantidad:",font = ("Arial", 12))
    
    cantidad = Entry(beb)

    inkaboton = Button(beb, text =" Inca Kola 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,0,'es'))
    cocaboton = Button(beb, text =" Coca Kola 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,1,'es'))
    fantaboton = Button(beb, text ="  Fanta  500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,2,'es')) 
    gateboton = Button(beb, text =" Gatorade 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,3,'es'))
    voltboton = Button(beb, text ="   Volt 450ml  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,4,'es'))
    pepsiboton = Button(beb, text ="  Pepsi 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,5,'es'))
    freeboton = Button(beb, text ="  FreeTea 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,6,'es'))
    sanboton = Button(beb, text="  San Luis 625ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,7,'es'))
    cieloboton = Button(beb, text ="  Cielo 625ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,8,'es'))
    sporboton = Button(beb, text="  Sporade  500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,9,'es'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)
    
    inkaboton.grid(row=2,column=0,padx=10,pady=10)
    cocaboton.grid(row=2,column=1,padx=10,pady=10)
    fantaboton.grid(row=2,column=2,padx=10,pady=10)
    gateboton.grid(row=3,column=0,padx=10,pady=10)
    voltboton.grid(row=3,column=1,padx=10,pady=10)
    pepsiboton.grid(row=3,column=2,padx=10,pady=10)
    freeboton.grid(row=4,column=0,padx=10,pady=10)
    sanboton.grid(row=4,column=1,padx=10,pady=10)
    cieloboton.grid(row=4,column=2,padx=10,pady=10)
    sporboton.grid(row=4,column=3,padx=10,pady=10)

    beb.mainloop()

def botones_bebidas_en(lastWindow,carrito_Bebidas):
    beb = Toplevel()
    beb.title("Drinks Catalogue")
    beb.geometry("800x400")
    beb.resizable(False,False)
    beb.title("Beverages List")

    titulo_categoria = Label(beb,text="DRINKS",font = ("TIMES NEW ROMAN", 16))
    
    myLabel1 = ttk.Label(beb,text="Quantity:",font = ("Arial", 12))
    cantidad = Entry(beb)
    inkaboton = Button(beb, text =" Inca Kola 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,0,'en'))
    cocaboton = Button(beb, text =" Coca Kola 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,1,'en'))
    fantaboton = Button(beb, text ="  Fanta  500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,2,'en')) 
    gateboton = Button(beb, text =" Gatorade 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,3,'en'))
    voltboton = Button(beb, text ="   Volt 450ml  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,4,'en'))
    pepsiboton = Button(beb, text ="  Pepsi 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,5,'en'))
    freeboton = Button(beb, text ="  FreeTea 500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,6,'en'))
    sanboton = Button(beb, text="  San Luis 625ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,7,'en'))
    cieloboton = Button(beb, text ="  Cielo 625ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,8,'en'))
    sporboton = Button(beb, text="  Sporade  500ml ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,beb,carrito_Bebidas,cantidad,9,'en'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)
    
    inkaboton.grid(row=2,column=0,padx=10,pady=10)
    cocaboton.grid(row=2,column=1,padx=10,pady=10)
    fantaboton.grid(row=2,column=2,padx=10,pady=10)
    gateboton.grid(row=3,column=0,padx=10,pady=10)
    voltboton.grid(row=3,column=1,padx=10,pady=10)
    pepsiboton.grid(row=3,column=2,padx=10,pady=10)
    freeboton.grid(row=4,column=0,padx=10,pady=10)
    sanboton.grid(row=4,column=1,padx=10,pady=10)
    cieloboton.grid(row=4,column=2,padx=10,pady=10)
    sporboton.grid(row=4,column=3,padx=10,pady=10)

    beb.mainloop()

def botones_abarrotes_es(lastWindow,carrito_abarrotes):
    aba = Toplevel()
    aba.title("Catalogo de Abarrotes")
    aba.geometry("800x400")
    aba.resizable(False,False)
    aba.title("Lista de abarrotes")

    titulo_categoria = Label(aba,text="ABARROTES",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(aba,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(aba)
    picaboton = Button(aba, text = "Picaras",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,10,'es'))
    laysboton = Button(aba, text = " Lays ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,11,'es'))
    dorboton = Button(aba, text = "Doritos",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,12,'es'))
    sodboton = Button(aba, text =" Soda Field ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,13,'es'))
    iberboton = Button(aba, text ="   Iberica  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,14,'es'))
    subboton = Button(aba, text ="  Sublime  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,15,'es'))
    piqboton = Button(aba, text =" Piqueo Snack ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,16,'es'))
    doñaboton = Button(aba, text="  Doña Pepa  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,17,'es'))
    cereaboton = Button(aba, text ="  Cereal Bar  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,18,'es'))
    chokisboton = Button(aba, text="  Chokis  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,19,'es'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    picaboton.grid(row=2,column=0,padx=10,pady=10)
    laysboton.grid(row=2,column=1,padx=10,pady=10)
    dorboton.grid(row=2,column=2,padx=10,pady=10)
    sodboton.grid(row=3,column=0,padx=10,pady=10)
    iberboton.grid(row=3,column=1,padx=10,pady=10)
    subboton.grid(row=3,column=2,padx=10,pady=10)
    piqboton.grid(row=4,column=0,padx=10,pady=10)
    doñaboton.grid(row=4,column=1,padx=10,pady=10)
    cereaboton.grid(row=4,column=2,padx=10,pady=10)
    chokisboton.grid(row=4,column=3,padx=10,pady=10)

    aba.mainloop()

def botones_abarrotes_en(lastWindow,carrito_abarrotes):
    aba = Toplevel()
    aba.title("Groceries Catalogue")
    aba.geometry("800x400")
    aba.resizable(False,False)
    aba.title("Groceries List")

    titulo_categoria = Label(aba,text="GROCERIES",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(aba,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(aba)
    picaboton = Button(aba, text = "  Picaras  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,10,'en'))
    laysboton = Button(aba, text = "  Lays  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,11,'en'))
    dorboton = Button(aba, text = "  Doritos  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,12,'en'))
    sodboton = Button(aba, text ="  Soda Field  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,13,'en'))
    iberboton = Button(aba, text ="   Iberica  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,14,'en'))
    subboton = Button(aba, text ="  Sublime  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,15,'en'))
    piqboton = Button(aba, text ="  Piqueo Snack  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,16,'en'))
    doñaboton = Button(aba, text="  Doña Pepa  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,17,'en'))
    cereaboton = Button(aba, text ="  Cereal Bar  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,18,'en'))
    chokisboton = Button(aba, text="  Chokis  ",font = ("Arial", 12),width=15,command=lambda:add_Producto(lastWindow,aba,carrito_abarrotes,cantidad,19,'en'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    picaboton.grid(row=2,column=0,padx=10,pady=10)
    laysboton.grid(row=2,column=1,padx=10,pady=10)
    dorboton.grid(row=2,column=2,padx=10,pady=10)
    sodboton.grid(row=3,column=0,padx=10,pady=10)
    iberboton.grid(row=3,column=1,padx=10,pady=10)
    subboton.grid(row=3,column=2,padx=10,pady=10)
    piqboton.grid(row=4,column=0,padx=10,pady=10)
    doñaboton.grid(row=4,column=1,padx=10,pady=10)
    cereaboton.grid(row=4,column=2,padx=10,pady=10)
    chokisboton.grid(row=4,column=3,padx=10,pady=10)


    aba.mainloop()    

def botones_congelados_es(lastWindow,carrito_congelados):
    cong = Toplevel()
    cong.title("Catalogo de Productos Congelados")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cong.title("Lista de Productos Congelados")

    titulo_categoria = Label(cong,text="CONGELADOS",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(cong,text="Cantidad:",font = ("Arial", 12))

    cantidad= Entry(cong)
    luboton = Button(cong, text =" Donofrio Lucuma 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,20,'es'))
    nesboton = Button(cong, text = " Nestle beso de moza 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,21,'es'))
    moroboton = Button(cong, text = " Nestle morochas 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,22,'es'))
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,23,'es'))
    torvaboton = Button(cong , text = " Donofrio Tornado Vainilla 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,24,'es'))
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,25,'es'))
    hamboton = Button(cong, text =" San Fernando 6 hamburguesas",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,26,'es'))
    pizzpboton = Button(cong, text="  Pizza Peperoni  ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,27,'es'))
    pizzamboton = Button(cong, text ="  Pizza Americana  ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,28,'es'))
    raviboton = Button(cong, text=" Pack de Ravioles ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,29,'es'))    

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)
    
    luboton.grid(row=2,column=0,padx=10,pady=10)
    nesboton.grid(row=2,column=1,padx=10,pady=10)
    moroboton.grid(row=3,column=0,padx=10,pady=10)
    torluboton.grid(row=3,column=1,padx=10,pady=10)
    torvaboton.grid(row=4,column=0,padx=10,pady=10)
    nuggboton.grid(row=4,column=1,padx=10,pady=10)
    hamboton.grid(row=5,column=0,padx=10,pady=10)
    pizzpboton.grid(row=5,column=1,padx=10,pady=10)
    pizzamboton.grid(row=6,column=0,padx=10,pady=10)
    raviboton.grid(row=6,column=1,padx=10,pady=10)
    
    cong.mainloop()

def botones_congelados_en(lastWindow,carrito_congelados):
    cong = Toplevel()
    cong.title("Frozen Products Catalogue")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cong.title("Frozen Products List")
    
    
    titulo_categoria = Label(cong,text="FROZEN PRODUCTS",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(cong,text="Quantity:",font = ("Arial", 12))

    cantidad= Entry(cong)
    luboton = Button(cong, text = "Donofrio Lucuma 1L",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,20,'en'))
    nesboton = Button(cong, text = " Nestle beso de moza 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,21,'en'))
    moroboton = Button(cong, text = "Nestle morochas 1L",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,22,'en')) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,23,'en'))
    torvaboton = Button(cong , text = " Donofrio Tornado Vanella 1L ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,24,'en'))
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,25,'en'))
    hamboton = Button(cong, text =" San Fernando 6 Patties",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,26,'en'))
    pizzpboton = Button(cong, text="  Pepperoni Pizza  ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,27,'en'))
    pizzamboton = Button(cong, text ="  American Pizza  ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,28,'en'))
    raviboton = Button(cong, text=" Ravioli Pack ",font = ("Arial", 12),width=25,command=lambda:add_Producto(lastWindow,cong,carrito_congelados,cantidad,29,'en'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)
    
    luboton.grid(row=2,column=0,padx=10,pady=10)
    nesboton.grid(row=2,column=1,padx=10,pady=10)
    moroboton.grid(row=3,column=0,padx=10,pady=10)
    torluboton.grid(row=3,column=1,padx=10,pady=10)
    torvaboton.grid(row=4,column=0,padx=10,pady=10)
    nuggboton.grid(row=4,column=1,padx=10,pady=10)
    hamboton.grid(row=5,column=0,padx=10,pady=10)
    pizzpboton.grid(row=5,column=1,padx=10,pady=10)
    pizzamboton.grid(row=6,column=0,padx=10,pady=10)
    raviboton.grid(row=6,column=1,padx=10,pady=10)

    cong.mainloop()



def botones_comida_preparada_es(lastWindow, carrito_comidas):
    com = Toplevel()
    com.title("Catalogo Comida Preparada")    
    com.geometry("800x400")
    com.resizable(False,False)
    com.title("Comida Preparada")

    titulo_categoria = Label(com,text="COMIDA LISTA",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(com,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(com)
    hamb_car_boton = Button(com, text = " Hamburguesa de Carne ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,30,'es'))
    hamb_po_boton = Button(com, text = " Hamburguesa de Pollo ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,31,'es'))
    empa_car_boton = Button(com, text = " Empanada de Carne ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,32,'es'))
    empa_po_boton = Button(com, text = " Empanada de Pollo ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,33,'es'))
    pollo_frito_boton = Button(com, text = " Pollo Frito ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,34,'es'))
    wrap_pollo_boton = Button(com, text = " Wrap de Pollo",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,35,'es'))
    wrap_carne_boton = Button(com, text = " Wrap de Carne ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,36,'es'))
    choripan_boton = Button(com, text = " Choripan ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,37,'es'))
    SiuMai_boton = Button(com, text = " Siu May ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,38,'es'))
    MinPao_boton = Button(com, text = " Min Pao" ,font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,39,'es'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    hamb_car_boton.grid(row=2,column=0,padx=10,pady=10)
    hamb_po_boton.grid(row=2,column=1,padx=10,pady=10)
    empa_car_boton.grid(row=3,column=0,padx=10,pady=10)
    empa_po_boton.grid(row=3,column=1,padx=10,pady=10)
    pollo_frito_boton.grid(row=4,column=0,padx=10,pady=10)
    wrap_pollo_boton.grid(row=4,column=1,padx=10,pady=10)
    wrap_carne_boton.grid(row=5,column=0,padx=10,pady=10)
    choripan_boton.grid(row=5,column=1,padx=10,pady=10)
    SiuMai_boton.grid(row=6,column=0,padx=10,pady=10)
    MinPao_boton.grid(row=6,column=1,padx=10,pady=10)

    com.mainloop()

def botones_comida_preparada_en(lastWindow, carrito_comidas):
    com = Toplevel()
    com.title("Ready to take Catalogue")    
    com.geometry("800x400")
    com.resizable(False,False)
    com.title("Ready to take!")

    titulo_categoria = Label(com,text="READY TO EAT!",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(com,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(com)
    hamb_car_boton = Button(com, text = " Meat Hamburger ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,30,'en'))
    hamb_po_boton = Button(com, text = " Chicken Hamburger  ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,31,'en'))
    empa_car_boton = Button(com, text = " Meat Patty",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,32,'en'))
    empa_po_boton = Button(com, text = " Chicken Patty ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,33,'en'))
    pollo_frito_boton = Button(com, text = " Pollo Frito ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,34,'en'))
    wrap_pollo_boton = Button(com, text = " Chicken Wrap ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,35,'en'))
    wrap_carne_boton = Button(com, text = " Roast Beef Wrap ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,36,'en'))
    choripan_boton = Button(com, text = " Choripan ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,37,'en'))
    SiuMai_boton = Button(com, text = " Siu May ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,38,'en'))
    MinPao_boton = Button(com, text = " Min Pao ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,com,carrito_comidas,cantidad,39,'en'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    hamb_car_boton.grid(row=2,column=0,padx=10,pady=10)
    hamb_po_boton.grid(row=2,column=1,padx=10,pady=10)
    empa_car_boton.grid(row=3,column=0,padx=10,pady=10)
    empa_po_boton.grid(row=3,column=1,padx=10,pady=10)
    pollo_frito_boton.grid(row=4,column=0,padx=10,pady=10)
    wrap_pollo_boton.grid(row=4,column=1,padx=10,pady=10)
    wrap_carne_boton.grid(row=5,column=0,padx=10,pady=10)
    choripan_boton.grid(row=5,column=1,padx=10,pady=10)
    SiuMai_boton.grid(row=6,column=0,padx=10,pady=10)
    MinPao_boton.grid(row=6,column=1,padx=10,pady=10)

    com.mainloop()

def botones_cuidado_personal_es(lastWindow,carrito_cuidados):
    cui = Toplevel()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("800x400")
    cui.resizable(False,False)
    cui.title("Cuidado Personal")

    titulo_categoria = Label(cui,text="CUIDADO PERSONAL",font = ("TIMES NEW ROMAN", 14))
    myLabel1 = ttk.Label(cui,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(cui)
    jabon_boton = Button(cui, text = " Jabon Dove ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,40,'es'))
    shamp_boton = Button(cui, text = " H&S Old Spice ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,41,'es'))
    pasta_boton = Button(cui, text = " Pasta de dientes Colgate ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,42,'es'))
    cepi_boton = Button(cui, text = " Cepillo Colgate ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,43,'es'))
    gill_boton = Button(cui, text = " Hoja de afeitar Gillet ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,44,'es'))
    lady_boton = Button(cui, text = " Toallas femeninas LadySoft ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,45,'es'))
    enjuage_listerine_boton = Button(cui, text = " Listerine 500 ML ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,46,'es'))
    pasta_Dento_boton = Button(cui, text = " Pasta Dento ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,47,'es'))
    crema_Gillete_boton = Button(cui, text = " Crema de Afeitar Gillete ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,48,'es'))
    shampoo_HeadandShoulders_boton = Button(cui, text = " Head & Shoulders 375 ML ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,49,'es'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    jabon_boton.grid(row=2,column=0,padx=10,pady=10)
    shamp_boton.grid(row=2,column=1,padx=10,pady=10)
    pasta_boton.grid(row=3,column=0,padx=10,pady=10)
    cepi_boton.grid(row=3,column=1,padx=10,pady=10)
    gill_boton.grid(row=4,column=0,padx=10,pady=10)
    lady_boton.grid(row=4,column=1,padx=10,pady=10)
    enjuage_listerine_boton.grid(row=5,column=0,padx=10,pady=10)
    pasta_Dento_boton.grid(row=5,column=1,padx=10,pady=10)
    crema_Gillete_boton.grid(row=6,column=0,padx=10,pady=10)
    shampoo_HeadandShoulders_boton.grid(row=6,column=1,padx=10,pady=10)

    cui.mainloop()



def botones_cuidado_personal_en(lastWindow,carrito_cuidados):
    cui = Toplevel()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("800x400")
    cui.resizable(False,False)
    cui.title("Personal Care")

    titulo_categoria = Label(cui,text="PERSONAL CARE",font = ("TIMES NEW ROMAN", 14))
    myLabel1 = ttk.Label(cui,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(cui)
    jabon_boton = Button(cui, text = " Soap Dove ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,40,'en'))
    shamp_boton = Button(cui, text = " H&S Old Spice ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,41,'en'))
    pasta_boton = Button(cui, text = " Colgate Toothpaste ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,42,'en'))
    cepi_boton = Button(cui, text = " Colgate Toothbrush ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,43,'en'))
    gill_boton = Button(cui, text = " Gillete Razor Blade ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,44,'en'))
    lady_boton = Button(cui, text = " LadySoft Pads ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,45,'en'))
    enjuage_listerine_boton = Button(cui, text = " Listerine 500 ML ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,46,'en'))
    pasta_Dento_boton = Button(cui, text = " Dento Toothpaste ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,47,'en'))
    crema_Gillete_boton = Button(cui, text = " Gillete Shaving Cream",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,48,'en'))
    shampoo_HeadandShoulders_boton = Button(cui, text = " Head & Shoulders 375 ML ",font = ("Arial", 12),width=25,command=lambda: add_Producto(lastWindow,cui,carrito_cuidados,cantidad,49,'en'))

    titulo_categoria.grid(row=0,column=0,padx=5,pady=5)
    myLabel1.grid(row=1,column=0,padx=5,pady=5)
    cantidad.grid(row=1,column=1,padx=5,pady=5)

    jabon_boton.grid(row=2,column=0,padx=10,pady=10)
    shamp_boton.grid(row=2,column=1,padx=10,pady=10)
    pasta_boton.grid(row=3,column=0,padx=10,pady=10)
    cepi_boton.grid(row=3,column=1,padx=10,pady=10)
    gill_boton.grid(row=4,column=0,padx=10,pady=10)
    lady_boton.grid(row=4,column=1,padx=10,pady=10)
    enjuage_listerine_boton.grid(row=5,column=0,padx=10,pady=10)
    pasta_Dento_boton.grid(row=5,column=1,padx=10,pady=10)
    crema_Gillete_boton.grid(row=6,column=0,padx=10,pady=10)
    shampoo_HeadandShoulders_boton.grid(row=6,column=1,padx=10,pady=10)

    cui.mainloop()

def pagar_efectivo(total,campo_entry,commander,carrito,idioma):

    if idioma == 'es':
        try:#Aplicando excepciones en caso valor del campo_entry no pueda ser convertido a float

            pago_usuario = float(campo_entry.get())#Convirtiendo valor a float

            if pago_usuario >= total:#Comprobando que el valor pago_usuario sea suficiente para el pago
                messagebox.showinfo('PAGO','Su pago se realizo satisfactoriamente\nSu vuelto es de '+str(pago_usuario-total)+" soles.")
                carrito.clear()
                commander.destroy()
        
            else:#En caso que el valor no sea suficiente
                messagebox.showerror('ERROR','El monto ingresado no es suficiente!')
                commander.lift()#Traer la ventana de pago hacia adelante

        except:#En caso de error en la conversion
        
            if campo_entry.get() == '':#En caso de que el campo_entry este vacio
                messagebox.showerror('Error','No se ha ingresado ningun monto')#Mostrar mensaje de error
        
            else:#En caso de que el valor no sea un valor numerico
                messagebox.showerror('Error','El monto no es valido!')#Mostrar mensaje de error
        
            commander.lift()#Traer la ventana de pago hacia adelante
    
    elif idioma == 'en':

        try:#Aplicando excepciones en caso valor del campo_entry no pueda ser convertido a float

            pago_usuario = float(campo_entry.get())#Convirtiendo valor a float

            if pago_usuario >= total:#Comprobando que el valor pago_usuario sea suficiente para el pago
                messagebox.showinfo('PAGO','Your payment was successful\nYour change is '+str(pago_usuario-total)+" soles.")
                carrito.clear()
                commander.destroy()
        
            else:#En caso que el valor no sea suficiente
                messagebox.showerror('ERROR','The amount entered is not enough to proceed!')
                commander.lift()#Traer la ventana de pago hacia adelante

        except:#En caso de error en la conversion
        
            if campo_entry.get() == '':#En caso de que el campo_entry este vacio
                messagebox.showerror('Error','No amount was entered')#Mostrar mensaje de error
        
            else:#En caso de que el valor no sea un valor numerico
                messagebox.showerror('Error','The amount entered is not valid!')#Mostrar mensaje de error
        
            commander.lift()#Traer la ventana de pago hacia adelante
    


def pagar_dc(total,campo_entry,commander,carrito,idioma):

    if idioma == 'es':
        #===============================Comprobando si hay error en conversion==========================#
        try:
            pago_usuario = float(campo_entry.get())#Convirtiendo valor a float
            nuevo_pago = str(pago_usuario + 5)

            temp = 'Todo pago por tarjeta de debito o credito\ntiene un recargo de 5 soles\nEsta de acuerdo con proceder a pagar el monto de: '+nuevo_pago+'?'
            result = messagebox.askquestion('PAGO DEBITO/CREDITO',temp)

            if result == 'yes':#En caso el usuario acepte el recargo de 5 soles
                messagebox.showinfo('PAGO','Su pago se ha realizado satisfactoriamente: '+nuevo_pago+' soles')
                carrito.clear()
                commander.destroy()

            else:#En caso de que el usuario no acepte el recargo de 5 soles
                messagebox.showinfo('PAGO','No se ha cargado ningun valor a su tarjeta')
                commander.lift()

        except:

            if campo_entry.get() == '':#En caso de que el campo_entry este vacio
                messagebox.showerror('Error','No se ha ingresado ningun monto')#Mostrar mensaje de error
        
            else:#En caso de que el valor no sea un valor numerico
                messagebox.showerror('Error','El monto no es valido!')#Mostrar mensaje de error
        
            commander.lift()#Traer la ventana de pago hacia adelante
        #==================================================================================================#

    elif idioma == 'en':
        #===============================Comprobando si hay error en conversion==========================#
        try:
            pago_usuario = float(campo_entry.get())#Convirtiendo valor a float
            nuevo_pago = str(pago_usuario + 5)

            temp = 'Any payment done by debit or credit card will be charged with 5 soles\nDo you agree to proceed with the payment '+nuevo_pago+' soles?'
            result = messagebox.askquestion('DEBIT/CREDIT PAYMENT',temp)

            if result == 'yes':#En caso el usuario acepte el recargo de 5 soles
                messagebox.showinfo('PAYMENT','Your payment was successful, you were charged with: '+nuevo_pago+' soles')
                carrito.clear()
                commander.destroy()

            else:#En caso de que el usuario no acepte el recargo de 5 soles
                messagebox.showinfo('PAGO','No charge was debit from your credit/debit card')
                commander.lift()

        except:

            if campo_entry.get() == '':#En caso de que el campo_entry este vacio
                messagebox.showerror('Error','No amount was entered')#Mostrar mensaje de error
        
            else:#En caso de que el valor no sea un valor numerico
                messagebox.showerror('Error','The amount entered is not valid!')#Mostrar mensaje de error
        
            commander.lift()#Traer la ventana de pago hacia adelante
        #==================================================================================================#
def interfaz_pagar(carrito,idioma):
    
    if idioma == 'es':
        if len(carrito) != 0:
        
            total = 0

            for x in range(len(carrito)):
                valor = retornar_precio(carrito[x][0])
                total += valor * (carrito[x][1])

            loader = Toplevel()
            loader.title("Medio de Pago")
            loader.resizable(False,False)
            loader.geometry("400x300")
            loader.configure(bg="pale turquoise",relief='groove',bd=10)

            frame = Frame(loader,bg='skyblue',width=300,heigh=100)
            frame.pack()

            #Texto de la ventana
            mensaje1 = Label(frame,text="TOTAL A PAGAR:",font = ("TIMES NEW ROMAN", 12),bg= 'sky blue').place(x=30,y=10)
            mostrarTotal = Label(frame,text=str(total)+' soles',font = ("TIMES NEW ROMAN", 12),bg= 'sky blue').place(x=200,y=10)
            label1 = Label(frame,text="Monto a ingresar:",font = ("TIMES NEW ROMAN", 12),bg='skyblue').place(x=30,y=40)

            #Campo Entry para el monto que ingrese el usuario
            campo_monto = Entry(frame)
            campo_monto.place(x=150,y=40)

            #Botones
            boton_efectivo = Button(loader,text='EFECTIVO',width=30,command=lambda:pagar_efectivo(total,campo_monto,loader,carrito,'es')).place(x=80,y=150)
            boton_dc = Button(loader,text='DEBITO/CREDITO',width=30,command=lambda:pagar_dc(total,campo_monto,loader,carrito,'es')).place(x=80,y=200)
        
    
        else:
            messagebox.showerror('Error','No hay nada en el carrito!')
    
    elif idioma == 'en':
        if len(carrito) != 0:
        
            total = 0

            for x in range(len(carrito)):
                valor = retornar_precio(carrito[x][0])
                total += valor * (carrito[x][1])

            loader = Toplevel()
            loader.title("Payment Methods")
            loader.resizable(False,False)
            loader.geometry("400x300")
            loader.configure(bg="pale turquoise",relief='groove',bd=10)

            frame = Frame(loader,bg='skyblue',width=300,heigh=100)
            frame.pack()

            #Texto de la ventana
            mensaje1 = Label(frame,text="TOTAL TO PAY:",font = ("TIMES NEW ROMAN", 12),bg= 'sky blue').place(x=30,y=10)
            mostrarTotal = Label(frame,text=str(total)+' soles',font = ("TIMES NEW ROMAN", 12),bg= 'sky blue').place(x=200,y=10)
            label1 = Label(frame,text="Amount to pay:",font = ("TIMES NEW ROMAN", 12),bg='skyblue').place(x=30,y=40)

            #Campo Entry para el monto que ingrese el usuario
            campo_monto = Entry(frame)
            campo_monto.place(x=150,y=40)

            #Botones
            boton_efectivo = Button(loader,text='CASH',width=30,command=lambda:pagar_efectivo(total,campo_monto,loader,carrito,'en')).place(x=80,y=150)
            boton_dc = Button(loader,text='DEBIT/CREDIT',width=30,command=lambda:pagar_dc(total,campo_monto,loader,carrito,'en')).place(x=80,y=200)
        
    
        else:
            messagebox.showerror('Error','The cart is empty!')


    




 

        


        
