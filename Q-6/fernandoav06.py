#positivos e media
#LER OS VALORES E INDICAR OS POSIT.
positivos = [float(input("digite os valores:")) for _6
 in range(6)] #colocar em for in range para a contagem
totalpositivos = 0  
somadospositivos = 0

for y in positivos:
    if y > 0:
        totalpositivos += 1 #contagem d positivos
        somadospositivos += y #a soma dele

print('{} valores positivos'.format(totalpositivos))
print('{:.1f}'.format(somadospositivos / totalpositivos))