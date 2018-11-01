
#Entrada
def vuelto ():
    while True :
        monto_total= float(input("Ingrese el monto "))
        # El monto total deve ser positivo
        if monto_total >= 0 :
            break

    #Billetes
    billete_10 = 0 
    billete_20 = 0
    billete_50 = 0
    billete_100 = 0
    billete_200 = 0

    #Monedas
    moneda_5 = 0
    moneda_2 = 0 
    moneda_1 = 0 
    monedad_50centavos = 0 
    moneda_20centavos = 0
    moneda_10centavos = 0

    #Billete de 200 soles
    billete_200 = (int(monto_total/200))
    monto_total = monto_total - 200 * billete_200

    #Billete de 100 soles
    billete_100 = (int(monto_total/100))
    monto_total = monto_total - 100 * billete_100

    #Billete de 50 soles
    billete_50 = (int(monto_total/50))
    monto_total = monto_total - 50 * billete_50

    #Billete de 20 soles
    billete_20 = (int(monto_total/20))
    monto_total = monto_total - 20 * billete_20
    
    #Billete de 10 soles
    billete_10 = (int(monto_total/10))
    monto_total = monto_total - 10 * billete_10

    #Moneda de 5 soles
    moneda_5 = (int(monto_total / 5 ))
    monto_total = monto_total - 5 * moneda_5

    #Moneda de 2 soles
    moneda_2 = (int(monto_total / 2 ))
    monto_total = monto_total - 2 * moneda_2
    #Moneda de 1 sol
    moneda_1 = (int(monto_total / 1 ))
    monto_total = monto_total - 1 * moneda_1
    #Moneda de 50 centavos = 0.50 soles
    moneda_50centavos = (int(monto_total / 0.50 ))
    monto_total = monto_total - 0.50 * moneda_50centavos
    #Moneda de 20 centavos = 0.20 soles
    moneda_20centavos = (int(monto_total / 0.20 ))
    monto_total = monto_total - 0.20 * moneda_20centavos
    #Moneda de 10 centavos = 0.10 soles
    moneda_10centavos = (int(monto_total / 0.10 ))
    monto_total = monto_total - 0.10 * moneda_10centavos

    print("Cantidad de S/ 200" , billete_200)
    print("Cantidad de S/ 100" , billete_100)
    print("Cantidad de S/ 50 " , billete_50)
    print("Cantidad de S/ 20 " , billete_20)
    print("Cantidad de S/ 10 " , billete_10)
    print("Cantidad de S/ 5 "  , moneda_5)
    print("Cantidad de S/ 2 "  , moneda_2)
    print("Cantidad de S/ 1 "  , moneda_1)
    print("Cantidad de 50 centavos" , moneda_50centavos)
    print("Cantidad de 20 centavos" , moneda_20centavos)
    print("Cantidad de 10 centavos" , moneda_10centavos)

vuelto()
print("Gracias por la compra")







    
    

    
    








    