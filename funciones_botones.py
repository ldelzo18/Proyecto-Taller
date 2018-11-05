from tkinter import *
from tkinter import ttk


def botones_bebidas_es():
    beb = Tk()
    beb.title("Catalogo de Bebidas")
    beb.geometry("1000x400")
    beb.resizable(False,False)

    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text =" Inca Kola 500ml ").place(x=50, y = 150)
    cocaboton = Button(beb, text =" Coca Kola 500ml ").place(x = 150, y = 150)
    fantaboton = Button(beb, text ="  Fanta  500ml ").place(x= 300, y = 150) 
    gateboton = Button(beb, text =" Gatorade 500ml ").place(x = 450, y= 150)
    voltboton = Button(beb, text ="   Volt 450ml  ").place(x = 600, y= 150)
    pepsiboton = Button(beb, text ="  Pepsi 500ml ").place(x =50, y = 370)
    freeboton = Button(beb, text ="  FreeTea 500ml ").place(x = 150,y =370)
    sanboton = Button(beb, text="  San Luis 625ml ").place(x=300, y=370)
    cieloboton = Button(beb, text ="  Cielo 625ml ").place(x = 450, y = 370)
    sporboton = Button(beb, text="  Sporade  500ml ").place(x= 600, y = 370)

    
    beb.mainloop()






def botones_bebidas_en():
    beb = Tk()
    beb.title("Drinks Catalogue")
    beb.geometry("1000x400")
    beb.resizable(False,False)
    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text = "Inca Kola 500ml ").place(x=50, y = 150)
    cocaboton = Button(beb, text = "Coca Kola 500ml ").place(x = 150, y = 150)
    fantaboton = Button(beb, text = "Fanta 500ml").place(x= 300, y = 150) 
    gateboton = Button(beb, text =" Gatorade 500ml").place(x = 450, y= 150)
    voltboton = Button(beb, text ="   Volt 450ml ").place(x = 600, y= 150)
    pepsiboton = Button(beb, text ="  Pepsi 500ml ").place(x =50, y = 370)
    freeboton = Button(beb, text ="  FreeTea 500ml ").place(x = 150,y =370)
    sanboton = Button(beb, text="  San Luis  625ml ").place(x=300, y=370)
    cieloboton = Button(beb, text ="  Cielo  625ml ").place(x = 450, y = 370)
    sporboton = Button(beb, text="  Sporade  500ml ").place(x= 600, y = 370)
    
    beb.mainloop()

def botones_abarrotes_es():
    aba = Tk()
    aba.title("Catalogo de Abarrotes")
    aba.geometry("1000x400")
    aba.resizable(False,False)
    cantidad = Entry(aba).place(x = 20, y = 30)
    picaboton = Button(aba, text = "Picaras").place(x=50, y = 150)
    laysboton = Button(aba, text = " Lays ").place(x = 150, y = 150)
    dorboton = Button(aba, text = "Doritos").place(x= 300, y = 150) 
    sodboton = Button(aba, text =" Soda Field ").place(x = 450, y= 150)
    iberboton = Button(aba, text ="   Iberica  ").place(x = 600, y= 150)
    subboton = Button(aba, text ="  Sublime  ").place(x =50, y = 370)
    piqboton = Button(aba, text =" Piqueo Snack ").place(x = 150,y =370)
    doñaboton = Button(aba, text="  Doña Pepa  ").place(x=300, y=370)
    cereaboton = Button(aba, text ="  Cereal Bar  ").place(x = 450, y = 370)
    chokisboton = Button(aba, text="  Chokis  ").place(x= 600, y = 370)

    aba.mainloop()

def botones_abarrotes_en():
    aba = Tk()
    aba.title("Groceries Catalogue")
    aba.geometry("1000x400")
    aba.resizable(False,False)
    cantidad = Entry(aba).place(x = 20, y = 30)
    picaboton = Button(aba, text = "Picaras").place(x=50, y = 150)
    laysboton = Button(aba, text = " Lays ").place(x = 150, y = 150)
    dorboton = Button(aba, text = "Doritos").place(x= 300, y = 150) 
    sodboton = Button(aba, text =" Soda Field ").place(x = 450, y= 150)
    iberboton = Button(aba, text ="   Iberica  ").place(x = 600, y= 150)
    subboton = Button(aba, text ="  Sublime  ").place(x =50, y = 370)
    piqboton = Button(aba, text =" Piqueo Snack ").place(x = 150,y =370)
    doñaboton = Button(aba, text="  Doña Pepa  ").place(x=300, y=370)
    cereaboton = Button(aba, text ="  Cereal Bar  ").place(x = 450, y = 370)
    chokisboton = Button(aba, text="  Chokis  ").place(x= 600, y = 370)


    aba.mainloop()    



def botones_congelados_es():
    cong = Tk()
    cong.title("Catalogo de Productos Congelados")
    cong.geometry("1000x400")
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
    cong.geometry("1000x400")
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
    com.geometry("600x300")
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
    com.geometry("600x300")
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
    cui.geometry("900x400")
    cui.resizable(False,False)
    cantidad = Entry(cui).place(x=20,y=30)
    jabon_boton = Button(cui, text = " Jabon Dove ").place(x=50,y=150)
    shamp_boton = Button(cui, text = " H&S Old Spice ").place(x=200,y=150)
    pasta_boton = Button(cui, text = " Pasta de dientes Colgate ").place(x=350,y=150)
    cepi_boton = Button(cui, text = " Cepillo Colgate ").place(x=50,y=370)
    gill_boton = Button(cui, text = " Hoja de afeitar Gillet ").place(x=200,y=370)
    lady_boton = Button(cui, text = " Toallas femeninas LadySoft ").place(x=600,y=370)

    cui.mainloop()



def botones_cuidado_personal_en():
    cui = Tk()
    cui.title("Catalogo de Productos de Cuidado Personal")
    cui.geometry("900x400")
    cui.resizable(False,False)
    cantidad = Entry(cui).place(x=20,y=30)
    jabon_boton = Button(cui, text = " Soap Dove ").place(x=50,y=150)
    shamp_boton = Button(cui, text = " H&S Old Spice ").place(x=200,y=150)
    pasta_boton = Button(cui, text = " Toothpaste Colgate ").place(x=350,y=150)
    cepi_boton = Button(cui, text = " Toothbrush Colgate ").place(x=50,y=370)
    gill_boton = Button(cui, text = " Gillet Razor Blade ").place(x=200,y=370)
    always_boton = Button(cui, text = " Pads Always ").place(x=600,y=370)    

    cui.mainloop()