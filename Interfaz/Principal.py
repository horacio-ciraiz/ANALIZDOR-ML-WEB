from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox




class INTERFACE:

    def __init__(self):
        self.Ventana = Tk()
        self.txtEntrada= Entry(self.Ventana,width=10)
        self.txtConsola= Entry(self.Ventana,width=10)

        #VENTANA
        self.Ventana.title("Proyecto 1 - ML WEB EDITOR 201513758")
        self.Ventana.geometry('800x600+250+100')
        self.Ventana.configure(bg='#474140')
        self.lbl = Label(self.Ventana,text="ML WEB",font=("Arial Bold",15))
        self.lbl.place(x=350,y=10)


        # MENU

        #ENTRADA
        self.txtEntrada = scrolledtext.ScrolledText(self.Ventana,width=50,height=10)
        self.txtEntrada.place(x=50,y=50)

        self.Ventana.mainloop()

start = INTERFACE()
