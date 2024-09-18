'''Elabore um programa que leia um número inteiro e uma função que
calcule o seu fatorial'''



def fatorial(num):
    fat=1
    while num>1:
        fat=fat*num
        num=num-1

    return fat
num=int(input('Digite um número: '))
fat_num=fatorial(num)

print(f'O fatorial de {num} é {fat_num}')