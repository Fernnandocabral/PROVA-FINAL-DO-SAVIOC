#faça um programa que caucule o valor de imposto que uma pessoa de lisarb deve pagar de acordo com o seu salario
#deve pagar de acordo com o salario
#de 0.00 a 2000.00
renda = float(input("digite sua renda atual:R$"))
def imposto():
    if renda <=2000.00:
        print("VOCÊ ESTÁ ISENTO DE TAXA DE IMPOSTO")

    elif renda >2000.00 and renda <= 3000.00:
        imposto1 = (renda * 8)/10
        print (f'SUA TAXA DE IMPOSTO DE RENDA É DE R${imposto1:.2f}')

    elif renda > 3000.00 and renda <=4000.00:
         imposto2 = (renda * 18)/100
         print (f'SUA TAXA DE IMPOSTO DE RENDA É DE R${imposto2:.2f}')

    
    else:
        imposto3 = (renda * 28) / 100
        print (f'SUA TAXA DE IMPOSTO DE RENDA É DE R${imposto3:.2f}')


imposto()

