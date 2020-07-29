class Fraction:
    
    def __init__(self,numerador=0, denominador=1):
        if(numerador<0 or denominador<=0):
            del self
            raise Exception("You should try better")
        else:
            self.numerador        = numerador
            self.denominador      = denominador    

    def mais(self,numerador,denominador):
        if(self.denominador == denominador):
            self.denominador = denominador
            self.numerador   = self.numerador + numerador
        else:
            self.numerador   = denominador*self.numerador + self.denominador*numerador
            self.denominador = self.denominador*denominador