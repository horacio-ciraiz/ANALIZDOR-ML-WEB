def Precedencia(TokenOperador):   
    if TokenOperador == '+' or TokenOperador == '-': 
        return 1
    if TokenOperador == '*' or TokenOperador == '/': 
        return 2
    return 0
  
def Evaluar(tokens):    
    Valores = [] #---------Arreglo Valores
    Operaciones = [] #-----Arreglo Operaciones + - / *
    i = 0
    try:  
        while i < len(tokens): 
            #---------------Espacio Vacio-------------------
            if tokens[i] == ' ': 
                i += 1
                continue
            #---------------Parentesis ---------------------
            elif tokens[i] == '(': 
                Operaciones.append(tokens[i]) 
            #---------------Numeros-------------------------
            elif tokens[i].isdigit(): 
                while (i < len(tokens) and (tokens[i].isdigit() or tokens[i]==".")): 
                    val = tokens[i]
                    i += 1
                i-=1
                Valores.append(val) 
            #----------------ID------------------------------
            elif tokens[i].isidentifier(): 
                while (i < len(tokens) and (tokens[i].isidentifier() or tokens[i].isdigit() )):               
                    val = tokens[i] 
                    i += 1
                i-=1
                Valores.append(val)
            elif tokens[i] == ')': 
                while len(Operaciones) != 0 and Operaciones[-1] != '(': 
                    if(len(Valores)%1==0):#o Valores>1
                        val2 = Valores.pop() 
                        val1 = Valores.pop() 
                        TokenOperador = Operaciones.pop() 
                        Valores.append(1) 
                    else:
                        val1 = Valores.pop() 
                        TokenOperador = Operaciones.pop() 
                        Valores.append(1)
                Operaciones.pop() 
            else: 
                while (len(Operaciones) != 0 and Precedencia(Operaciones[-1]) >= Precedencia(tokens[i])):       
                    val2 = Valores.pop() 
                    val1 = Valores.pop() 
                    TokenOperador = Operaciones.pop() 
                    Valores.append(1) 
                Operaciones.append(tokens[i]) 
            i += 1
    except:
        #print("Error Sintactico Parentesis")
        return False
    try:
        while len(Operaciones) != 0: 
            val2 = Valores.pop() 
            val1 = Valores.pop() 
            TokenOperador = Operaciones.pop()      
            Valores.append(1) 
        if len(Valores)>1 and len(Operaciones==0):
            return False
    # Top of 'Valores' contains result, 
    # return it. 
        return True, Valores[-1] 
    except:
        #print("Error Sintactico Fatan Numeros")
        return False
