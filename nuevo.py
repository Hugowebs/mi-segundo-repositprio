def vehiculo (tipo, color):
    def __iinit__ (self,tipo,color):
        self.tipo= tipo
        self.color= color
        self.velocidad= 0

    def acelerar (self, velocidad):
        self.velocidad+= velocidad

         a1 = vehiculo
        a1.acelerar (30)
        a1.acelerar (20)
        a1.acelerar (10)