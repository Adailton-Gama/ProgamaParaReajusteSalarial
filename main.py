#Programa que recebe o salário de um colaborador e o reajusta segundo o seguinte critério, baseado no salário atual:

print()
print('AC Informática')
print()
print('Programa de Reajuste salarial')

func = input('Digite seu nome: ')
salAtual=int(input('Qual o valor do seu salário atual? '))

#salários até R$ 280,00 : aumento de 20%
if salAtual <= 280:
    pA='20%'
    aSal = salAtual*0.20
    salN = salAtual + aSal
    #print('o funcionário {}, teve o seu salário aumentado de R$ {}, para R$ {}'.format(func, salAtual, salN))

#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salAtual >= 280:
    pA='15%'
    aSal = salAtual * 0.15
    salN = salAtual+aSal
    #print('o funcionário {}, teve o seu salário aumentado de R$ {}, para R$ {}'.format(func,salAtual,salN))

#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salAtual >= 700:
    pA='10%'
    aSal = salAtual * 0.10
    salN = salAtual+aSal
    #print('o funcionário {}, teve o seu salário aumentado de R$ {}, para R$ {}'.format(func,salAtual,salN))

#salários de R$ 1500,00 em diante : aumento de 5%
elif salAtual >= 1500:
    pA='5%'
    aSal = salAtual * 0.05
    salN = salAtual+aSal
    #print('o funcionário {}, teve o seu salário aumentado de R$ {}, para R$ {}'.format(func,salAtual,salN))

 #Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('o funcionário {}, teve o seu salário aumentado em {}, elevando assim de R$ {}, para R$ {}'.format(func, pA, salAtual, salN))