from SintacticoExpresion import Evaluar

def LexRTM(cadena):
    print("Inicio Analisis")
    cadenatoken=""
    columna=1
    fila=1
    i=0
    codigoHTML=""

    while i<len(cadena):
        #print("Entre")
        if cadena[i].isidentifier():
            cadenatoken+=cadena[i]
            columna+=1
            i+=1
            #print("IDENTIFCADOR: " )
        elif cadena[i].isdigit():
            
            
            
            while (i < len(cadena) ): 
                if cadena[i].isdigit():    
                    cadenatoken+= cadena[i]
                    i += 1
                    columna+=1
                elif cadena[i]==".":
                    cadenatoken+= cadena[i]
                    i += 1
                    columna+=1
                    while (i < len(cadena) and cadena[i].isdigit()): 
                        cadenatoken+= cadena[i]
                        i += 1
                        columna+=1
                else:
                    break    
            #print("NUMERO")



        elif cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/" or cadena[i]==" " or cadena[i]=="(" or cadena[i]==")":
            cadenatoken += cadena[i]
            columna+=1
            i+=1

        elif cadena[i]=="\n"  or cadena[i]=="$": #---------------------Salto de Linea---------------------
            #print(cadenatoken)
            #print("Ejecutar Metodo")
            columna=1
            fila+=1
            ValorCorrecto = Evaluar(cadenatoken)
            CadenaValor=""
            
            print("\nCadena " + cadenatoken + " Resulatdo :" + str(ValorCorrecto))

            if ValorCorrecto==(True,1):
                CadenaValor="Correcto"
            else:
                CadenaValor="Incorrecto"

            codigoHTML+="\n <tr> <td align=\"center\">" + cadenatoken + "</td><td align=\"center\">" + CadenaValor + "</td></tr>"

            cadenatoken=""
            i+=1
        else:
            print("Error Lexico:"+ cadena[i] +" fila:" + str(fila) + " columna: " + str(columna) )
            i+=1
            break
    ReporteRTM(codigoHTML)
    codigoHTML=""
    #print(cadenatoken)

def ReporteRTM(CadenaTabla):
    CadenaHTML=""
    ArchivoReporteRTM = open("ReporteRTM.html","w") 
    ArchivoReporteRTM.write(CadenaHTML) 
    ArchivoReporteRTM.close() 

    CadenaHTML=""
    CadenaHTML+="<html><head><title>Reporte RTM</title></head> "
    CadenaHTML+="<body><h1 align=center>Reporte RTM</h1>"
    CadenaHTML+="<table border=2 width=400 align=center>"
    CadenaHTML+="<tr><td align=\"center\">Expresion</td><td align=\"center\">Validacion</td></tr>"
    CadenaHTML+=CadenaTabla
    CadenaHTML+="</table></body></html>"        
    ArchivoErroresCSS = open("ReporteRTM.html","w") 
    ArchivoErroresCSS.write(CadenaHTML) 
    ArchivoErroresCSS.close() 



LexRTM("(2+3/3(3+69(5-6))*((2.3+8.5)+3*(535))"
+ "\n" + "2+6-5*/52"
+ "\n" + "2+3*5-6"
+ "\n" + "(5.50+2+*(3+5(()"
+ "\n" + "(3+-5/5*63-5.30)"
+ "\n" + "((4 - 6 *(1/8)/2)+(6-9*(2))-(5)*(3*x)/(var1))"
+ "\n" + "(7/6*2)-(var1 * exp1/r)/(6-8))"
+ "\n" + "2*(3)+(2+5)-(2.5+3.8)-(1)-(0)"
+ "\n" + "78-20353.0/85*((3+(2+6)))+3" + " $")