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
    
    myLabel1 = ttk.Label(beb,text="Quantity",font = ("Arial", 12))
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
    myLabel1 = ttk.Label(aba,text="Cantidad",font = ("Arial", 12))

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
    myLabel1 = ttk.Label(aba,text="Quantity",font = ("Arial", 12))

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



def botones_congelados_es():
    cong = Tk()
    cong.title("Catalogo de Productos Congelados")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cantidad= Entry(cong).place(x=20,y=30)
    luboton = Button(cong, text = "Donofrio Lucuma 1L").place(x=50, y = 150)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ").place(x = 200, y = 150)
    moroboton = Button(cong, text = "Nestle morochas 1L").place(x= 350, y = 150) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ").place(x = 600, y= 150)
    torvaboton = Button(cong , text = " Donofrio Tornado Vainilla 1L ").place(x = 750, y= 150)
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ").place(x =50, y = 370)
    hamboton = Button(cong, text =" San Fernando 6 hamburguesas").place(x = 200,y =370)
    pizzpboton = Button(cong, text="  Pizza Peperoni  ").place(x=350, y=370)
    pizzamboton = Button(cong, text ="  Pizza Americana  ").place(x = 600, y = 370)
    raviboton = Button(cong, text=" Pack de Ravioles ").place(x= 750, y = 370)    

    cong.mainloop()




def botones_congelados_en():
    cong = Tk()
    cong.title("Catalogo de Productos Congelados")
    cong.geometry("800x400")
    cong.resizable(False,False)
    cantidad= Entry(cong).place(x=20,y=30)
    luboton = Button(cong, text = "Donofrio Lucuma 1L").place(x=50, y = 150)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ").place(x = 200, y = 150)
    moroboton = Button(cong, text = "Nestle morochas 1L").place(x= 350, y = 150) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ").place(x = 600, y= 150)
    torvaboton = Button(cong , text = " Donofrio Tornado Vainilla 1L ").place(x = 750, y= 150)
    nuggboton = Button(cong, text ="  San Fernando 15 Nuggets ").place(x =50, y = 370)
    hamboton = Button(cong, text =" San Fernando 6 hamburguesas").place(x = 200,y =370)
    pizzpboton = Button(cong, text="  Pizza Peperoni  ").place(x=350, y=370)
    pizzamboton = Button(cong, text ="  Pizza Americana  ").place(x = 600, y = 370)
    raviboton = Button(cong, text=" Pack de Ravioles ").place(x= 750, y = 370)    

    cong.mainloop()



def botones_comida_preparada_es():
    com = Tk()
    com.title("Catalogo Comida Preparada")    
    com.geometry("500x300")
    com.resizable(False,False)
    cantidad = Entry(com).place(x=20,y=30)
    hamb_car_boton = Button(com, text = " Hamburguesa de Carne ").place(x=50,y=150)
    hamb_po_boton = Button(com, text = " Hamburguesa de Pollo ").place(x=250, y=150)
    empa_car_boton = Button(com, text = " Empanada de Carne ").place(x=50,y=270)
    empa_po_boton = Button(com, text = " Empanada de Pollo ").place(x=250,y=270)



    com.mainloop()

def botones_comida_preparada_en():
    com = Tk()
    com.title("Ready to take Catalogue")    
    com.geometry("500x300")
    com.resizable(False,False)
    cantidad = Entry(com).place(x=20,y=30)
    hamb_car_boton = Button(com, text = " Meat Hamburger ").place(x=50,y=150)
    hamb_po_boton = Button(com, text = "Chicken Hamburger  ").place(x=250, y=150)
    empa_car_boton = Button(com, text = " Meat Patty").place(x=50,y=270)
    empa_po_boton = Button(com, text = " Chicken Patty ").place(x=250,y=270)

    com.mainloop()

def botones_cuidado_personal_es():
    cui = Tk()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("700x400")
    cui.resizable(False,False)
    cantidad = Entry(cui).place(x=20,y=30)
    jabon_boton = Button(cui, text = " Jabon Dove ").place(x=50,y=150)
    shamp_boton = Button(cui, text = " H&S Old Spice ").place(x=200,y=150)
    pasta_boton = Button(cui, text = " Pasta de dientes Colgate ").place(x=350,y=150)
    cepi_boton = Button(cui, text = " Cepillo Colgate ").place(x=50,y=370)
    gill_boton = Button(cui, text = " Hoja de afeitar Gillet ").place(x=200,y=370)
    lady_boton = Button(cui, text = " Toallas femeninas LadySoft ").place(x=350,y=370)

    cui.mainloop()



def botones_cuidado_personal_en():
    cui = Tk()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("700x400")
    cui.resizable(False,False)
    cantidad = Entry(cui).place(x=20,y=30)
    jabon_boton = Button(cui, text = " Soap Dove ").place(x=50,y=150)
    shamp_boton = Button(cui, text = " H&S Old Spice ").place(x=200,y=150)
    pasta_boton = Button(cui, text = " Toothpaste Colgate ").place(x=350,y=150)
    cepi_boton = Button(cui, text = " Toothbrush Colgate ").place(x=50,y=370)
    gill_boton = Button(cui, text = " Gillet Razor Blade ").place(x=200,y=370)
    always_boton = Button(cui, text = " Pads Always ").place(x=350,y=370)    

    cui.mainloop()