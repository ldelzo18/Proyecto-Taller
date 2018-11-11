from tkinter import *

def funcion_imprimir(text,carrito):
    text.delete(1.0,END)
    text.insert(1.0,carrito)

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

