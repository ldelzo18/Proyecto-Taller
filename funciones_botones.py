from tkinter import *
from tkinter import ttk


def botones_bebidas_es():
    beb = Tk()
    beb.title("Catalogo de Bebidas")
    beb.geometry("1000x400")
    beb.resizable(False,False)

    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text =" Inca Kola").place(x=50, y = 150)
    cocaboton = Button(beb, text =" Coca Kola").place(x = 150, y = 150)
    fantaboton = Button(beb, text ="  Fanta  ").place(x= 300, y = 150) 
    gateboton = Button(beb, text =" Gatorade ").place(x = 450, y= 150)
    voltboton = Button(beb, text ="   Volt   ").place(x = 600, y= 150)
    pepsiboton = Button(beb, text ="  Pepsi  ").place(x =50, y = 370)
    freeboton = Button(beb, text ="  FreeTea ").place(x = 150,y =370)
    sanboton = Button(beb, text="  San Luis  ").place(x=300, y=370)
    cieloboton = Button(beb, text ="  Cielo  ").place(x = 450, y = 370)
    sporboton = Button(beb, text="  Sporade  ").place(x= 600, y = 370)

    
    beb.mainloop()






def botones_bebidas_en():
    beb = Tk()
    beb.title("Drinks Catalogue")
    beb.geometry("1000x400")
    beb.resizable(False,False)
    cantidad = Entry(beb).place (x=20, y=30)
    inkaboton = Button(beb, text = "Inca Kola").place(x=50, y = 150)
    cocaboton = Button(beb, text = "Coca Kola").place(x = 150, y = 150)
    fantaboton = Button(beb, text = "Fanta").place(x= 300, y = 150) 
    gateboton = Button(beb, text =" Gatorade ").place(x = 450, y= 150)
    voltboton = Button(beb, text ="   Volt   ").place(x = 600, y= 150)
    pepsiboton = Button(beb, text ="  Pepsi  ").place(x =50, y = 370)
    freeboton = Button(beb, text ="  FreeTea ").place(x = 150,y =370)
    sanboton = Button(beb, text="  San Luis  ").place(x=300, y=370)
    cieloboton = Button(beb, text ="  Cielo  ").place(x = 450, y = 370)
    sporboton = Button(beb, text="  Sporade  ").place(x= 600, y = 370)
    
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
    cong.tittle("Catalogo de Productos Congelados")    
    cong.geometry("1000x400")
    cong.resizable(False,False)
    cantidad = Entry(cong).place(x=20,y=30)
    luboton = Button(cong, text = "Donofrio Lucuma 1L").place(x=50, y = 150)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ").place(x = 150, y = 150)
    moroboton = Button(cong, text = "Nestle morochas 1L").place(x= 300, y = 150) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ").place(x = 450, y= 150)
    torvaboton = Button(cong, text ="   Donofrio Tornado Vainilla 1L ").place(x = 600, y= 150)
    nuggboton = Button(cong, text ="  San Fernando pack de 15 und Nuggets ").place(x =50, y = 370)
    hamboton = Button(cong, text =" San Fernando 6 und de hamburguesas ").place(x = 150,y =370)
    pizzpboton = Button(cong, text="  Pizza Peperoni  ").place(x=300, y=370)
    pizzamboton = Button(cong, text ="  Pizza Americana  ").place(x = 450, y = 370)
    raviboton = Button(cong, text="  Pack de ravioles ").place(x= 600, y = 370)    

    cong.mainloop()






def botones_congelados_en():
    cong = Tk()
    cong.tittle("Frozen products Catalogue")    
    cong.geometry("1000x400")
    cong.resizable(False,False)
    cantidad = Entry(cong).place(x=20,y=30)
    luboton = Button(cong, text = "Donofrio Lucuma 1L").place(x=50, y = 150)
    nesboton = Button(cong, text = " Nestle beso de moza 1L ").place(x = 150, y = 150)
    moroboton = Button(cong, text = "Nestle morochas 1L").place(x= 300, y = 150) 
    torluboton = Button(cong, text =" Donofrio Tornado Lucuma 1L ").place(x = 450, y= 150)
    torvaboton = Button(cong , text = " Donofrio Tornado Vainilla 1L ").place(x = 600, y= 150)
    nuggboton = Button(cong, text ="  San Fernando 15 units Nuggets ").place(x =50, y = 370)
    hamboton = Button(cong, text =" San Fernando 6 units hamburgers").place(x = 150,y =370)
    pizzpboton = Button(cong, text="  Pizza Peperoni  ").place(x=300, y=370)
    pizzamboton = Button(cong, text ="  Pizza Americana  ").place(x = 450, y = 370)
    raviboton = Button(cong, text=" Ravioles Pack ").place(x= 600, y = 370)    

    cong.mainloop()