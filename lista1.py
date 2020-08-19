'''
@Lucas Soares Leite - 22955658
https://www.github.com/querneu
'''
import os
import math


def questao(numero):
    if(numero == 1):
        clear_terminal()
        print("Questão 1 - Escreva um programaque apresente na tela a frase: 'Meu primeiro programa!!!'")
        print("Meu primeiro programa!!!")
        os.system('pause')

    elif(numero == 2):
        clear_terminal()
        print("Questão 2 - Escreva um programaque solicite ao usuário um número inteiro e ao final apresente na tela o número informado pelo usuário do programa")
        print(int(input("Digite um numero inteiro: ")))
        os.system('pause')

    elif(numero == 3):
        clear_terminal()
        print("Questão 3 - Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado da seguinte forma: 'Foi informado o valor: X'")
        print("Foi informado o valor: {}".format(int(input("Digite um numero inteiro: "))))
        os.system('pause')

    elif(numero == 4):
        clear_terminal()
        print("Questão 4 - Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela os dois números informados da seguinte forma: 'Voce informou os numeros X e Y'")
        inteiro_1 = int(input("Digite o valor do primeiro número inteiro: "))
        inteiro_2 = int(input("Digite o valor do segundo número inteiro: "))
        print("Os valores informados foram {} e {}".format(inteiro_1,inteiro_2))
        os.system('pause')

    elif(numero == 5):
        clear_terminal()
        print("Questão 5 - Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o número informado formatado com duas casas decimais da seguinte forma: 'Voce informou o numero X.YY'")
        print("Você informou o número: {0:.2f}".format(float(input("Digite um número: "))))
        os.system('pause')

    elif(numero == 6):
        clear_terminal()
        print("Questão 6 - Escreva um programa que solicite ao usuário a temperatura em graus Celsius e ao final apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32")
        celcius = float(input("Digite a temperatura em ºC: "))
        fahrenheit = celcius * 1.8 + 32
        print("A temperatura informada convertida em ºF é: {0:.2f}".format(fahrenheit))
        os.system('pause')

    elif(numero == 7):
        clear_terminal()
        print("Questão 7 - Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final apresente na tela os dois números informados formatando com duas casas decimais somente o número real da seguinte forma: 'Voce informou os numeros N e X.YY'")
        inteiro_1 = int(input("Digite o valor do primeiro número inteiro: "))
        float_1 = float(input("Digite o valor do segundo número real: "))
        print("Os valores informados foram {} e {}".format(inteiro_1,float_1))
        os.system('pause')
    
    elif(numero == 8):
        clear_terminal()
        print("Questão 8 - Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final apresente na tela a letra informada pelo usuário da seguinte forma: 'Voce digitou w'")
        print("Você digitou: {}".format(input("Digite a primeira letra do seu nome: ")))
        os.system('pause')

    elif(numero == 9):
        clear_terminal()
        print("Questão 9 - Escreva um programa que solicite ao usuário o nome de sua cor preferida e ao final apresente na tela a cor informada pelo usuário da seguinte forma: 'Voce gosta da cor AAA'")
        print("Você digitou: {}".format(input("Digite sua cor preferida: ")))
        os.system('pause')

    elif(numero == 10):
        clear_terminal()
        print("Questão 10 - Escreva um programa que solicite ao usuário o nome de uma verdura e uma fruta de sua preferencia e ao final apresente na tela as informações digitadas pelo usuário da seguinte forma: 'Voce gosta de AAAAAAA e BBBBBBB'")
        fruta = input("Digite sua fruta favorita: ")
        verdura = input("Digite sua verdura favorita: ")
        print("Voce gosta de {} e {}".format(fruta,verdura))
        os.system('pause')

    elif(numero == 11):
        clear_terminal()
        print("Questão 11 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o numero informado e na linha de baixo o dobro deste número da seguinte forma: Numero -> X Dobro deste numero -> Y")
        numero_1 = float(input("Digite um número: "))
        print("Número -> {} \n Dobro desse número-> {}".format(numero_1, (numero_1*2)))
        os.system('pause')

    elif(numero == 12):
        clear_terminal()
        print("Questão 12 - Elabore um programa que apresente o quadrado e o cubo do número informado")
        numero_1 = float(input("Digite um número: "))
        print("Número-> {} \n Quadrado desse número-> {} \n Cubo desse número-> {}".format(numero_1,math.pow(numero_1,2), math.pow(numero_1,3)))
        os.system('pause')
    elif(numero == 13):
        clear_terminal()
        print("Questão 13 - Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela a soma dos dois números informados da seguinte forma: 'O numeros N e X somados correspondem a Y'")
        inteiro_1 = int(input("Digite o valor do primeiro número inteiro: "))
        inteiro_2 = int(input("Digite o valor do segundo número inteiro: "))
        print("O numeros {} e {} somados correspondem a {}".format(inteiro_1,inteiro_2,(inteiro_1+inteiro_2)))
        os.system('pause')

    elif(numero == 14):
        clear_terminal()
        print("Questão 14 - Escreva um programa que solicite ao usuário dois números reais e ao final apresente na tela o produto dos dois números informados da seguinte forma: 'O produto dos numeros N e X corresponde a Y'")
        float_1 = float(input("Digite o valor do primeiro número real: "))
        float_2 = float(input("Digite o valor do segundo número real: "))
        print("O produto dos numeros {} e {} corresponde a {}".format(float_1,float_2,(float_1*float_2)))
        os.system('pause')

    elif(numero == 15):
        clear_terminal()
        print("Questão 15 - Escreva um programa que solicite ao usuário dois números reais e ao final apresente na tela o resultado das quatro operações aritméticas básicas.")
        float_1 = float(input("Digite o valor do primeiro número real: "))
        float_2 = float(input("Digite o valor do segundo número real: "))
        print("A multiplicação dos numeros {} e {} corresponde a {}".format(float_1,float_2,(float_1*float_2)))
        print("A adição dos numeros {} e {} corresponde a {}".format(float_1,float_2,(float_1+float_2)))
        print("A subtração dos numeros {} e {} corresponde a {}".format(float_1,float_2,(float_1-float_2)))
        print("A divisão dos numeros {} e {} corresponde a {}".format(float_1,float_2,(float_1/float_2)))
        os.system('pause')

    elif(numero == 16):
        clear_terminal()
        print("Questão 16 - Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.")
        salario = float(input("Digite o valor do salário: "))
        total_vendas = float(input("Digite o total de vendas no mês: "))
        percentual_comissao = float(input("Digite o percentual de comissão: "))
        salario+=(salario*(total_vendas*percentual_comissao/100))
        print("O salário bruto do funcionario no mês foi: {}".format(salario))
        os.system('pause')
        
    else:
        clear_terminal()
        print("Digito invalido!")
        os.system('pause')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_terminal()
    print("Questão 1 - Escreva um programaque apresente na tela a frase: 'Meu primeiro programa!!!'")
    print("Questão 2 - Escreva um programaque solicite ao usuário um número inteiro e ao final apresente na tela o número informado pelo usuário do programa")
    print("Questão 3 - Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado da seguinte forma: 'Foi informado o valor: X'")
    print("Questão 4 - Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela os dois números informados da seguinte forma: 'Voce informou os numeros X e Y'")
    print("Questão 5 - Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o número informado formatado com duas casas decimais da seguinte forma: 'Voce informou o numero X.YY'")
    print("Questão 6 - Escreva um programa que solicite ao usuário a temperatura em graus Celsius e ao final apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32")
    print("Questão 7 - Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final apresente na tela os dois números informados formatando com duas casas decimais somente o número real da seguinte forma: 'Voce informou os numeros N e X.YY'")
    print("Questão 8 - Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final apresente na tela a letra informada pelo usuário da seguinte forma: 'Voce digitou w'")
    print("Questão 9 - Escreva um programa que solicite ao usuário o nome de sua cor preferida e ao final apresente na tela a cor informada pelo usuário da seguinte forma: 'Voce gosta da cor AAA'")
    print("Questão 10 - Escreva um programa que solicite ao usuário o nome de uma verdura e uma fruta de sua preferencia e ao final apresente na tela as informações digitadas pelo usuário da seguinte forma: 'Voce gosta de AAAAAAA e BBBBBBB'")
    print("Questão 11 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o numero informado e na linha de baixo o dobro deste número da seguinte forma: Numero -> X Dobro deste numero -> Y")
    print("Questão 12 - Elabore um programa que apresente o quadrado e o cubo do número informado")
    print("Questão 13 - Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela a soma dos dois números informados da seguinte forma: 'O numeros N e X somados correspondem a Y'")
    print("Questão 14 - Escreva um programa que solicite ao usuário dois números reais e ao final apresente na tela o produto dos dois números informados da seguinte forma: 'O produto dos numeros N e X corresponde a Y'") 
    print("Questão 15 - Escreva um programa que solicite ao usuário dois números reais e ao final apresente na tela o resultado das quatro operações aritméticas básicas.")
    print("Questão 16 - Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.")
    questao(int(input("Digite o número da questão: ")))
    
while True:
    main()