class MaquinaAgua:
    quant_maxima = 20000
    
    def __init__(self,quant_agua_left = None,quant_200_left= None):
        self.quant_agua_left = quant_agua_left
        self.quant_200_left = quant_200_left

    def say_quant_200_left(self):
        print(self.quant_200_left)

    def set_quant200(self, quant_200_left):
        self.quant_200_left = quant_200_left
        
    def get_quant200(self):
        return self.quant_200_left 

x = MaquinaAgua()
x.set_quant200(100)
print(x.say_quant_200_left())
