from Analizadores.ErrorLexicoJS import ErrorLexJS


lista_error = list()
fila=0
columna=0


#nuevo= ErrorLexJS("#",1,2)

#lista_error.append(nuevo)
#nuevo= ErrorLexJS("%",1,2)
#lista_error.append(nuevo)





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
    elif varascii==39 or varascii==37 or varascii==61 or varascii==58 or varascii==59 or varascii==62 or varascii==60 or varascii==40 or varascii==41 or varascii==125 or varascii==123 or varascii==43 or varascii==45  or varascii==46 or varascii==44 or varascii==33 or varascii==38 or varascii==124 :
        return 5 #simbolos ' % = ; : > < ( ) } { + - . , ! & |   
    elif  varascii==32 :
        return 6 #espacio en blanco
    elif varascii==10 :
        return 7 #salto de linea
    elif varascii>=0 and varascii<=31:
        return 8 #control de linea 
    elif varascii== 92 :
        return 9 # \ diagonal      
    elif varascii==34:
        return 10 # " comillas   
    else: 
        return 0




def AnalizarJS(cadena): 
    Consola=""
    indice=0
    fila=1
    columna=1
    banderaID=0
    banderaDigito=0
    banderaCadena=0


    token=""
    cadenaJS=""
    while indice < len(cadena):
        letra = cadena[indice]
        validacion = ValidarSimbolo(letra)
        


        #----------------------ID---------------------
        if validacion==1 : #Letra en ID A-B
            
            print ("--------------ID---------")
            if banderaID==0:
                Consola+="S0->S1 [label=\""+letra+"\"]\n"

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
                    if banderaID==0:
                        Consola+="S1->S1 [label=\""+letra+"\"]\n"
                    #print("letra")
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==2: #Digito
                    if banderaID==0:#validar banderaID
                        Consola+="S1->S1 [label=\""+letra+"\"]\n"
                    token=token+letra
                    #print("digito")
                    indice += 1
                    columna+=1
                else:
                    if banderaID==0:#validar banderaID
                        Consola+="S1[shape=\"doublecircle\"]\n" 
                        #Consola+="S1->S0 [label=\""+letra+"\"]\n"
                        banderaID= 1         
                    bandera=1
            print (token)

            token=""
            
        #----------------------Digito-----------------
        elif validacion==2: #Digito en A - C
            if banderaDigito==0:#validar banderaDigito
                Consola+="S0->S2 [label=\""+letra+"\"]\n" 
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

                if validacion==2: # Letra 
                    if banderaDigito==0:#validar banderaDigito
                        Consola+="S2->S2 [label=\""+letra+"\"]\n" 
                    #print("letra")
                    token=token+letra
                    indice += 1
                    columna+=1
                else:     
                    if banderaDigito==0:#validar banderaDigito
                        Consola+="S2[shape=\"doublecircle\"]\n" 
                        #Consola+="S2->S0 [label=\""+letra+"\"]\n"  
                        banderaDigito=1
                    bandera=1 # Salida Digito
            print (token)
            token=""
 
        #---------------Comentario  ---------------------
        elif validacion==4: #Diagonal / en A - G
            
            print("----------Comentario  ----------")
            #token=""
            token=token+letra
            bandera=0
            indice += 1
            columna+=1

            if indice==len(cadena):
                break
            else:
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                #--------------------Comentario de Linea-------------------
                if validacion==4: #Diagonal / G -H  
                    
                    print("----------Comentario de Linea---------")
                    while bandera==0: #C-C
                        if indice==len(cadena):
                            break

                        letra = cadena[indice]
                        validacion = ValidarSimbolo(letra)
                        

                        if validacion==7: # Salto de Linea 
                            fila+=1
                            columna=1
                            bandera =1
                        #Salida de Comentario

                        else: 
                            
                            token=token+letra
                            indice += 1
                            columna+=1
                                 
                        # Salida Digito
                    print (token)
                    token=""
                    print("----------Fin Comentario Linea--------")
                #-------------------Comentario Multilinea--------------
                elif validacion==3: # * Asterisco    
                    
                    print("----------Inicio Comentario MultiLinea")
                    while bandera==0: #G-I
                        if indice==len(cadena):
                            break

                        letra = cadena[indice]
                        validacion = ValidarSimbolo(letra)
                        

                        if validacion==3: #*Asterisco 
                            
                            token=token+letra
                            indice += 1 
                            columna+=1
                            if indice==len(cadena):
                                break
                            
                            letra = cadena[indice]
                            validacion = ValidarSimbolo(letra)
                            

                            if validacion==4: # / Diagonal
                                
                                token=token+letra
                                indice += 1
                                columna+=1 
                                #print("----------Fin Comentario Multilinea--------")                               
                                break
                        
                            else:
                                
                                token=token+letra
                                indice += 1 
                                columna+=1 
                            
                        #Salida de Comentario

                        else: 
                                validacion=ValidarSimbolo(letra)
                                if validacion==7:
                                    token=token+letra
                                    indice += 1 
                                    columna+=1 
                                    fila+=1
                                    columna=1
                                else:    
                                    token=token+letra
                                    indice += 1 
                                    columna+=1    
                        # Salida Digito
                    print (token)
                    token=""
                    print("----------Fin Comentario Multilinea--------")


                else:
                    
                    print("Error Lexico Comentario")    
                    token=token+letra
                    indice+=1
                    columna+=1


                    while bandera==0: #C-C
                        if indice==len(cadena):
                            break

                        letra = cadena[indice]
                        validacion = ValidarSimbolo(letra)

                        if validacion==7:
                            NuevoError= ErrorLexJS("Salto-Linea",str(fila),str(columna))
                            lista_error.append(NuevoError)
                            columna=1
                            bandera=1
                        else:
                            NuevoError= ErrorLexJS(str(letra),str(fila),str(columna))
                            lista_error.append(NuevoError)
                            token=token+letra
                            indice += 1
                            columna+=1     
                            bandera=1

                        # Salida Digito
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
                else: 
                        
                    bandera=1 # Salida Digito
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
            if banderaCadena==0:#validar banderaCadena
                        Consola+="S0->S3 [label=\"comilla\"]\n"  
            token=token+letra
            bandera=0
            indice += 1
            columna+=1
            print("----------Cadena---------")
            while bandera==0: #B-B
                if indice==len(cadena):
                    print("ERROR CADENA 0")
                    if banderaCadena==0:#validar banderaCadena
                        #Consola+="S4->S0 [label=\""+letra+"\"]\n"
                        #Consola+="S4[shpae=\"doublecircle\"]\n" 
                        banderaCadena=1  
                    NuevoError= ErrorLexJS(str(letra),str(fila),str(columna))
                    lista_error.append(NuevoError)
                    break
                letra = cadena[indice]
                validacion = ValidarSimbolo(letra)
                
                if validacion==10: # Comilla
                    if banderaCadena==0:#validar banderaCadena
                        Consola+="S3->S4 [label=\"comilla\"]\n" 
                        Consola+="S4[shape=\"doublecircle\"]\n"   
                        banderaCadena=1
                    #print("letra")
                    bandera=1
                    token=token+letra
                    indice += 1
                    columna+=1
                elif validacion==7:
                    if banderaCadena==0:#validar banderaCadena
                        #Consola+="S4->S0 [label=\""+letra+"\"]\n"  
                        Consola+="S4[shape=\"doublecircle\"]\n" 
                        banderaCadena=1  
                    print("ERROR CADENA 1")
                    NuevoError= ErrorLexJS("Salto-Linea",str(fila),str(columna))
                    lista_error.append(NuevoError)
                    token=token+letra
                    indice+=1
                    columna+=1
                    bandera=1
                    columna=1
                    fila+=1

                else: #Lo que sea 
                    if banderaCadena==0:#validar banderaCadena
                        Consola+="S3->S3 [label=\""+letra+"\"]\n"  

                    token=token+letra
                    #print("digito")
                    indice += 1
                    columna+=1
                
            print (token)
            token=""

        else: #---------------OTROS CARACTERES------------------

            
            NuevoError= ErrorLexJS(str(letra),str(fila),str(columna))
            lista_error.append(NuevoError)
            print("---------Error Lexico----------")

            print(letra)
            indice += 1
            columna+=1
    return Consola,lista_error
            
            
            
def ErroresLexicosJS():
    for obj in lista_error: 
        NuevoError= "simbolo: " + str(obj.simbolo) + " fila: " + str(obj.fila) + " columna: " + str(obj.columna)
        print(NuevoError)
            
        

       

#Analizar("\"Ho\n\nla@\"@")
#Analizar('asda asd3 @ ')#para = document.querySelector(\'p\');@'
#Analizar('//"HOla$$$//$$$$@\n@\n\nHoracio@ s')
#Analizar('/*HOla$$$$$$$@\n Horacio@ */@')
#AnalizarJS("@function setfocus() \n { \n            document.forms(0).txt.select(); \n            document.forms(0).txt.focus();  \n  }")
#Analizar('Horacio2 @Hola#  &&&&  223#2      \n \n   HOla')
#ErroresLexicosJS()








        


    


        
