#aumento de salario
salario = float(input("digite o valor do salario"))

if salario<= 400.00:
    reajuste = (salario * 15)/100
    new = (salario + reajuste)
    print(f"""o novo salario é de R$:{new:.2f})
    o reajuste ganho foi: {reajuste:.2f}
    em pecentual: 15%""")

elif salario == 400.01 or salario <= 800.00:
    reajuste02 = (salario * 12)/100
    new02 = (salario+reajuste02)
    print(f"""o novo salario é de R$: {new02:.2f})
    o reajuste ganho foi: {reajuste02:.2f}
    em percentual:12%""")

elif salario == 400.01 or salario <= 800.00: #calculo do aumento dos funcionarios
    reajuste03 = (salario * 10)/100
    new03 = (salario+reajuste03)
    print(f"""o novo salario é de R$: {new03:.2f})
    o reajuste ganho foi: {reajuste03:.2f}
    em percentual:10%""")

elif salario == 800.01 or salario <= 1200.00: #calculo do aumento dos funcionarios
    reajuste04 = (salario * 10)/100
    new04 = (salario+reajuste04)
    print(f"""o novo salario é de R$: {new04:.2f})
    o reajuste ganho foi: {reajuste04:.2f}
    em percentual:10%""")

elif salario == 1200.01 or salario <= 2000.00: #calculo do aumento dos funcionarios
    reajuste05 = (salario * 10)/100
    new05 = (salario+reajuste05)
    print(f"""o novo salario é de R$: {new05:.2f})
    o reajuste ganho foi: {reajuste05:.2f}
    em percentual:10%""")

else: #calcular o aumento dos funcionarios 
    reajuste06 = (salario * 10)/100
    new06 = (salario+reajuste06)
    print(f"""o novo salario é de R$: {new06:.2f})
    o reajuste ganho foi: {reajuste06:.2f}
    em percentual:4%""")
