def pagoDebito(total):
    #Se cobra el 5% del total de la transaccion
    porcentajeDeCobro = total * 0.5
    nuevoTotal = total + porcentajeDeCobro
    return nuevoTotal

def cambiarDolares(soles):
    #La tasa de cambio del dollar es 1dollar = 3.33 soles
    tasa_de_Cambio = 3.33
    cambio  = (soles * 3.33)*1.00
    return cambio

