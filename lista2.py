'''
@Lucas Soares Leite - 22955658
https://www.github.com/querneu
'''
import os
import math


def questao(numero):
    if(numero == 1):
        clear_terminal()
        print("Questão 1 - Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que 10 (dez)")
        valor_1 = int(input("Digite um número: "))
        print("O valor é maior que 10" if valor_1 >
              10 else "Valor menor ou igual a 10")
        os.system('pause')

    elif(numero == 2):
        clear_terminal()
        print("Questão 2 - Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior ou igual a dez ou menor que 10 (dez)")
        valor_1 = int(input("Digite um número: "))
        if(valor_1 < 10):
            print("O valor é menor que 10")
            
        elif(valor_1 > 10):
            print("O valor é maior que 10")
            
        else:
            print("O valor é igual a {}".format(valor_1))
        os.system('pause')

    elif(numero == 3):
        clear_terminal()
        print("Questão 3 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que dez, se é menor que dez, ou se é igual a dez")
        valor_1 = int(input("Digite um número: "))
        if(valor_1 < 10):
            print("O valor é menor que 10")
            
        elif(valor_1 > 10):
            print("O valor é maior que 10")
            
        else:
            print("O valor é igual a {}".format(valor_1))
            
        os.system('pause')

    elif(numero == 4):
        clear_terminal()
        print("Questão 4 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é positivo, negativo ou nulo (zero)")
        valor_1 = int(input("Digite um número: "))
        if(valor_1 < 0):
            print("O valor é negativo")
            
        elif(valor_1 > 0):
            print("O valor é positivo")
            
        else:
            print("O valor é nulo")
            
        os.system('pause')
    elif(numero == 5):
        clear_terminal()
        print("Questão 5 - Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo de 3, ou, não é múltiplo de 3")
        numero_1 = int(input("Digite um número inteiro: "))
        mod = numero_1 % 3
        print("O número {} é multiplo de 3".format(numero_1) if(mod == 0)
              else "O número {} Não é multiplo de 3".format(numero_1))
        os.system('pause')
        return 0  # Correção alternativa de escape de valor na memória "Valor inválido"

    elif(numero == 6):
        clear_terminal()
        print(
            "Questão 6 - Refazer o exercício 5, solicitando antes o múltiplo a ser testado")
        numero_1 = int(input("Digite um número inteiro: "))
        multiplo_de = int(input("Digite o valor que deve ser multiplo de: "))
        mod = numero_1 % multiplo_de
        print("O numero {} é multiplo de {}".format(numero_1, multiplo_de) if(
            mod == 0) else "O número {} não é multiplo de {}".format(numero_1, multiplo_de))
        os.system('pause')

    elif(numero == 7):
        clear_terminal()
        print("Questão 7 - Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como par ou ímpar")
        numero_1 = int(input("Digite um número inteiro: "))
        mod = numero_1 % 2
        print("O numero {} é par".format(numero_1) if(mod == 0)
              else "O número {} é impar".format(numero_1))
        os.system('pause')

    elif(numero == 8):
        clear_terminal()
        print("Questão 8 - Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade desse número, caso contrário, imprimir o dobro do número")
        numero_1 = float(input("Digite um número: "))
        print("Metade: {}".format(numero_1/2) if(numero_1 > 20)
              else "Dobro: {}".format(numero_1*2))
        os.system('pause')

    elif(numero == 9):
        clear_terminal()
        print("Questão 9 - Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele")
        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))
        soma = numero_1+numero_2
        print("Quadrado do reultado: {}".format(math.pow(soma, 2))
              if (soma > 10) else "Metade: {}".format(soma/2))
        os.system('pause')

    elif(numero == 10):
        clear_terminal()
        print("""Questão 10 - O sistema de avaliação de determinada disciplina é composto por três provas. 
                A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. 
                Considerando que a média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno desta disciplina e dizer se o aluno foi aprovado ou não""")
        nota_1 = float(input("Digite a primeira nota: "))
        nota_2 = float(input("Digite a segunda nota: "))
        nota_3 = float(input("Digite a terceira nota:"))
        media = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5)/10
        print("Nota {}, aprovado!".format(media) if (
            media >= 6) else "Reprovado: {}".format(media))
        os.system('pause')

    elif(numero == 11):
        clear_terminal()
        print("Questão 11 - Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da pessoa mais pesada")
        nome_1 = input("Digite o nome da primeira pessoa: ")
        peso_1 = input("Digite o peso da primeira pessoa: ")
        nome_2 = input("Digite o nome da segunda pessoa: ")
        peso_2 = input("Digite o peso da segunda pessoa: ")
        print("{} é mais pesado, com {}Kg".format(nome_1, peso_1) if (
            peso_1 > peso_2) else "{} é mais pesado, com {}Kg".format(nome_2, peso_2))
        os.system('pause')

    elif(numero == 12):
        clear_terminal()
        print("Questão 12 - Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não")
        numero_1 = int(input("Digite um numero: "))
        print("{} está entre 20 e 90".format(numero_1) if (20 <= numero_1 <=
                                                           90) else "O numero {} não está entre 20 e 90".format(numero_1))
        os.system('pause')

    elif(numero == 13):
        clear_terminal()
        print("Questão 13 - Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se são iguais")
        primeiro = int(input("Primeiro numero: "))
        segundo = int(input("Segundo numero : "))

        #maior
        if (segundo > primeiro):
            print("Menor: {}".format(primeiro))
            print("Maior: {}".format(segundo))

        elif (primeiro > segundo):
            print("Maior: {}".format(primeiro))
            print("Menor: {}".format(segundo))
            
        #menor
        elif (segundo < primeiro):
            print("Maior: {}".format(primeiro))
            print("Menor: {}".format(segundo))
            
        elif (primeiro < segundo):
            print("Menor: {}".format(primeiro))
            print("Maior: {}".format(segundo))
            
        #igual
        else:
            print("{} e {} são iguais.".format(primeiro, segundo))
            
        os.system('pause')


    elif(numero == 14):
        clear_terminal()
        print("""Questão 14 - Escreva um programa em linguagem C que solicite ao usuário a média para aprovação em um curso 
            e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao final imprima a frase: 
            "O aluno XXXXX foi aprovado com media YY" considerando o gênero do(a) aluno(a) e se foi aprovado(a) ou reprovado(a)""")
        media = float(input("Digite a média para aprovação: "))
        nome =  input("Digite seu nome: ")
        sexo =  input("Digite seu sexo; M para masculino, F para feminino.\n")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        total = (nota1+nota2+nota3)/3
        if(sexo == 'M'):
            if(total < media):
                print("O aluno {}, foi reprovado com media {}".format(nome, total))
            if(total >= media):
                print("O aluno {}, foi aprovado com media {}".format(nome,total))
        elif(sexo == 'F'):
            if(total < media):
                print("A aluna {}, foi reprovada com media {}".format(nome, total))
            if(total >= media):
                print("A aluna {}, foi aprovada com media {}".format(nome,total))
        os.system('pause')

    else:
        clear_terminal()
        print("Digito invalido!")
        os.system('pause')


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_terminal()
    print("Questão 1 - Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que 10 (dez)")
    print("Questão 2 - Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior ou igual a dez ou menor que 10 (dez)")
    print("Questão 3 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que dez, se é menor que dez, ou se é igual a dez")
    print("Questão 4 - Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é positivo, negativo ou nulo (zero)")
    print("Questão 5 - Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo de 3, ou, não é múltiplo de 3")
    print("Questão 6 - Refazer o exercício 5, solicitando antes o múltiplo a ser testado")
    print("Questão 7 - Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como par ou ímpar")
    print("Questão 8 - Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade desse número, caso contrário, imprimir o dobro do número")
    print("Questão 9 - Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele")
    print("""Questão 10 - O sistema de avaliação de determinada disciplina é composto por três provas. 
            A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. 
            Considerando que a média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno desta disciplina e dizer se o aluno foi aprovado ou não""")
    print("Questão 11 - Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da pessoa mais pesada")
    print("Questão 12 - Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não")
    print("Questão 13 - Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se são iguais")
    print("""Questão 14 - Escreva um programa que solicite ao usuário a média para aprovação em um curso 
            e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao final imprima a frase: 
            "O aluno XXXXX foi aprovado com media YY" considerando o gênero do(a) aluno(a) e se foi aprovado(a) ou reprovado(a)""")
    questao(int(input("Digite o número da questão: ")))


while True:
    main()
