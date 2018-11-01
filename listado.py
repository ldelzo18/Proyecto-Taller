
contador_incacola = 0
contador_cocacola = 0
contador_fanta = 0
contador_pepsi = 0 

contador_volt = 0
contador_gaterode = 0
contador_sporade = 0
contador_freetea = 0

contador_san_mateo = 0
contador_cielo = 0

#Lista Bebidas energetica
bebidas_energetica =["Gaterode 500 ml " ,"Volt 330 ml" , "FreeTea" , "Sporade"]
precio_bebidas_energetica = [2.50 , 3.00 , 3.50 , 4.00]
#Lista Gaseosa
Gaseosa_producto =["Coca Cola 450 ml " , "Inca Cola 450 ml" , "Fanta 400 ml" , "Pepsi 500 ml"]
Precio_Gaseosa = [2.45 , 2.45 , 3.00 , 1.80]
#Lista agua
agua_producto =["San Mateo 450 ml" , "Cielo 620 ml"]
precio_agua = [3.50 , 2.00]

while True :
        seleccion =  input ("Seleccione \n1=Bebidas \n2=Galletas\n" )
        if (seleccion == "1"):
                while True :
                        seleccion_bebidas = input("Seleccione \n 1=Gaseosa \n 2=Bedidas Energeticas \n 3=Bebidas(agua) \n")

                        if (seleccion_bebidas == "1") :
                                while True :
                                        seleccion_gaseosa = input("Seleccione las marcas que tenemos \n 1=Inca Cola 450 ml \n 2=Coca Cola 450 ml \n 3=Fanta 400ml ")
                                        if (seleccion_gaseosa == "1"):
                                                cantidad_incacola = int(input("seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_incacola) :
                                                        contador_incacola += 1 
                                                break      

                                        if (seleccion_gaseosa == "2"):
                                                cantidad_cocacola = int(input("seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_cocacola) :
                                                        contador_cocacola += 1     
                                                break

                                        if (seleccion_gaseosa == "3"):
                                                cantidad_fanta = int(input("seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_fanta) :
                                                        contador_fanta += 1 
                                                break


                        if (seleccion_bebidas == "2") :
                                while True :
                                        seleccion_bebidas_energetica = input("Seleccione las marcas disponible  \n 1=Volt 330ml \n 2=Gaterode \n 3=Sporade \n 4=FreeTea \n")
                                        if(seleccion_bebidas_energetica == "1"):
                                                cantidad_volt = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_volt):
                                                        contador_volt += 1
                                                break

                                        if(seleccion_bebidas_energetica == "2"):
                                                cantidad_gaterode = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_gaterode):
                                                        contador_gaterode += 1
                                                break

                                        if(seleccion_bebidas_energetica == "3"):
                                                cantidad_sporade = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_sporade):
                                                        contador_sporade += 1
                                                break

                                        if(seleccion_bebidas_energetica == "4"):
                                                cantidad_freetea = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_freetea):
                                                        contador_freetea += 1
                                                break
                        if (seleccion_bebidas == "3"):
                                while True :
                                        seleccion_agua = input("Seleccione las marcas disponible  \n 1=San Mateo \n 2=Cielo \n")
                                        if(seleccion_agua == "1"):
                                                cantidad_san_mateo = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range (cantidad_san_mateo):
                                                        contador_san_mateo += 1
                                                break
                                        if(seleccion_agua == "2"):
                                                cantidad_cielo = int(input("Seleccione cuantas deseas llevar \n"))
                                                for i in range ( cantidad_cielo) :
                                                        contador_cielo +=1
                                        break
                        break

        if (contador_gaterode >= 1 ):
                print ("Cantidad :" , contador_gaterode ,"Nombre" ,bebidas_energetica[0] ,"Precio por unidad",precio_bebidas_energetica[0])
        if (contador_cocacola >= 1) :
                print ("Cantidad :" , contador_cocacola ,"Nombre" ,Gaseosa_producto[0] ,"Precio por unidad",Precio_Gaseosa[0] )
        if (contador_incacola >= 1) :
                print ("Cantidad :" , contador_incacola ,"Nombre" ,Gaseosa_producto[1] ,"Precio por unidad",Precio_Gaseosa[1] )
        if (contador_volt >= 1) :
                print ("Cantidad :" , contador_volt , "Nombre" , bebidas_energetica[1] ,"Precio por unidad" , precio_bebidas_energetica[1])
        if (contador_fanta >= 1 ):
                print("Cantidad :" , contador_fanta , "Nombre" , Gaseosa_producto[2] ,"Precio por unidad" , Precio_Gaseosa[2])
        if (contador_freetea >= 1 ):
                print("Cantidad :" , contador_freetea , "Nombre" , bebidas_energetica[2] ,"Precio por unidad" , precio_bebidas_energetica[2])
        if (contador_sporade >= 1 ):
                print("Cantidad :" , contador_sporade , "Nombre" , bebidas_energetica[3] ,"Precio por unidad" , precio_bebidas_energetica[3])
        if (contador_san_mateo >= 1 ):
                print("Cantidad :" , contador_san_mateo , "Nombre" , agua_producto[0] ,"Precio por unidad" , precio_agua[0])
        if (contador_cielo >= 1 ):
                print("Cantidad :" , contador_cielo , "Nombre" , agua_producto[1] ,"Precio por unidad" , precio_agua[1])
        
        


        decision =  input ("Desea continuar Si o No \n")
        if ( decision == "No"):
                print ("gracias ;)") 
                break  

