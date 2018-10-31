
contador_incacola = 0
contador_cocacola = 0


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
                                                for i in range (cantidad_incacola) :
                                                        contador_incacola += 1
                                                        
                                                
                                                break        
                                        if (seleccion_gaseosa == "2"):
                                                cantidad_cocacola = int(input("seleccione cuantas deseas llevar"))
                                                for i in range (cantidad_cocacola) :
                                                        contador_cocacola += 1
                                                        
                                                break
                                        break
                        break

        
        print (contador_incacola)
        decision =  input ("Desea continuar Si o No")
        if ( decision == "No"):
                print ("gracias ;)") 
                break  


          


              
        



<<<<<<< HEAD
                     
        
                        
                        

                
                        




    
                
        
=======
if gaseosa[3] == '7up':
        print ("El precio es de 5.50 soles")
>>>>>>> 843924063ea354534eed39e5720acece3d2aa1b2
