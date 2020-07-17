class MaquinaAgua:
 
    def __init__(self,quant_agua = 0):

        self.quant_agua = quant_agua          #quantidade de agua que ainda tem na bomba
 
    def abastecerAgua(self):
        self.quant_maxima = 2000
        print("Volume: ", self.quant_maxima)