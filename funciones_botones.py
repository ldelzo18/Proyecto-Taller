from tkinter import *
from tkinter import ttk


def botones_bebidas_es():
    beb = Tk()
    beb.title("Catalogo de Bebidas")
    beb.geometry("800x400")
    beb.resizable(False,False)
    beb.title("Lista de bebidas")

    titulo_categoria = Label(beb,text="BEBIDAS",font = ("TIMES NEW ROMAN", 16))
    
    myLabel1 = ttk.Label(beb,text="Cantidad:",font = ("Arial", 12))
    cantidad = Entry(beb)
    inkaboton = Button(beb, text =" Inca Kola 500ml ",font = ("Arial", 12),width=15)
    cocaboton = Button(beb, text =" Coca Kola 500ml ",font = ("Arial", 12),width=15)
    fantaboton = Button(beb, text ="  Fanta  500ml ",font = ("Arial", 12),width=15) 
    gateboton = Button(beb, text =" Gatorade 500ml ",font = ("Arial", 12),width=15)
    voltboton = Button(beb, text ="   Volt 450ml  ",font = ("Arial", 12),width=15)
    pepsiboton = Button(beb, text ="  Pepsi 500ml ",font = ("Arial", 12),width=15)
    freeboton = Button(beb, text ="  FreeTea 500ml ",font = ("Arial", 12),width=15)
    sanboton = Button(beb, text="  San Luis 625ml ",font = ("Arial", 12),width=15)
    cieloboton = Button(beb, text ="  Cielo 625ml ",font = ("Arial", 12),width=15)
    sporboton = Button(beb, text="  Sporade  500ml ",font = ("Arial", 12),width=15)

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



def botones_bebidas_en():
    beb = Tk()
    beb.title("Drinks Catalogue")
    beb.geometry("800x400")
    beb.resizable(False,False)
    beb.title("Beverages List")

    titulo_categoria = Label(beb,text="DRINKS",font = ("TIMES NEW ROMAN", 16))
    
    myLabel1 = ttk.Label(beb,text="Quantity:",font = ("Arial", 12))
    cantidad = Entry(beb)
    inkaboton = Button(beb, text =" Inca Kola 500ml ",font = ("Arial", 12),width=15)
    cocaboton = Button(beb, text =" Coca Kola 500ml ",font = ("Arial", 12),width=15)
    fantaboton = Button(beb, text ="  Fanta  500ml ",font = ("Arial", 12),width=15) 
    gateboton = Button(beb, text =" Gatorade 500ml ",font = ("Arial", 12),width=15)
    voltboton = Button(beb, text ="   Volt 450ml  ",font = ("Arial", 12),width=15)
    pepsiboton = Button(beb, text ="  Pepsi 500ml ",font = ("Arial", 12),width=15)
    freeboton = Button(beb, text ="  FreeTea 500ml ",font = ("Arial", 12),width=15)
    sanboton = Button(beb, text="  San Luis 625ml ",font = ("Arial", 12),width=15)
    cieloboton = Button(beb, text ="  Cielo 625ml ",font = ("Arial", 12),width=15)
    sporboton = Button(beb, text="  Sporade  500ml ",font = ("Arial", 12),width=15)

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

