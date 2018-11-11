def encontrar_posicion_Producto(lista,producto):
    temp = 0
    if len(lista) !=0:
        for x in range(len(lista)):
            if lista[x][0] == producto:
                temp = x
        return temp

    return None

def agregar_Lista(lista,nombre_producto,cantidad):
    
    if len(lista) == 0:#Si la lista esta vacia
        lista.append([nombre_producto,cantidad])
    else:#Si la lista ya contiene algun valor
        posicion = encontrar_posicion_Producto(lista,nombre_producto)
        if posicion == None:
            lista.append([nombre_producto,cantidad])
        else:
            lista[posicion][1] += cantidad

