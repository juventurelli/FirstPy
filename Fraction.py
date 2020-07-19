class Fraction:
    
    def __init__(self,numerador=0, denominador=1):

        self.numerador        = numerador
        self.denominador      = denominador   
        self.resultado_fracao = None

    def Fraction(self, numerador,denominador):
        if denominador >0:
            self.resultado_fracao = numerador/denominador
            return self.resultado_fracao
        else:
            break

    def mais(self,numerador,denominador):
        if(self.denominador == denominador):
            self.denominador = denominador
            self.numerador   = self.numerador + numerador
        else:
            self.numerador   = denominador*self.numerador + self.denominador*numerador
            self.denominador = self.denominador*denominador