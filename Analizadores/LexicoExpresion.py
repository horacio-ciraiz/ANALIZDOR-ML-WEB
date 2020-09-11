def LexRTM(cadena):
    print("Inicio Analisis")
    cadenatoken=""
    i=0
    codigoHTML=""
    ValorCorrecto=True
    while i<len(cadena):
        if cadena[i].isidentifier():
            cadenatoken+=cadena[i]
        elif cadena[i].isdigit():
            cadenatoken += cadena[i]
        elif cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/" or cadena[i]==" " or cadena[i]=="(" or cadena[i]==")":
            cadenatoken += cadena[i]
        elif cadena[i]=="\n":
            print("Ejecutar Metodo")
            
            cadenatoken=""
    i+=1             