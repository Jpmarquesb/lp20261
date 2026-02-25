'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print('João Pedro')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    media = (5+8+12)/3
    print(f'(5+8+12)/3 = {media}')
#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = int(input('digite um numero inteiro: '))
    print(f'você digitou: {numero}')
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float(input('digite um numero real: '))
    num2 = float(input('digite outro numero real: '))
    print(f'os numeros digitados foram: {num1}e {num2}')
#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num1 = float(input('digite um numero real: '))
    print (f"antecessor de {num1}: {num1 - 1}")
    print (f"Sucessor de {num1}: {num1 + 1}")
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input("digite seu nome: ").title().strip()
    endereco = input("digite seu endereço: ")
    telefone = input("digite seu telefone: ")

    print (f"\nNome: {nome}\nEndereco: {endereco}\nTelefone: {telefone}")
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num1 = int(input("digite o 1º número: "))
    num2 = int(input("digite o 2º número: "))
    print (f"subtracão de {num1} e {num2}: {num1-num2}")
#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input("digite um numero real: "))
    print(f'¼ de {num} = {num/4}')
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('1 numero real: '))
    num2 = float(input('2 numero real: '))
    num3 = float(input('3 numero real: '))
    media = (num1 + num2 + num3) / 3
    print(f'media de {num1}, {num2} e {num3} é igual a {media:.2f}')
#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('1 numero: '))
    num2 = float
    print(f'{num1}+{num2} ={num1+num2}')
    print(f'{num1}-{num2} ={num1-num2}')
    print(f'{num1}*{num2} ={num1*num2}')
    print(f'{num1}/{num2} ={num1/num2}')
#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num = float(input('digite um numero real: '))
    print(f'{num}*{num} = {num*num}')
#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('digite o saldo da conta: R$ '))
    saldo = round (saldo, 2)
    print(f'saldo de{saldo:.2f} + 2% = R$ (saldo*1.02)')
#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
def q14():
    base = float(input('digite a base do retangulo: '))
    altura = float(input('digite a altura do retangulo: '))
    print(f'perimetro = {base*2 + altura*2}')
    print(f'área: {base*altura}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor = round((float(input('valor do produto: R$ '))), 2)
    desconto_desejado = float(input('% do desconto desejado: '))
    valor_desconto = valor*desconto_desejado/100
    print(f'valor do desconto: R$ {valor_desconto:.2f}')
    print(f'valor final do produto: R$ {valor-valor_desconto:.2f}')
#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario_atual = float(input("digite o salario atual: R$ "))
    percentual_reajuste = float(input("digite o percentual de reajuste: "))
    valor_aumento = salario_atual * (percentual_reajuste / 100)
    novo_salario = salario_atual + valor_aumento
    print("-" * 30)
    print(f"o aumento será de: R$ {valor_aumento:.2f}")
    print(f"o novo salario é: R$ {novo_salario:.2f}")

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
questao = input('digite a questão a ser executada: ')
eval(f'q{questao}()')


