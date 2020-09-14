from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
import os
from subprocess import check_call

#--------------Importa JS
from Analizadores.LexicoJS import AnalizarJS
from Analizadores.LexicoJS import ErroresLexicosJS
from Analizadores.ErrorLexicoJS import ErrorLexJS
#--------------Import CSS
from Analizadores.LexicoCSS import AnalizarCSS
from Analizadores.LexicoCSS import ErroresLexicosCSS
from Analizadores.ErrorLexicoCSS import ErrorLexCSS 
#--------------Importa HTML
from Analizadores.LexicoHTML import AnalizarHTML
from Analizadores.LexicoHTML import ErroresLexicosHTML
from Analizadores.ErrorLexicoHTML import ErrorLexHTML
#--------------Importa Expresion 
from Analizadores.LexicoExpresion import LexRTM
#from Analizadores.LexicoHTML import AnalizarHTML
#from Analizadores.LexicoCSS import AnalizarCSS


class INTERFACE:
    DireccionTemporal=""
    def __init__(self):
        self.Ventana = Tk()
        self.txtEntrada= Text(self.Ventana,width=100)
        self.txtConsola= Text(self.Ventana,width=100)
        
        
        #textContainer = Frame(self.Ventana, borderwidth=1, relief="suken")
        #txtEntrada = Text(textContainer, width=24, height=13, wrap="none", borderwidth=0)
        #textVsb = Scrollbar(textContainer, orient="vertical", command=txtEntrada.yview)
        #textHsb = Scrollbar(textContainer, orient="horizontal", command=txtEntrada.xview)
        #txtEntrada.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)

        
        #VENTANA
        self.Ventana.title("Proyecto 1 - ML WEB EDITOR 201513758")
        self.Ventana.geometry('763x487+250+100')
        self.Ventana.configure(bg='#474140')
        self.Ventana.resizable(0, 0)


        # MENU 
        self.Menus= Menu(self.Ventana)
        # MENU ARCHIVO
        self.Archivo_item = Menu(self.Menus) #Menu
        self.Archivo_item.add_command(label='Nuevo', command=self.MenuNuevo )
        self.Archivo_item.add_separator()
        self.Archivo_item.add_command(label='Abrir',command=self.MenuAbrir)
        self.Archivo_item.add_separator()
        self.Archivo_item.add_command(label='Guardar')
        self.Archivo_item.add_separator()
        self.Archivo_item.add_command(label='Guardar Como')

        #MENU REPORTE

        self.Reporte_item = Menu(self.Menus)
        self.Reporte_item.add_command(label='Reporte JS')
        self.Reporte_item.add_separator()
        self.Reporte_item.add_command(label='Reporte CSS')
        self.Reporte_item.add_separator()
        self.Reporte_item.add_command(label='Reporte RTM')
        self.Reporte_item.add_separator()        
        self.Reporte_item.add_command(label='Errores JS',command=self.ErroresLexicosJS)
        self.Reporte_item.add_separator()
        self.Reporte_item.add_command(label='Errores CSS',command=self.ErroresLexicosCSS)
        self.Reporte_item.add_separator()
        self.Reporte_item.add_command(label='Errores HTML',command=self.ErroresLexicosHTML)

        #MENU ANALIZAR

        self.Analizar_item=Menu(self.Menus)
        self.Analizar_item.add_command(label='Analizar JS',command=self.MenuAnalizarJS)
        self.Analizar_item.add_separator()
        self.Analizar_item.add_command(label='Analizar CSS',command=self.MenuAnalizarCSS)
        self.Analizar_item.add_separator()
        self.Analizar_item.add_command(label='Analizar HTML',command=self.MenuAnalizarHTML)
        self.Analizar_item.add_separator()
        self.Analizar_item.add_command(label='Analizar RTM',command=self.MenuAnalizarRTM)

        self.Menus.add_cascade(label='Archivo',menu=self.Archivo_item)
        self.Menus.add_cascade(label='Analizar',menu=self.Analizar_item)
        self.Menus.add_cascade(label='Reporte',menu=self.Reporte_item)
        
        self.Ventana.config(menu=self.Menus)




        

        #ENTRADA
        self.txtEntrada = scrolledtext.ScrolledText(self.Ventana,width=45,height=30,wrap="none")
        self.txtEntrada.pack(side="left", fill="both", expand=True)
        self.txtEntrada.place(x=0,y=1)


        self.txtConsola = scrolledtext.ScrolledText(self.Ventana,width=45,height=30,bg="black",fg="white",insertbackground="white")
        self.txtConsola.place(x=381,y=1)
        self.Ventana.mainloop()

    #-----------------Metodo Menu Nuevo-------------------
    def MenuNuevo(self):
        self.txtEntrada.delete('1.0', END)
        self.txtConsola.delete('1.0', END)
    def lines_that_equal(self,line_to_match, fp):
        return [line for line in fp if line == line_to_match]
    #-----------------Metodo Menu Abrir-------------------  
    def MenuAbrir(self):
        
        nameFile=filedialog.askopenfilename(title = "Seleccione Archivo",filetypes = (("All Files","*.*"),("js files","*.js"),("rmt files","*.rmt"), ("html files","*.html"),("css files","*.css")))
        if nameFile!='':
            archi1=open(nameFile, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.txtEntrada.delete("1.0", END) 
            self.txtEntrada.insert("1.0", contenido)
            #----------------linea de la direccion
            search = open(nameFile)
            for line in search:
                if "PATHW" in line:
                    print (line) 
                    nombreLista = re.split(' |\n',line)

            self.DireccionTemporal = nombreLista[1]
            print (self.DireccionTemporal)
            search.close()


    #---------------Metodo Menu Analisis JS ---------------


    def MenuAnalizarJS(self):

    #------------------econtrar path



        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Consola,lista_errorJS=AnalizarJS(entrada,self.DireccionTemporal)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", Consola)
        
        
        CadenaGrap="digraph G {"+ Consola+"}"
        archi1 = open("ReporteJS.dot","w") 
        archi1.write(CadenaGrap) 
        archi1.close() 


        messagebox.showinfo('Project 1', 'Analisis JS Terminado')
        #check_call(['dot', '-Tpng','C:/Users/Horacio Ciraiz/Documents/CURSOS/2DO SEMESTRE 2020/PROGRAMACION/LABORATORIO/Proyecto1/OLC1_Proyecto1_201513758/ReporteJS.dot','-o','C:/Users/Horacio Ciraiz/Documents/CURSOS/2DO SEMESTRE 2020/PROGRAMACION/LABORATORIO/Proyecto1/OLC1_Proyecto1_201513758/ReporteJS.png'])
        check_call(['dot', '-Tpng','ReporteJS.dot','-o','ReporteJS.png'])
        
        #subprocess.call('dot ReporteJS.dot -o ReporteJS.png -Tpng ', shell=True)
        #os.system("dot -ReportejS.png -Tpng ReporteJS.dot")

    #---------------Metodo Error Lexico JS-----------------
    def ErroresLexicosJS(self):
        ErroresLexicosJS()
        messagebox.showinfo('Project 1', 'Errores Lexicos JS')
            
    #---------------Metodo Menu Analisis CSS---------------
    def MenuAnalizarCSS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Consola,lista_errorCSS=AnalizarCSS(entrada,self.DireccionTemporal)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", Consola)
        messagebox.showinfo('Project 1', 'Analisis CSS Terminado')

        


    #----------------Metodo Error Lexico CSS----------------
    def ErroresLexicosCSS(self):
        ErroresLexicosCSS()
        messagebox.showinfo('Project 1', 'Errores Lexicos CSS')


    #---------------Metodo Menu Analisis HTML---------------
    def MenuAnalizarHTML(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Consola,lista_errorHTML=AnalizarHTML(entrada)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", Consola)
        messagebox.showinfo('Project 1', 'Analisis HTML Terminado')


    #----------------Metodo Error Lexico HTML----------------
    def ErroresLexicosHTML(self):
        ErroresLexicosHTML()
        messagebox.showinfo('Project 1', 'Errores Lexicos HTML')
    
    def MenuAnalizarRTM(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Arreglo=[]
        Arreglo=LexRTM(entrada+"$")
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", Arreglo)
        print("RTM")
        
       



start = INTERFACE()

