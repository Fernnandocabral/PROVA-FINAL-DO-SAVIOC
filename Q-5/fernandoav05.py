#contador
positivoos = [int(input("digite um inteiro:")) for _ in range(5)] #RECEBER OS VALORES INTEIROS E COLOCAR EM FOR
total = [par for par in positivoos if par % 2 == 0] #MOSTRAR QUAIS SÃO OS PARES
print('{} valores pares'.format(len(total)))