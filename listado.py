
contador_incacola = 0
contador_cocacola = 0
contador_volt = 0
contador_gaterode = 0
contador_sporade = 0
contador_fanta = 0

nombre_producto =["Inca Kola" , "Volt" , "Coca Cola" , "Fanta" , "gaterode"]
precio_correspondiente = [2.45 , 3.00 , 2.45 , 3.00 , 4.00]


while True :
        seleccion =  input ("Seleccione \n1=Bebidas \n2=Galletas\n" )
        if (seleccion == "1"):
                while True :
                        seleccion_bebidas = input("Seleccione \n 1=Gaseosa \n 2=Bedidas Energeticas \n 3=Vino \n")

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
                                        seleccion_bebidas_energetica = input("Seleccione las marcas disponible  \n 1=Volt 330ml \n 2=Gaterode \n 3=Sporade \n")
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
                                                       
                        
                                        break
                        break

        if (contador_gaterode >= 1 ):
                print ("Cantidad :" , contador_gaterode ,"Nombre" ,nombre_producto[4] ,"Precio por unidad",precio_correspondiente[4])
        if (contador_cocacola >= 1) :
                print ("Cantidad :" , contador_cocacola ,"Nombre" ,nombre_producto[2] ,"Precio por unidad",precio_correspondiente[0] )
        if (contador_incacola >= 1) :
                print ("Cantidad :" , contador_incacola ,"Nombre" ,nombre_producto[0] ,"Precio por unidad",precio_correspondiente[0] )
        if (contador_volt >= 1) :
                print ("Cantidad :" , contador_volt , "Nombre" , nombre_producto[1] ,"Precio por unidad" , precio_correspondiente[1])
        if (contador_fanta >= 1 ):
                print("Cantidad :" , contador_fanta , "Nombre" , nombre_producto[3] ,"Precio por unidad" , precio_correspondiente[3])
        


        decision =  input ("Desea continuar Si o No \n")
        if ( decision == "No"):
                print ("gracias ;)") 
                break  

##print("cantidad de sporade " , contador_sporade)
       ### print ("cantidad de gaterode " , contador_gaterode)
       # print ("cantidad de cocacola " ,contador_cocacola)
       # print ("cantidad de inca cola " 
          
