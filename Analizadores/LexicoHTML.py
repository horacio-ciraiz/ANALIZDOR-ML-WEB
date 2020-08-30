from ErrorLexicoHTML import ErrorLexHTML

lista_error = list()
fila=0
columna=0

def ValidarSimbolo(caracter):
    varascii= ord(caracter)

    if varascii>=65 and varascii<=90 or varascii>=97 and varascii<=122 :
        return 1 #Letras
    elif varascii>= 48 and varascii<=57: 
        return 2 #numeros    
    elif varascii== 42 :
        return 3 # * asterisco   
    #elif varascii== 47 :
        #return 4 # / diagonal   
    elif  varascii==47 or varascii==37 or varascii==61 or varascii==59 or varascii==62 or varascii==60 or varascii==40 or varascii==41 or varascii==125 or varascii==123 or varascii==43 or varascii==45  or varascii==46 or varascii==44 or varascii==33 or varascii==38 or varascii==124 :
        return 5 #simbolos ' % = ; > < ( ) } { + - . , ! & |   
    elif  varascii==32 :
        return 6 #espacio en blanco
    elif varascii==10 :
        return 7 #salto de linea
    elif varascii>=0 and varascii<=31:
        return 8 #control de linea 
    elif varascii== 92 :
        return 9 # \ diagonal      
    elif varascii==34 or varascii==39:
        return 10 # " comillas   
    else: 
        return 0

def AnalizarHTML(cadena):
    indice=0
    fila=1
    columna=0

    token=""
    cadenaHTML=""

    while indice<len(cadena):
        letra=cadena[indice]
        validacion = ValidarSimbolo(letra)

        #----------------------ID---------------------
        if validacion==1 : #Letra en ID A-B
            
            print ("--------------ID---------")
            
            #print("Letra")
            token=token+letra
            bandera=0
            indice += 1
            columna+=1
            while bandera==0: #B-B
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)

                

                if validacion==1: # Letra
                    
                    #print("letra")
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==2: #Digito
                    
                    token=token+letra
                    #print("digito")
                    indice += 1
                    columna+=1
                elif validacion==6: #Espacio
                    print("---------Espacio")
                    bandera=1
                elif validacion==5: #Simbolos
                    print("---------Simbolo")
                    bandera=1
                elif validacion==6 or validacion==7 : #salto o validacion
                    print ("---------control de linea")
                    bandera=1
                elif validacion==10: #comillas
                    print ("---------Comillas")
                    bandera=1


                else:
                    print(token)
                    token=""
                    print("---------Error Lexico---------")
                    token=token+letra

                    NuevoError= ErrorLexHTML(str(letra),str(fila),str(columna))
                    lista_error.append(NuevoError)

                    #print("digito")
                    indice += 1
                    columna+=1
            print (token)

            token=""
        elif validacion==2: #Digito en A - C
            
            print("----------Digito----------")
            
            token=token+letra
            bandera=0
            indice += 1
            columna+=1

            while bandera==0: #C-C
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)

                if validacion==2: # Digito 
                    #print("letra")
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==6 : #Espacio
                    print("---------Espacio")
                    bandera=1

                elif validacion==5 : #Simbolo
                    print("---------Simbolo")
                    bandera=1      
                elif validacion==6 or validacion==7 : #salto o validacion
                    print ("---------control de linea")
                    bandera=1
                elif validacion==10: #comillas
                    print ("---------Comillas")
                    bandera=1                    
                else:
                    print(token)
                    token=""
                    print("---------Error Lexico---------")
                    token=token+letra

                    NuevoError= ErrorLexHTML(str(letra),str(fila),str(columna))
                    lista_error.append(NuevoError)
                    #print("digito")
                    indice += 1
                    columna+=1                        
                    
            print (token)
            token=""

        #----------------------Simbolo-----------------
        elif validacion==5: #simbolos  A-D  
            
            print("----------Simbolo----------")
            
            token=token+letra
            bandera=0
            indice += 1
            columna+=1

            while bandera==0: #D-D
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                

                if validacion==5: # SIMBOLO 
                    
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==1 : #Letra
                    #print("---------Letra")
                    bandera=1  
                elif validacion==2 : #Numero
                    print("---------Numero")
                    bandera=1      
                elif validacion==6 : #Espacio
                    print("---------Espacio")
                    bandera=1    
                elif validacion==6 or validacion==7 : #salto o validacion
                    print ("---------control de linea")
                    bandera=1
                elif validacion==10: #comillas
                    print ("---------Comillas")
                    bandera=1
                else:
                    print(token)
                    token=""
                    print("---------ANY---------")
                    token=token+letra
                    #NuevoError= ErrorLexHTML(str(letra),str(fila),str(columna))
                    #lista_error.append(NuevoError)
                    
                    #print("digito")
                    indice += 1
                    columna+=1 
                    bandera=1

                        

            print (token)
            token=""
        #-------------------Espacio en Blanco----------------
        elif validacion==6: #Espacios A-E
            
            print("----------Espacio----------")
            
            token=token+letra
            bandera=0
            indice += 1
            columna+=1
            while bandera==0: #E-E
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                

                if validacion==6: # ESPACIO EN BLANCO
                    
                    token=token+letra
                    indice += 1
                    columna+=1
                else:      
                    bandera=1 # Salida Digito
            print (token)
            token=""
        #-------------------Salto de Linea----------------
        elif validacion==7: #Salto A-F
            
            print("----------Salto de Linea----------")
            

            token=token+letra
            bandera=0
            indice += 1
            columna+=1
            fila+=1
            columna=1
            while bandera==0: #F-F
                if indice==len(cadena):
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                
                if validacion==7: # SALTO DE LINEA
                    
                    token=token+letra
                    indice += 1
                    columna+=1
                    columna=1
                    fila+=1
                else:      
                    bandera=1 # Salida Salto
            #print (token) 
            print("")
            token=""
        #-------------------Cadena-----------------------
        elif validacion==10: # Comilla A- K 
            
            token=token+letra
            bandera=0
            indice += 1
            columna+=1
            print("----------Cadena---------")
            while bandera==0: #B-B
                if indice==len(cadena):
                    print("ERROR CADENA 0")
                    
                    NuevoError= ErrorLexHTML(str(letra),str(fila),str(columna))
                    lista_error.append(NuevoError)
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                
                if validacion==10: # Comilla
                    
                    #print("letra")
                    bandera=1
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==7:
                    
                    print("ERROR CADENA 1")
                    NuevoError= ErrorLexHTML("Salto-Linea",str(fila),str(columna))
                    lista_error.append(NuevoError)
                    token=token+letra
                    indice+=1
                    columna+=1
                    bandera=1
                    columna=1
                    fila+=1

                else: #Lo que sea 
                    
                    token=token+letra
                    #print("digito")
                    indice += 1
                    columna+=1
                
            print (token)
            token=""
                
            
  
        else:
            print("Lo que sea ")   
            print(letra)
            indice+=1
            columna+=1 

def ErroresLexicosHTML():
    for obj in lista_error: 
        NuevoError= "simbolo: " + str(obj.simbolo) + " fila: " + str(obj.fila) + " columna: " + str(obj.columna)
        print(NuevoError)
        #print(obj.fila)
        #print(columna)
      #print(lista_error)

AnalizarHTML(":<html>\n<head><title><title></head><body><ul>\n <li>Elemento 1</li> <li>Elemento 2</li> <li>Elemento 3</li>\n  <li>Elemento4</li> </ul> <p style=\"color:red; font-size:100px\">Hola Mundo</p></html>")
ErroresLexicosHTML()

        