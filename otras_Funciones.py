from tkinter import *
from funciones_mysql import * 

def funcion_imprimir(text,carrito):

    if len(carrito) != 0:#SOLO IMPRIMIR BOLETA SI ES QUE EL CARRITO TIENE ALGUN PRODUCTO
        monto = 0
        temp = "******************** SUPERMARKET***********************\n"
        temp += "******************Boleta de Venta*********************\n\n"
        temp += '{:<30s}{:>10s}{:^22s}{:>8s}'.format("PRODUCTO","CANTIDAD","PRECIO UNITARIO","PRECIO TOTAL")
        temp += '\n-------------------------------------------------------------------------'
    
        for x in range(len(carrito)):
            producto = carrito[x][0]#String que indica el nombre del producto
            cantidad = str(carrito[x][1])#String que indica la cantida del producto en el carrito
            precio_unitario = str(retornar_precio(carrito[x][0]))#Precio unitario recuperado de base de datos lista_precios
            precio_total = str(retornar_precio(carrito[x][0])*carrito[x][1])#Precio total del producto
            monto += retornar_precio(carrito[x][0])*carrito[x][1]#Sumando total del producto a la variable monto

            temp += "\n"+'{:<30s}{:>10s}{:^22s}{:>8s}'.format(producto,cantidad,precio_unitario,precio_total)


        temp += '\n-------------------------------------------------------------------------'
        temp += '\n{:<20s}{:>5s}'.format("TOTAL A PAGAR:",str(monto))
        temp += '\n{:<20s}{:>5s}'.format("IGV - 18%:",str(monto*0.18))
        temp += '\n{:<20s}{:>5s}'.format("IMPORTE TOTAL:",str(monto))
        
        text.delete(1.0,END)
        text.insert(1.0,temp)

    else:#SI EL CARRITO ESTA VACIO
        text.delete(1.0,END)
        text.insert(1.0,"EL CARRITO ESTA VACIO!")

def encontrar_posicion_Producto(lista,producto):
    for x in range(0,len(lista)):
        if lista[x][0] == producto:#Si el producto ya se encuentra en la lista
            return x
            
    return -1

def agregar_Lista(lista,nombre_producto,cantidad):
    
    if len(lista) == 0:#Si la lista esta vacia
        lista.append([nombre_producto,cantidad])
    else:#Si la lista ya contiene algun valor
        posicion = encontrar_posicion_Producto(lista,nombre_producto)
        if posicion == -1:
            lista.append([nombre_producto,cantidad])
        else:
            lista[posicion][1] += cantidad

