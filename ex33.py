'''Elabore um programa que leia dois números inteiros e uma função
que some todos os valores inteiros contidos no intervalo entre esses
dois números'''



def soma_valores_intervalo(n1,n2):
    soma=0
    if n1>n2:
        while n2!=n1:
            n2= n2 + 1
            if n2!=n1:
                soma= soma + n2

    elif n2!=n1:
        while n1<n2:
            n1= n1 + 1
            if n1 != n2:
                soma= soma + n1

    return soma

n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
soma_int=soma_valores_intervalo(n1,n2)

print(f'A soma dos números entre {n1} e {n2} é {soma_int}')