import MaquinaAgua as MA

maq = MA.MaquinaAgua()

print(maq.quant_agua)
print(maq.quant_200)
print(maq.quant_300)  

maq.servirCopo200(maq.quant_200,maq.quant_agua)
maq.servirCopo300(maq.quant_300,maq.quant_agua)

maq.abastecerAgua()
maq.abastecerCopo300()

maq.servirCopo200(maq.quant_200,maq.quant_agua)
maq.abastecerCopo200()
maq.abastecerCopo200()
maq.abastecerCopo200()

for i in range(101): 
    maq.servirCopo300(maq.quant_300,maq.quant_agua)

#maq.servirCopo300(maq.quant_300,maq.quant_agua)
#maq.servirCopo300(maq.quant_300,maq.quant_agua)
#maq.servirCopo300(maq.quant_300,maq.quant_agua)
#maq.servirCopo200(maq.quant_200,maq.quant_agua)
#maq.servirCopo200(maq.quant_200,maq.quant_agua)

#maq.servirCopo200(maq.quant_200,maq.quant_agua)
#maq.servirCopo200(maq.quant_200,maq.quant_agua)

#maq.abastecerCopo300()
#maq.servirCopo200(maq.quant_200,maq.quant_agua)
