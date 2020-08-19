'''
@Lucas Soares Leite - 22955658
https://www.github.com/querneu
'''
import os, sys
import math


def questao(numero):
    if(numero == 1):
        clear_terminal()
        print("Questão 1 - Elabore um algoritmo que imprima na tela lado a lado o texto 'Hello World!' 10 vezes.")
        for x in range(10):
            print("Hello world!", end="  ")
        print("") #Fix para escape de execução apos o loop#
        os.system('pause')

    elif(numero == 2):
        clear_terminal()
        print("Questão 2 - Elabore um algoritmo que imprima na tela o texto 'Hello World!' 10 vezes, um por linha.")
        for x in range(10):print("Hello world!")
        os.system('pause')

    elif(numero == 3):
        clear_terminal()
        print("Questão 3 - Elabore um algoritmo que imprima todos os números inteiros de 1 até 100 inclusive.")
        for x in range(100):print(x+1)
        os.system('pause')

    elif(numero == 4):
        clear_terminal()
        print("Questão 4 - Elabore um algoritmo que imprima 100 vezes o texto '1- Hello World!' com o número. ")
        for x in range(100):print("{} Hello world!".format(x+1))
        os.system('pause')

    elif(numero == 5):
        clear_terminal()
        print("Questão 5 - Elabore um algoritmo que imprima todos os números decrescentes de 100 até 0 inclusive.")
        for x in reversed(range(101)):print(x)
        os.system('pause')

    elif(numero == 6):
        clear_terminal()
        print("Elabore um algoritmo que imprima todos os números pares inteiros de 1 até 1000")
        for x in range(1000):
            resto = x%2
            if resto == 0:
                print("{}".format(x))
        os.system('pause')

    elif(numero == 7):
        clear_terminal()
        print("Elabore um algoritmo que imprima todos os números pares inteiros de 1 até 1000")
        for x in reversed(range(1000)):
            resto = x%2
            if resto == 1:
                print("{}".format(x))
        os.system('pause')

    elif(numero == 8):
        clear_terminal()
        print("Questão 8 - Elabore um algoritmo que imprima a soma dos 100 primeiros números inteiros positivos.")
        contador = 0
        for x in range(100):
            contador+=x
        print("{}".format(contador))
        os.system('pause')

    elif(numero == 9):
        clear_terminal()
        print("Questão 9 - Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade de vezes que o texto 'Hello World!' será impresso na tela, um em cada linha.")
        x = int(input("Digite a quantidade de vezes que o 'Hello World!' será repetido: "))
        for contador in range(x):
            print("Hello World.")
        os.system('pause')

    elif(numero == 10):
        clear_terminal()
        print("Questão 9 - Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade de vezes que o texto 'Hello World!' será impresso na tela, um em cada linha.")
        palavra = input("Digite a palavra a ser repetida: ")
        x = int(input("Digite a quantidade de vezes que a palavra {} será repetido: ".format(palavra)))
        for contador in range(x):
            print(palavra)
        os.system('pause')

    elif(numero == 11):
        clear_terminal()
        print("Questão 11 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos. Em seguida, leia n números (conforme o valor informado anteriormente) e imprima a soma e a média aritmética dos números informados.")
        x = int(input("Digite a quantidade de numeros a serem lidos: "))
        numeros = []
        for contador in range(x):
            numeros.append(input("Digite um numero: "))
        total = 0
        for n in numeros:
            total += int(n)
        media = total/len(numeros)
        print("Soma: {}, Média: {}".format(total, media))
        os.system('pause')

    elif(numero == 12):
        clear_terminal()
        print("Questão 12 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa mais velha")
        x = int(input("Digite a quantidade de regitros a serem lidos: "))
        pessoa = {}
        lista = []
        for i in range(x):
            pessoa['nome']  = input("Digite um nome: ")
            pessoa['idade'] = int(input("Digite uma idade: "))
            lista.append(pessoa.copy())
        pessoa_maior_idade = max(lista, key=lambda x:x['idade'])
        print("Pessoa mais velha: {}".format(pessoa_maior_idade['nome']))
            

        os.system('pause')
    elif(numero == 13):
        clear_terminal()
        print("Questão 13 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados.")
        x = int(input("Digite a quantidade de regitros a serem lidos: "))
        pessoa = {}
        lista = []
        for i in range(x):
            pessoa['nome']  = input("Digite um nome: ")
            pessoa['sexo'] = input("Digite seu sexo: [M] para masculino e [F] para feminino: ")
            pessoa['idade'] = int(input("Digite uma idade: "))
            lista.append(pessoa.copy())
        idades_m = ([pessoa['idade'] for pessoa in lista if pessoa['sexo'] == 'M'])
        idades_f = ([pessoa['idade'] for pessoa in lista if pessoa['sexo'] == 'F'])
        media_m = sum(idades_m) / len(idades_m)
        media_f = sum(idades_f) / len(idades_f)
        print("Média de pessoas do sexo M: {}".format(media_m))
        print("Média de pessoas do sexo F: {}".format(media_f))
        os.system('pause')

    elif(numero == 14):
        clear_terminal()
        print("Questão 14 - Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o maior e o menor deles.")
        numeros = []
        for i in range(10):
            numeros.append(float(input("Digite um numero: ")))
        menor = min(numeros)
        maior = max(numeros)
        print("Maior: {}, Menor: {}".format(maior,menor))
        os.system('pause')

    elif(numero == 15):
        clear_terminal()
        print("Questão 15 - Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente.")
        numeros= []
        for i in iter(int, 1):
            numeros.append(float(input("Digite um numero: (Digite 0 para terminar): ")))
            if numeros[i-1] == 0:
                print("Ordem crescente: ")
                print(sorted(numeros))
                break
            else:
                continue

        os.system('pause')

    elif(numero == 16):
        clear_terminal()
        print("Questão 16 - Escreva um programa que vá solicitando as idades dos alunos da sala até que todos sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de 18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana.")
        idades= []
        for i in iter(int, 1):
            idades.append(float(input("Digite uma idade: ")))
            sair = input("Gostaria de terminar? [S] para sim e [N] para Não: ")
            if sair == 'S':
                mais_novo = min(idades)
                mais_velho = max(idades)
                maioridade = 0
                menoridade = 0
                ate_dezoito = 0
                for i in idades:
                    if i > 18:
                        maioridade+=1
                    elif i< 18:
                        menoridade+=1
                    elif i == 18:
                        ate_dezoito+=1
                media = sum(idades) / len(idades)
                lista_ordenada = sorted(idades)
                mediana = lista_ordenada[len(idades)//2]
                print("Mais novo tem: {}, mais velho tem: {}, quantidade maior de 18: {}, quantidade menor de 18: {}, quantidade com 18: {}, media aritmética: {}, mediana: {}".format(mais_novo,mais_velho, maioridade, menoridade,ate_dezoito, media,mediana))
                break
            else:
                continue
        os.system('pause')

    else:
        clear_terminal()
        print("Digito invalido!")
        os.system('pause')


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_terminal()
    print("Questão 1 - Elabore um algoritmo que imprima na tela lado a lado o texto 'Hello World!' 10 vezes.")
    print("Questão 2 - Elabore um algoritmo que imprima na tela o texto 'Hello World!' 10 vezes, um por linha.")
    print("Questão 3 - Elabore um algoritmo que imprima todos os números inteiros de 1 até 100 inclusive.")
    print("Questão 4 - Elabore um algoritmo que imprima 100 vezes o texto '1- Hello World!' com o número. ")
    print("Questão 5 - Elabore um algoritmo que imprima todos os números decrescentes de 100 até 0 inclusive.")
    print("Questão 6 - Elabore um algoritmo que imprima todos os números pares inteiros de 1 até 1000.")
    print("Questão 7 - Elabore um algoritmo que imprima todos os números ímpares de 1000 até 0.")
    print("Questão 8 - Elabore um algoritmo que imprima a soma dos 100 primeiros números inteiros positivos.")
    print("Questão 9 - Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade de vezes que o texto 'Hello World!' será impresso na tela, um em cada linha.")
    print("Questão 10 - Elabore um algoritmo que solicite ao usuário uma palavra e um número inteiro que indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada linha.")
    print("Questão 11 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos. Em seguida, leia n números (conforme o valor informado anteriormente) e imprima a soma e a média aritmética dos números informados.")
    print("Questão 12 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa mais velha")
    print("Questão 13 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados.")
    print("Questão 14 - Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o maior e o menor deles.")
    print("Questão 15 - Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente.")
    print("Questão 16 - Escreva um programa que vá solicitando as idades dos alunos da sala até que todos sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de 18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana.")
    questao(int(input("Digite o número da questão: ")))


while True:
    main()
