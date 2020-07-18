class MaquinaAgua:
    ## thank you =) 
    def __init__(self,quant_agua = 0,
                      quant_200  = 0,
                      quant_300  = 0 ):

        self.quant_agua = quant_agua          #quantidade de agua que ainda tem na bomba
        self.quant_200  = quant_200
        self.quant_300  = quant_300

 
    def abastecerAgua(self):
        self.quant_agua = 20000
        print("Abastecido: ", self.quant_agua)

    def abastecerCopo200(self):
        self.quant_200 = 100
        print("Abastecido copos de 200ml: ", self.quant_200)

    def abastecerCopo300(self):
        self.quant_300 = 100
        print("Abastecido copos de 300ml: ", self.quant_300)

    def servirCopo200(self,quant_200,y):
        if quant_200 >0 and y >=200:
            self.quant_200  = quant_200 - 1
            self.quant_agua = y - 200
            print("Água servida em um copo de 200ml")
        else:
            if quant_200 <=0: 
                print("Abastecer copos de 200")
            else:
                print("Não há água suficiente. Favor abastecer.")    
        print("Agua restante: ", self.quant_agua)
        print("Copos de 200ml restantes: ", self.quant_200)

    def servirCopo300(self,quant_300,quant_agua):
        if quant_300 >0 and quant_agua >=300:
            self.quant_300  = quant_300 - 1
            self.quant_agua = quant_agua - 300
            print("Água servida em um copo de 300ml")
        else: 
            print("Abastecer água ou copos")
        print("Agua restante: ", self.quant_agua)
        print("Copos de 300ml restantes: ", self.quant_300)    