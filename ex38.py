'''Construa um programa em Python que receba uma lista de 15
inteiros, via teclado e um número. O programa deve informar se
o número existe ou não na lista'''

lista=[1,5,4,7,85,96,32,1,4,58,74,13,69,78,59]

num=int(input('Qual número deseja saber se consta na lista? '))
if num in lista:
    print(f'Está presente na posição {lista.index(num)} da lista!')