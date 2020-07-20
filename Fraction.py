class Fraction:
    
    def __init__(self,numerador=0, denominador=1):
        if(numerador>=0):
            self.numerador        = numerador
        if(denominador>0):
            self.denominador      = denominador    
        else: 
            print("whatever")

    def mais(self,numerador,denominador):
        if(self.denominador == denominador):
            self.denominador = denominador
            self.numerador   = self.numerador + numerador
        else:
            self.numerador   = denominador*self.numerador + self.denominador*numerador
            self.denominador = self.denominador*denominador