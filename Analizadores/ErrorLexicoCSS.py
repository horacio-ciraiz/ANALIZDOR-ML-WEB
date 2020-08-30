class ErrorLexCSS:

    def __init__(self, simbolo, fila, columna):
        self.simbolo = simbolo
        self.fila = fila
        self.columna = columna

    #def __repr__(self):
      #  return str(self.__dict__)
    def __str__(self):
        return "simbolo=%s fila=%s columna=%s" % (self.simbolo, self.fila, self.columna)

