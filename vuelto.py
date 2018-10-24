def vuelto (total ):
    total= int(input("Ingrese el pago"))
    
    billete_10 = 0
    billete_20 = 0 
    billete_50 = 0 
    billete_100 = 0 
    billete_200 = 0

    if total % 10 == 0 :
        billete_10 = total / 10 
    elif total % 20 == 0 :
        billete_20 = total / 20
    elif total % 50 == 0 :
        billete_50 = total / 50
    elif total % 100 == 0 :
        billete_100 = total / 100
    elif total % 200 == 0 :
        billete_200 = total / 200 

    print(billete_10)
    print(billete_20)
    print(billete_50)
    print(billete_100)
    print(billete_200) 

    
    
    








    