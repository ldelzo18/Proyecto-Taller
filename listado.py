igv = 1.18
cantidad  = []
contador_incacola = 0


while True :
        seleccion =  input ("Seleccione \n 1=Bebidas \n 2=Galletas " )
        if (seleccion == "1"):
                while True :
                        seleccion_bebidas = input("Seleccione \n 1=Gaseosa \n 2=Bedidas Energeticas \n 3=Vino ")
                        if (seleccion_bebidas == "1") :
                                while True :
                                        seleccion_gaseosa = input("Seleccione las marcas que tenemos \n 1=Inca Cola 450 ml \n 2=Coca Cola 450 ml")
                                        if (seleccion_gaseosa == "1"):
                                                cantidad_incacola = int(input("seleccione cuantas deseas llevar"))
                                                precio_inca_cola = 2.45
                                                precio_completo_inca_kola = precio_inca_cola * igv * cantidad_incacola
                                                for i in range (cantidad_incacola) :
                                                        contador_incacola += 1
                                                        cantidad.append(i)
                                                
                                                break        



                                        if (seleccion_gaseosa == "2"):
                                                precio_coca_cola = 2.45
                                                precio_completo_coca_cola = precio_coca_cola * igv * cantidad
                                                break
                                        break
                        break

        
        print (contador_incacola)
        decision =  input ("Desea continuar Si o No")
        if ( decision == "No"):
                print ("gracias ;)") 
                break  


          


              
        



                     
        
                        
                        

                
                        




    
                
        
