#Funcion para la Precedencia de Operadores
def precedencia(op): 
      
    if op == '+' or op == '-': 
        return 1
    if op == '*' or op == '/': 
        return 2
    return 0
  

  
#--------------------------Evaluar Expresion---------------------
def evaluar(tokens): 
    valores = []  #arreglo para los valores 
    operandos = []  #arreglo para los operandos 
    i = 0
      
    while i < len(tokens): 
          
        #---------Espacio Vacio  
        if tokens[i] == ' ': 
            i += 1
            continue
          
        #---------Parentesis Abre y lo agrego  
        elif tokens[i] == '(': 
            operandos.append(tokens[i]) 
          
        #---------Numero
        elif tokens[i].isdigit(): 
            val = 0
              
            #-----------numeros----------- 
            while (i < len(tokens) and tokens[i].isdigit()): 
                val = tokens[i]
                i += 1
            valores.append(val)
        #----------Id---------------------    
        elif tokens[i].isidentifier() or tokens[i]=="-" : 
            val = 0  
            #----------mas id-------------- 
            while (i < len(tokens) and  tokens[i].isidentifier() ): 
                val = tokens[i] 
                i += 1
            valores.append(val)              
          
        #------------parentesis que cierra -------------------------
        elif tokens[i] == ')': 
            try:    
                while len(operandos) != 0 and operandos[-1] != '(': 
                    val2 = valores.pop() 
                    val1 = valores.pop() 
                    op = operandos.pop() 
                    valores.append(1)  
                operandos.pop() 
            except:
                return False   #Error Sintactico Faltan Parentensis
        #-------------cualquier otra cosa---- + - * / 
        else: 
            #--------- comparo la precedencia de los operandos -------------------------
            try:     
                while (len(operandos) != 0 and  precedencia(operandos[-1]) >= precedencia(tokens[i])): 
                         
                        val2 = valores.pop() 
                        val1 = valores.pop() 
                        op = operandos.pop() 
                        
                        valores.append(1) 
                
            # Saco un simbolo de Operacion------------------------------------------
                operandos.append(tokens[i]) 
            except:
                    
                    return False  # Error Sintactico Faltan Numeros 
        i += 1
      
   #luego que se evaluan todos los operandos y la cadena debo de operar cualquier operando que se quede en el arreglo

    
    while len(operandos) != 0: 
        try:  
            val2 = valores.pop() 
            val1 = valores.pop() 
            op = operandos.pop() 
                  
            valores.append(1) 
        except:
            
            return False      #Error Sintactico Faltan Numeros
    return True
  