class WaterDispenser:

    def __init__(self,quant_agua = 0,
                      quant_copos_200  = 0,
                      quant_copos_300  = 0 ):

        self.quant_agua = quant_agua          #quantidade de agua que ainda tem na bomba
        self.quant_copos_200  = quant_copos_200
        self.quant_copos_300  = quant_copos_300

    def agua(self):
        return self.quant_agua 

    def copos_200(self):
        return self.quant_copos_200    
    
    def copos_300(self):
        return self.quant_copos_300  

    def abastecerAgua(self):
        self.quant_agua = 20000
        print("Abastecido: ", self.quant_agua)

    def abastecer_copo_200(self):
        self.quant_copos_200 = 100
        print("Abastecido copos de 200ml: ", self.quant_copos_200)

    def abastecer_copo_300(self):
        self.quant_copos_300 = 100
        print("Abastecido copos de 300ml: {}".format(self.quant_copos_300))

    def servir_copo_200(self,quant_copos_200,quant_agua):
        if quant_copos_200 >0 and quant_agua >=200:
            self.quant_copos_200  = quant_copos_200 - 1
            self.quant_agua = quant_agua - 200
            print("Água servida em um copo de 200ml")
            print("Agua restante: ", self.quant_agua)
            print("Copos de 200ml restantes: ", self.quant_copos_200) 
        else:
            if quant_copos_200 <=0: 
                print("Sem copos de 200")
            if quant_agua <=0: 
                print("Não há água suficiente. Favor abastecer.")    
        
    
    def servir_copo_300(self,quant_copos_300,quant_agua):
        if quant_copos_300 >0 and quant_agua >=300:
            self.quant_copos_300  = quant_copos_300 - 1
            self.quant_agua = quant_agua - 300
            print("Água servida em um copo de 300ml")
            print("Agua restante: ", self.quant_agua)
            print("Copos de 300ml restantes: ", self.quant_copos_300) 
        else:
            if quant_copos_300 <=0: 
                print("Sem copos de 300")
            if quant_agua <=0: 
                print("Não há água suficiente. Favor abastecer.") 