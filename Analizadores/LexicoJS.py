
def ValidarSimbolo(caracter):
    varascii= ord(caracter)

    if varascii>=65 and varascii<=90 or varascii>=97 and varascii<=122 :
        return 1 #Letras
    elif varascii>= 48 and varascii<=57: 
        return 2 #numeros
    elif varascii== 42 :
        return 3 # * asterisco   
    elif varascii== 47 :
        return 4 # / diagonal
    elif varascii== 92 :
        return 4 # \ diagonal       
    elif varascii==39 or varascii==37 or varascii==61 or varascii==59 or varascii==62 or varascii==60 or varascii==40 or varascii==41 or varascii==125 or varascii==123 or varascii==43 or varascii==45  or varascii==46 or varascii==44 or varascii==33 or varascii==38 or varascii==124 :
        return 5 #simbolos ' % = ; > < ( ) } { + - . , ! & |   
    elif  varascii>=0 and varascii<=32 :
        return 6 #controles de linea  
    else: 
        return 0




def Analizar(cadena):
    indice=0
    token=""
    cadenaJS=""
    while indice < len(cadena):
        letra = cadena[indice]
        validacion = ValidarSimbolo(letra)

        #----------------------ID---------------------
        if validacion==1 : #Letra en ID A-B
            print ("--------------ID---------")
            token=""
            #print("Letra")
            token=token+letra
            bandera=0
            indice += 1
            while bandera==0: #B-B
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)

                if validacion==1: # Letra
                    #print("letra")
                    token=token+letra
                    indice += 1
                elif validacion==2: #Digito
                    token=token+letra
                    #print("digito")
                    indice += 1
                else:
                              
                    bandera=1
            print (token)
            
        #----------------------Digito-----------------
        elif validacion==2: #Digito en A - C
            print("----------Digito-----------")
            token=""
            token=token+letra
            bandera=0
            indice += 1

            while bandera==0: #B-B
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)

                if validacion==2: # Letra
                    #print("letra")
                    token=token+letra
                    indice += 1
                else:
                            
                    bandera=1
            print (token)


          
        #----------------------Simbolo-----------------
        elif validacion==5: #simbolos     
            break
        elif validacion==6: #control de lineas
            
            indice += 1
        else:
            print("Error Lexico")
            print(letra)
            indice += 1
            
        



    
Analizar('Horacio2 @Hola#    223#2         HOla')






        


    


        
