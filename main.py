from add_abarrotes import *
from add_bebidas import *
from add_comidapreparada import *
from add_congelados import *
from add_cuidado_personal import *
#=============================================== Variables del Main ======================================================#
lista_Productos = []
lista_Precios = []
#=============================================== funcion imprimir_Menu -==================================================#
def imprimir_Menu():             
    print("Bienvenido al Sistema Market!")
    print("Eliga entre las siguientes opciones:")
    print("1: Agregar producto")
    print("2: Remover producto")
    print("3: Imprimir el total:")
    print("4: Terminar el programa")

    opcion = (int)(input("Ingrese su opcion:"))

    #Opcion 1: Ver productos disponibles
    if opcion == 1:
        while True:
            #Usando funcion imprimir_Categorias
            y = imprimir_Categorias()

            #Si la funcion retorna valor 1: el usuario regresa al menu principal
            if y == 1:
                break
        
    #Opcion 2: Remover producto
    #elif opcion == 2:
    
    #Opcion 3: Imprimir el total
    #elif opcion == 3:

    #Opcion 4: Termina el programa
    elif opcion == 4:
        return 1

#=========================================================================================================================#

#================================================ Funcion imprimir_Categorias ============================================#
def imprimir_Categorias():
    print("1: Bebidas")
    print("2: Abarrotes")
    print("3: Congelados")
    print("4: Cuidado Personal")
    print("5: Comida Preparada")
    print("6: Salir")

    opcionC = (int)(input("Ingrese su opcion:"))

    #Opcion 1: Ir a menu de bebidas
    if opcionC == 1:
        while True:
            z = menu_bebidas()
            
            if z == 1:
                break

    elif opcionC == 6:
        return 1
#=========================================================================================================================#

#=============================================== menu_bebidas ============================================================#
def menu_bebidas():
    print("1: Inka Kola 500 ml")
    print("2: Coca Cola 500 ml")
    print("3: Agua San Luis 500 ml")
    print("4: Agua Cielo 625 ml")
    print("5: Bebida rehidratante Gatorade 500 ml")
    print("6: Salir")

    opcionB = (int)(input("Ingrese el producto que va a agregar a su carrito de compras:"))

    if opcionB == 1:
        add_bebidas(lista_Productos,lista_Precios,0)
        print("El producto inka Kola fue agregado satisfactoriamente!")
        return 1

    elif opcionB == 6:
        return 1
#=========================================================================================================================#

#================================================ Main ===================================================================#
while True:
    x = imprimir_Menu()

    if x == 1:
        break

#==========================================================================================================================#

  

    

    

    
