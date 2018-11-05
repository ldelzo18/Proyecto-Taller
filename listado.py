
def xd () :     
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

        contador_picaras = 0
        contador_lay = 0
        contador_doritos = 0
        contador_soda_field = 0 
        contador_iberica = 0
        contador_sublime = 0
        contador_piqueo = 0
        contador_doña_pepa = 0
        contador_cereal_bar = 0
        contador_chokis = 0
        monto_total = 0


        precio_incacola = 0
        precio_cocacola = 0
        precio_fanta = 0
        precio_gaterode = 0
        precio_volt = 0
        precio_sporade = 0
        precio_freetea = 0
        precio_san_mateo = 0
        precio_cielo = 0

        precio_picaras = 0
        precio_lay = 0
        precio_doritos = 0
        precio_soda_field = 0
        precio_iberica = 0
        precio_sublime = 0
        precio_piqueo = 0
        precio_doña_pepa = 0
        precio_cereal_bar = 0
        precio_chokis = 0

        #Lista Bebidas energetica
        bebidas_energetica =["Gaterode 500 ml " ,"Volt 330 ml" , "FreeTea" , "Sporade"]
        precio_bebidas_energetica = [2.50 , 3.00 , 3.50 , 4.00]
        #Lista Gaseosa
        Gaseosa_producto =["Coca Cola 450 ml " , "Inca Cola 450 ml" , "Fanta 400 ml" , "Pepsi 500 ml"]
        Precio_Gaseosa = [2.45 , 2.45 , 3.00 , 1.80]
        #Lista agua
        agua_producto =["San Mateo 450 ml" , "Cielo 620 ml"]
        precio_agua = [3.50 , 2.00]
        #Lista galletas
        galleta_producto =["Picaras" , "Lays" , "Doritos" , "Soda Field" , "Iberica" , "Sublime" , "Piqueo Snacks" , "Doña Pepa " , "Cereal Bar" , "Chokis"]
        galleta_precio = [1.40 , 1.00 , 1.00 , 0.60 , 1.20 , 1.00 , 1.20 , 0.70 , 1.00 , 1.30]

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
                                                seleccion_bebidas_energetica = input("Seleccione las marcas disponible  \n 1=Volt 330ml \n 2=Gaterode \n 3=Sporade \n 4=FreeTea  \n")
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

                if (seleccion == "2"):
                        while True :
                                seleccion_galletas = input ("Seleccione lo que tenemos disponible \n 1=Picaras \n 2=Lays \n 3=Doritos \n 4=Soda Field \n 5=Iberica \n 6=Sublime \n 7=Piqueo Snack \n 8=Doña pepa \n 9=Cereal Bar \n 10= Chokis \n")
                                if (seleccion_galletas == "1") :
                                        cantidad_picaras = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_picaras) :
                                                contador_picaras += 1
                                        break
                                if(seleccion_galletas == "2"):
                                        cantidad_lay = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_lay) :
                                                contador_lay += 1
                                        break
                                if(seleccion_galletas == "3"):
                                        cantidad_doritos = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_doritos) :
                                                contador_doritos += 1
                                        break
                                if(seleccion_galletas == "4"):
                                        cantidad_soda_field= int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_soda_field) :
                                                contador_soda_field += 1
                                        break
                                if(seleccion_galletas == "5"):
                                        cantidad_iberica = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_iberica) :
                                                contador_iberica += 1
                                        break
                                if(seleccion_galletas == "6"):
                                        cantidad_sublime = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_sublime) :
                                                contador_sublime += 1
                                        break
                                if(seleccion_galletas == "7"):
                                        cantidad_piqueo = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_piqueo) :
                                                contador_piqueo += 1
                                        break
                                if(seleccion_galletas == "8"):
                                        cantidad_doña_pepa = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_doña_pepa) :
                                                contador_doña_pepa += 1
                                        break
                                if(seleccion_galletas == "9"):
                                        cantidad_cereal_bar = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_cereal_bar) :
                                                contador_cereal_bar += 1
                                        break
                                if(seleccion_galletas == "10"):
                                        cantidad_chokis = int(input("Seleccione cuantas deseas llevar \n"))
                                        for i in range (cantidad_chokis) :
                                                contador_chokis += 1
                                        break
                        break


                #Gaseosas
                if (contador_incacola >= 1) :
                        print ("Cantidad :" , contador_incacola ,"Nombre" ,Gaseosa_producto[1] ,"Precio por unidad",Precio_Gaseosa[1] )
                        precio_incacola = contador_incacola*Precio_Gaseosa[1]
                
                if (contador_cocacola >= 1) :
                        print ("Cantidad :" , contador_cocacola ,"Nombre" ,Gaseosa_producto[0] ,"Precio por unidad",Precio_Gaseosa[0] )
                        precio_cocacola = contador_cocacola*Precio_Gaseosa[0]
                
                if (contador_fanta >= 1 ):
                        print("Cantidad :" , contador_fanta , "Nombre" , Gaseosa_producto[2] ,"Precio por unidad" , Precio_Gaseosa[2])
                        precio_fanta = contador_fanta*Precio_Gaseosa[2]
                
                
                 #Bebidas Energizantes
                if (contador_gaterode >= 1 ):
                        print ("Cantidad :" , contador_gaterode ,"Nombre" ,bebidas_energetica[0] ,"Precio por unidad",precio_bebidas_energetica[0])
                        precio_gaterode = contador_gaterode*precio_bebidas_energetica[0]
                if (contador_volt >= 1) :
                        print ("Cantidad :" , contador_volt , "Nombre" , bebidas_energetica[1] ,"Precio por unidad" , precio_bebidas_energetica[1])
                        precio_volt = contador_volt*precio_bebidas_energetica[1]
                if (contador_freetea >= 1 ):
                        print("Cantidad :" , contador_freetea , "Nombre" , bebidas_energetica[2] ,"Precio por unidad" , precio_bebidas_energetica[2])
                        precio_freetea = contador_freetea*precio_bebidas_energetica[2]
                if (contador_sporade >= 1 ):
                        print("Cantidad :" , contador_sporade , "Nombre" , bebidas_energetica[3] ,"Precio por unidad" , precio_bebidas_energetica[3])
                        precio_sporade = contador_sporade*precio_bebidas_energetica[3]
        
                # Agua
                if (contador_san_mateo >= 1 ):
                        print("Cantidad :" , contador_san_mateo , "Nombre" , agua_producto[0] ,"Precio por unidad" , precio_agua[0])
                        precio_san_mateo= contador_san_mateo*precio_agua[0]
                
                if (contador_cielo >= 1 ):
                        print("Cantidad :" , contador_cielo , "Nombre" , agua_producto[1] ,"Precio por unidad" , precio_agua[1])
                        precio_cielo =contador_cielo*precio_agua[1]
              

                #Galleta
                if (contador_picaras >= 1 ):
                        print("Cantidad :" , contador_picaras , "Nombre" , galleta_producto[0] ,"Precio por unidad" , galleta_precio[0])
                        precio_picaras = contador_picaras*galleta_precio[0]
                if (contador_lay >= 1 ):
                        print("Cantidad :" , contador_lay, "Nombre" , galleta_producto[1] ,"Precio por unidad" , galleta_precio[1])
                        precio_lay= contador_lay*galleta_precio[1]
                if (contador_doritos >= 1 ):
                        print("Cantidad :" , contador_san_mateo , "Nombre" , galleta_producto[2] ,"Precio por unidad" , galleta_precio[2])
                        precio_doritos=contador_doritos*galleta_precio[2]
                if (contador_soda_field >= 1 ):
                        print("Cantidad :" , contador_soda_field , "Nombre" , galleta_producto[3] ,"Precio por unidad" , galleta_precio[3])
                        precio_soda_field = contador_soda_field*galleta_precio[3]
                
                if (contador_iberica >= 1 ):
                        print("Cantidad :" , contador_iberica , "Nombre" , galleta_producto[4] ,"Precio por unidad" , galleta_precio[4])
                        precio_iberica = contador_iberica*galleta_precio[4]
                
                if (contador_sublime >= 1 ):
                        print("Cantidad :" , contador_sublime  , "Nombre" , galleta_producto[5] ,"Precio por unidad" , galleta_precio[5])
                        precio_sublime = contador_sublime*galleta_precio[5]
                
                if (contador_piqueo >= 1 ):
                        print("Cantidad :" , contador_piqueo , "Nombre" , galleta_producto[6] ,"Precio por unidad" , galleta_precio[6])
                        precio_piqueo = contador_piqueo*galleta_precio[6]
                
                if (contador_doña_pepa >= 1 ):
                        print("Cantidad :" , contador_doña_pepa , "Nombre" , galleta_producto[7] ,"Precio por unidad" , galleta_precio[7])
                        precio_doña_pepa = contador_doña_pepa*galleta_precio[7]
                
                if (contador_cereal_bar >= 1 ):
                        print("Cantidad :" , contador_cereal_bar , "Nombre" , galleta_producto[8] ,"Precio por unidad" , galleta_precio[8])
                        precio_cereal_bar = contador_cereal_bar*galleta_precio[8]
                
                if (contador_chokis >= 1 ):
                        print("Cantidad :" , contador_chokis  , "Nombre" , galleta_producto[9] ,"Precio por unidad" , galleta_precio[9])
                        precio_chokis = contador_chokis*galleta_precio[9]
                
                #total
                monto_total = precio_incacola + precio_cocacola + precio_fanta + precio_volt + precio_gaterode + precio_freetea + precio_sporade + precio_san_mateo + precio_cielo + precio_picaras + precio_lay + precio_doritos + precio_soda_field + precio_iberica + precio_sublime + precio_piqueo + precio_doña_pepa + precio_cereal_bar + precio_chokis 
          
                decision =  input ("Desea continuar Si o No \n")
                if ( decision == "No"):
                        print ("monto total",monto_total)
                        break





