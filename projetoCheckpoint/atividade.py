#Ana Cristina Araújo Oliveira - RM 99816

salarioMin = int(1302)
salarioFuncionario = float(input("Informe o sálario: "))

if salarioFuncionario <0:
    print("ERRO! Digite um salário positivo!")

else:
    numeroDeFalta = int(input("Informe a quantidade de faltas: "))

    if salarioFuncionario <= salarioMin * 2:
        reajuste = salarioFuncionario * (6.45 / 100)

    elif salarioFuncionario > salarioMin * 2 and salarioFuncionario <= salarioMin * 5:
        reajuste = salarioFuncionario * (4.55 / 100)

    else:
        reajuste = salarioFuncionario * (2.89 / 100)


    if numeroDeFalta < 0:
        numeroDeFalta == 0
        bonus = 1000
    else:
        if numeroDeFalta == 0:
            bonus = 1000
        else:
            bonus = 0



    salarioReajustado = reajuste + salarioFuncionario

    print(f'''
Salário...................: R${salarioFuncionario:0.2f}
Salário Reajustado........: R${float(salarioReajustado):0.2f}
Bônus.....................: R${bonus:0.2f}''')

