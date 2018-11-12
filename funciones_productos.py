from otras_Funciones import *
from tkinter import messagebox

def add_Producto(lastWindow,commander,lista_Bebidas,cantidad,cod_producto):
        #==========Atributos========#
        producto_nombre = ''
        #===========================#

        #======Identificando producto por codigo====#
                        #-Bebidas-#
        if cod_producto == 0:#inkakola 
                producto_nombre = "Inka Kola 500 ml"
        elif cod_producto == 1:#cocacola
                producto_nombre = "CocaCola 500 ml"
        elif cod_producto == 2:#Fanta
                producto_nombre = "Fanta 500 ml"
        elif cod_producto == 3:#Gatorade
                producto_nombre = "Gatorade 500 ml"
        elif cod_producto == 4:#Volt
                producto_nombre = "Volt 450 ml"
        elif cod_producto == 5:#Pepsi
                producto_nombre = "Pepsi 500 ml"
        elif cod_producto == 6:#FreeTea
                producto_nombre = "FreeTea 500 ml"
        elif cod_producto == 7:#San Luis
                producto_nombre = "Agua San Luis 625 ml"
        elif cod_producto == 8:#Cielo
                producto_nombre = "Agua Cielo 625 ml"
        elif cod_producto == 9:#Sporade
                producto_nombre = "Sporade 500 ml"
                        #-Abarrotes-#
        elif cod_producto == 10:#Picaras
                producto_nombre = "Galleta Picaras"
        elif cod_producto == 11:#Lays
                producto_nombre = "Papas Lays" 
        elif cod_producto == 12:#Doritos
                producto_nombre = "Doritos"
        elif cod_producto == 13:#SodField
                producto_nombre = "Galleta SodaField"                               
        elif cod_producto == 14:#iberica
                producto_nombre = "Chocolate Iberica"
        elif cod_producto == 15:#sublime
                producto_nombre = "Chocolate Sublime"
        elif cod_producto == 16:#piqueosnack
                producto_nombre = "Piqueo Snack"
        elif cod_producto == 17:#doñapepa                
                producto_nombre = "Doña Pepa"
        elif cod_producto == 18:#cerealbar
                producto_nombre = "Barra energetica Cereal bar"
        elif cod_producto == 19:#chokis
                producto_nombre = "Galleta Chokis"
                        #-Congelados-#
        elif cod_producto == 20:#Donofrio Lucuma
                producto_nombre = "Donofrio Lucuma 1L"        
        elif cod_producto == 21:#Nestle Beso de moza
                producto_nombre = "Nestle beso de moza 1L"
        elif cod_producto == 22:#NestleMorochas
                producto_nombre = "Nestle morochas 1L"
        elif cod_producto == 23:#Donofrio Tornado Lucuma      
                producto_nombre = " Donofrio Tornado Lucuma 1L"
        elif cod_producto == 24:#Donofrio Tornado Vainilla
                producto_nombre = "Donofrio Tornado Vainilla 1L"
        elif cod_producto == 25:#Nuggets
                producto_nombre = "San Fernando 15 Nuggets"
        elif cod_producto == 26:#Hamburguesas
                producto_nombre = "San Fernando 6 hamburguesas"        
        elif cod_producto == 27:#PizzaPeperoni
                producto_nombre = "Pizza Peperoni"
        elif cod_producto == 28:#PizzaAmericana
                producto_nombre = "Pizza Americana"
        elif cod_producto == 29:#Ravioles                
                producto_nombre = "Pack de Ravioles"
                        #-ComidaPreparada-#                
        elif cod_producto == 30:#HamburguesaCarne
                producto_nombre = "Hamburguesa de carne"
        elif cod_producto == 31:#Hamburguespollo
                producto_nombre = "Hamburguesa de pollo"
        elif cod_producto == 32:#Empanadacarne
                producto_nombre = "Empanada de carne"                
        elif cod_producto == 33:#Empanadapollo
                producto_nombre = "Empanada de pollo"
        elif cod_producto == 34:#Pollofrito
                producto_nombre = "Pollo frito"
        elif cod_producto == 35:#Wrappollo
                producto_nombre = "Wrap de pollo"
        elif cod_producto == 36:#Wrapcarne
                producto_nombre = "Wrap de carne"        
        elif cod_producto == 37:#Choripan
                producto_nombre = "Choripan"
        elif cod_producto == 38:#Siumay
                producto_nombre = "Siu May"
        elif cod_producto == 39:#Minpao
                producto_nombre = "Min Pao"
                        #-CuidadoPersonal-#
        elif cod_producto == 40:#Dove
                producto_nombre = "Jabon Dove"                
        elif cod_producto == 41:#H&S
                producto_nombre = "Shampoo H&S Old Spice"
        elif cod_producto == 42:#Colgate
                producto_nombre = "Pasta dental Colgate"
        elif cod_producto == 43:#Colgate2
                producto_nombre = "Cepillo dental Colgate"
        elif cod_producto == 44:#Gillet
                producto_nombre = "Hoja de afeitar gillete"
        elif cod_producto == 45:#LadySoft        
                producto_nombre = "Toallas femeninas LadySoft"
        elif cod_producto == 46:#Listerine
                producto_nombre = "Enjuague Bucal Listerine 500ml"
        elif cod_producto == 47:#Dento
                producto_nombre = "Pasta dental Dento"        
        elif cod_producto == 48:#Gillete2
                producto_nombre = "Crema de afeitar Gillete"
        else:#H&S2
                producto_nombre = "Shampoo H&S de menta 375ml"
        #===============Fin de identificacion========#

        #===========Agregando valor===================#
        if cantidad.get() != "":#Si el valor del entry(cantidad) no se encuentra vacia

                
                try:#Aplicando excepciones en caso que el valor guardado en cantidad no pueda ser convertido a entero
                        temporal_int = int(cantidad.get())
                        agregar_Lista(lista_Bebidas,producto_nombre,temporal_int)#Agregando producto al carrito
                        messagebox.showinfo("Aviso","Se ingreso el producto satisfactoriamente!")#Mostrando verificacion de proceso como aviso
                        lastWindow.lift()#Forzar a ventana interfaz_Es a estar al frente
                        commander.destroy()#Cerrar la ventana actual

                except:#En caso de error en el valor de cantidad
                        messagebox.showerror("Error","La cantidad ingresa no es valida!")
                        lastWindow.lift()#Forzar a ventana interfaz_Es a estar al frente
                        commander.destroy()#Cerrar la ventana actual

        #=============================================#
        else:#Si el valor del entry(cantidad) se encuentra vacia
                messagebox.showerror("Error","No ha ingresado cantidad!")
                commander.lift()#Mantener al frente la ventana actual




        

        

        
