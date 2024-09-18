''''Elabore um programa que leia e armazene 10 números reais, o
programa deverá informar
• A média dos elementos
• O maior e o menor elemento
• A quantidade de números maiores que 29.
• Imprimir a lista lida
Python'''
media=0
soma=0
numeros=[]
maior=0
quant=0
menor=0

for x in range(3):
    num=int(input('Digite um número: '))
    numeros.append(num)
    soma=soma+num
media=soma/10

for num in numeros:
    menor=num
    if num > maior:
        maior=num

    if num > 29:
        quant = quant + 1

    for menor_num in numeros:
        if menor_num < menor:
            menor=menor_num


print(f'A média dos números da lista é {media} o seu maior elemento é {maior} e seu menor elemento é {menor} e a quantidade de números da lista maior que 29 é: {quant}')


