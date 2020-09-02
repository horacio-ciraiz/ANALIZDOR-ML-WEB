from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
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
#from Analizadores.LexicoHTML import AnalizarHTML
#from Analizadores.LexicoCSS import AnalizarCSS


class INTERFACE:

    def __init__(self):
        self.Ventana = Tk()
        self.txtEntrada= Entry(self.Ventana,width=10)
        self.txtConsola= Entry(self.Ventana,width=10)

        #VENTANA
        self.Ventana.title("Proyecto 1 - ML WEB EDITOR 201513758")
        self.Ventana.geometry('763x487+250+100')
        self.Ventana.configure(bg='#474140')
        self.Ventana.resizable(0, 0)
        #self.lbl = Label(self.Ventana,text="ML WEB" ,width=70 ,font=("Arial Bold",15))
        #self.lbl.place(x=0,y=0)

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

        self.Menus.add_cascade(label='Archivo',menu=self.Archivo_item)
        self.Menus.add_cascade(label='Analizar',menu=self.Analizar_item)
        self.Menus.add_cascade(label='Reporte',menu=self.Reporte_item)
        
        self.Ventana.config(menu=self.Menus)




        

        #ENTRADA
        self.txtEntrada = scrolledtext.ScrolledText(self.Ventana,width=45,height=30)
        self.txtEntrada.place(x=0,y=1)

        self.txtConsola = scrolledtext.ScrolledText(self.Ventana,width=45,height=30,bg="black",fg="white",insertbackground="white")
        self.txtConsola.place(x=381,y=1)

        self.Ventana.mainloop()

    #-----------------Metodo Menu Nuevo-------------------
    def MenuNuevo(self):
        self.txtEntrada.delete('1.0', END)
        self.txtConsola.delete('1.0', END)

    #-----------------Metodo Menu Abrir-------------------  
    def MenuAbrir(self):
        nameFile=filedialog.askopenfilename(title = "Seleccione Archivo",filetypes = (("js files","*.js"), ("html files","*.html"),("css files","*.css"),("All Files","*.*")))
        if nameFile!='':
            archi1=open(nameFile, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.txtEntrada.delete("1.0", END) 
            self.txtEntrada.insert("1.0", contenido)
    #---------------Metodo Menu Analisis JS ---------------
    def MenuAnalizarJS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Consola,lista_errorJS=AnalizarJS(entrada)
        self.txtConsola.delete("1.0", END)
        self.txtConsola.insert("1.0", Consola)
        messagebox.showinfo('Project 1', 'Analisis JS Terminado')

    #---------------Metodo Error Lexico JS-----------------
    def ErroresLexicosJS(self):
        ErroresLexicosJS()
        messagebox.showinfo('Project 1', 'Errores Lexicos JS')
            
    #---------------Metodo Menu Analisis CSS---------------
    def MenuAnalizarCSS(self):
        entrada = self.txtEntrada.get("1.0", END) #fila 1 col 0 hasta fila 2 col 10
        #retorno = lexer(entrada)
        Consola,lista_errorCSS=AnalizarCSS(entrada)
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
    

       



start = INTERFACE()
