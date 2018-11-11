from otras_Funciones import *

def add_Producto(commander,lista_Bebidas,cantidad,cod_producto):
        #==========Atributos========#
        producto_nombre = ''
        #===========================#

        #======Identificando producto por codigo====#
        if cod_producto == 0:#inkakola 
                producto_nombre = "Inka Kola 500 ml"
        elif cod_producto == 1:#cocacola
                producto_nombre = "CocaCola 5000 ml"
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
        else:#Sporade
                producto_nombre = "Sporade 500 ml"
        #===============Fin de identificacion========#

        #===========Agregando valor===================#
        if cantidad.get() != "":
                temporal_int = int(cantidad.get())
                agregar_Lista(lista_Bebidas,producto_nombre,temporal_int)
        #=============================================#

        commander.destroy()




        

        

        