def botones_abarrotes_es():
    aba = Tk()
    aba.title("Catalogo de Abarrotes")
    aba.geometry("800x400")
    aba.resizable(False,False)
    aba.title("Lista de abarrotes")

    titulo_categoria = Label(aba,text="ABARROTES",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(aba,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(aba)
    picaboton = Button(aba, text = "Picaras",font = ("Arial", 12),width=15)
    laysboton = Button(aba, text = " Lays ",font = ("Arial", 12),width=15)
    dorboton = Button(aba, text = "Doritos",font = ("Arial", 12),width=15)
    sodboton = Button(aba, text =" Soda Field ",font = ("Arial", 12),width=15)
    iberboton = Button(aba, text ="   Iberica  ",font = ("Arial", 12),width=15)
    subboton = Button(aba, text ="  Sublime  ",font = ("Arial", 12),width=15)
    piqboton = Button(aba, text =" Piqueo Snack ",font = ("Arial", 12),width=15)
    doñaboton = Button(aba, text="  Doña Pepa  ",font = ("Arial", 12),width=15)
    cereaboton = Button(aba, text ="  Cereal Bar  ",font = ("Arial", 12),width=15)
    chokisboton = Button(aba, text="  Chokis  ",font = ("Arial", 12),width=15)

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

def botones_abarrotes_en():
    aba = Tk()
    aba.title("Groceries Catalogue")
    aba.geometry("800x400")
    aba.resizable(False,False)
    aba.title("Groceries List")

    titulo_categoria = Label(aba,text="GROCERIES",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(aba,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(aba)
    picaboton = Button(aba, text = "  Picaras  ",font = ("Arial", 12),width=15)
    laysboton = Button(aba, text = "  Lays  ",font = ("Arial", 12),width=15)
    dorboton = Button(aba, text = "  Doritos  ",font = ("Arial", 12),width=15)
    sodboton = Button(aba, text ="  Soda Field  ",font = ("Arial", 12),width=15)
    iberboton = Button(aba, text ="   Iberica  ",font = ("Arial", 12),width=15)
    subboton = Button(aba, text ="  Sublime  ",font = ("Arial", 12),width=15)
    piqboton = Button(aba, text ="  Piqueo Snack  ",font = ("Arial", 12),width=15)
    doñaboton = Button(aba, text="  Doña Pepa  ",font = ("Arial", 12),width=15)
    cereaboton = Button(aba, text ="  Cereal Bar  ",font = ("Arial", 12),width=15)
    chokisboton = Button(aba, text="  Chokis  ",font = ("Arial", 12),width=15)

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

def botones_congelados_es():
    cong = Tk()
    cong.title("Catalogo de Productos Congelados")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cong.title("Lista de Productos Congelados")

    titulo_categoria = Label(cong,text="CONGELADOS",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(cong,text="Cantidad:",font = ("Arial", 12))

    cantidad= Entry(cong)
    luboton = Button(cong, text =" Donofrio Lucuma 1L ",font = ("Arial", 12),width=25)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ",font = ("Arial", 12),width=25)
    moroboton = Button(cong, text = " Nestle morochas 1L ",font = ("Arial", 12),width=25) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ",font = ("Arial", 12),width=25)
    torvaboton = Button(cong , text = " Donofrio Tornado Vainilla 1L ",font = ("Arial", 12),width=25)
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ",font = ("Arial", 12),width=25)
    hamboton = Button(cong, text =" San Fernando 6 hamburguesas",font = ("Arial", 12),width=25)
    pizzpboton = Button(cong, text="  Pizza Peperoni  ",font = ("Arial", 12),width=25)
    pizzamboton = Button(cong, text ="  Pizza Americana  ",font = ("Arial", 12),width=25)
    raviboton = Button(cong, text=" Pack de Ravioles ",font = ("Arial", 12),width=25)    

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

def botones_congelados_en():
    cong = Tk()
    cong.title("Frozen Products Catalogue")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cong.title("Frozen Products List")
    
    
    titulo_categoria = Label(cong,text="FROZEN PRODUCTS",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(cong,text="Quantity:",font = ("Arial", 12))

    cantidad= Entry(cong)
    luboton = Button(cong, text = "Donofrio Lucuma 1L",font = ("Arial", 12),width=25)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ",font = ("Arial", 12),width=25)
    moroboton = Button(cong, text = "Nestle morochas 1L",font = ("Arial", 12),width=25) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ",font = ("Arial", 12),width=25)
    torvaboton = Button(cong , text = " Donofrio Tornado Vanella 1L ",font = ("Arial", 12),width=25)
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ",font = ("Arial", 12),width=25)
    hamboton = Button(cong, text =" San Fernando 6 Patties",font = ("Arial", 12),width=25)
    pizzpboton = Button(cong, text="  Pepperoni Pizza  ",font = ("Arial", 12),width=25)
    pizzamboton = Button(cong, text ="  American Pizza  ",font = ("Arial", 12),width=25)
    raviboton = Button(cong, text=" Ravioli Pack ",font = ("Arial", 12),width=25)

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



def botones_comida_preparada_es():
    com = Tk()
    com.title("Catalogo Comida Preparada")    
    com.geometry("800x400")
    com.resizable(False,False)
    com.title("Comida Preparada")

    titulo_categoria = Label(com,text="COMIDA LISTA",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(com,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(com)
    hamb_car_boton = Button(com, text = " Hamburguesa de Carne ",font = ("Arial", 12),width=25)
    hamb_po_boton = Button(com, text = " Hamburguesa de Pollo ",font = ("Arial", 12),width=25)
    empa_car_boton = Button(com, text = " Empanada de Carne ",font = ("Arial", 12),width=25)
    empa_po_boton = Button(com, text = " Empanada de Pollo ",font = ("Arial", 12),width=25)
    pollo_frito_boton = Button(com, text = " Pollo Frito ",font = ("Arial", 12),width=25)
    wrap_pollo_boton = Button(com, text = " Wrap de Pollo",font = ("Arial", 12),width=25)
    wrap_carne_boton = Button(com, text = " Wrap de Carne ",font = ("Arial", 12),width=25)
    choripan_boton = Button(com, text = " Choripan ",font = ("Arial", 12),width=25)
    SiuMai_boton = Button(com, text = " Siu May ",font = ("Arial", 12),width=25)
    MinPao_boton = Button(com, text = " Min Pao" ,font = ("Arial", 12),width=25)

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

def botones_comida_preparada_en():
    com = Tk()
    com.title("Ready to take Catalogue")    
    com.geometry("800x400")
    com.resizable(False,False)
    com.title("Ready to take!")

    titulo_categoria = Label(com,text="READY TO EAT!",font = ("TIMES NEW ROMAN", 16))
    myLabel1 = ttk.Label(com,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(com)
    hamb_car_boton = Button(com, text = " Meat Hamburger ",font = ("Arial", 12),width=25)
    hamb_po_boton = Button(com, text = " Chicken Hamburger  ",font = ("Arial", 12),width=25)
    empa_car_boton = Button(com, text = " Meat Patty",font = ("Arial", 12),width=25)
    empa_po_boton = Button(com, text = " Chicken Patty ",font = ("Arial", 12),width=25)
    pollo_frito_boton = Button(com, text = " Pollo Frito ",font = ("Arial", 12),width=25)
    wrap_pollo_boton = Button(com, text = " Chicken Wrap ",font = ("Arial", 12),width=25)
    wrap_carne_boton = Button(com, text = " Roast Beef Wrap ",font = ("Arial", 12),width=25)
    choripan_boton = Button(com, text = " Choripan ",font = ("Arial", 12),width=25)
    SiuMai_boton = Button(com, text = " Siu May ",font = ("Arial", 12),width=25)
    MinPao_boton = Button(com, text = " Min Pao ",font = ("Arial", 12),width=25)

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

def botones_cuidado_personal_es():
    cui = Tk()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("800x400")
    cui.resizable(False,False)
    cui.title("Cuidado Personal")

    titulo_categoria = Label(cui,text="CUIDADO PERSONAL",font = ("TIMES NEW ROMAN", 14))
    myLabel1 = ttk.Label(cui,text="Cantidad:",font = ("Arial", 12))

    cantidad = Entry(cui)
    jabon_boton = Button(cui, text = " Jabon Dove ",font = ("Arial", 12),width=25)
    shamp_boton = Button(cui, text = " H&S Old Spice ",font = ("Arial", 12),width=25)
    pasta_boton = Button(cui, text = " Pasta de dientes Colgate ",font = ("Arial", 12),width=25)
    cepi_boton = Button(cui, text = " Cepillo Colgate ",font = ("Arial", 12),width=25)
    gill_boton = Button(cui, text = " Hoja de afeitar Gillet ",font = ("Arial", 12),width=25)
    lady_boton = Button(cui, text = " Toallas femeninas LadySoft ",font = ("Arial", 12),width=25)
    enjuage_listerine_boton = Button(cui, text = " Listerine 500 ML ",font = ("Arial", 12),width=25)
    pasta_Dento_boton = Button(cui, text = " Pasta Dento ",font = ("Arial", 12),width=25)
    crema_Gillete_boton = Button(cui, text = " Crema de Afeitar Gillete ",font = ("Arial", 12),width=25)
    shampoo_HeadandShoulders_boton = Button(cui, text = " Head & Shoulders 375 ML ",font = ("Arial", 12),width=25)

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



def botones_cuidado_personal_en():
    cui = Tk()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("800x400")
    cui.resizable(False,False)
    cui.title("Personal Care")

    titulo_categoria = Label(cui,text="PERSONAL CARE",font = ("TIMES NEW ROMAN", 14))
    myLabel1 = ttk.Label(cui,text="Quantity:",font = ("Arial", 12))

    cantidad = Entry(cui)
    jabon_boton = Button(cui, text = " Soap Dove ",font = ("Arial", 12),width=25)
    shamp_boton = Button(cui, text = " H&S Old Spice ",font = ("Arial", 12),width=25)
    pasta_boton = Button(cui, text = " Colgate Toothpaste ",font = ("Arial", 12),width=25)
    cepi_boton = Button(cui, text = " Colgate Toothbrush ",font = ("Arial", 12),width=25)
    gill_boton = Button(cui, text = " Gillete Razor Blade ",font = ("Arial", 12),width=25)
    lady_boton = Button(cui, text = " LadySoft Pads ",font = ("Arial", 12),width=25)
    enjuage_listerine_boton = Button(cui, text = " Listerine 500 ML ",font = ("Arial", 12),width=25)
    pasta_Dento_boton = Button(cui, text = " Dento Toothpaste ",font = ("Arial", 12),width=25)
    crema_Gillete_boton = Button(cui, text = " Gillete Shaving Cream",font = ("Arial", 12),width=25)
    shampoo_HeadandShoulders_boton = Button(cui, text = " Head & Shoulders 375 ML ",font = ("Arial", 12),width=25)

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

def imprimirLista(lista_Producto,lista_Precios,textArea):
    temp = ""
    for x in lista_Producto:
        temp += x+"\n"
    
    textArea.insert(0.0,temp)

        

def addInkaKola(lista_Producto,lista_Precios,cantidad):
    for x in range(0,cantidad):
        lista_Producto.append("Inka Kola 500 ml")
        lista_Precios.append(2.00)
        
