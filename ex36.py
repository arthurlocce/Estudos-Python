'''Um número é perfeito se a soma dos seus divisores, com exceção dele
mesmo, é igual a ele. Exemplo: número 6, os divisores de 6 são 1, 2,
3 e 6. Somando-se 1 + 2 + 3 =6. Portanto 6 é um número perfeito.
Elabore um programa que leia um número e usando uma função
determine se ele é perfeito'''


num=int(input('Digite um número:'))

def num_pft(num):
    soma_div=0
    cont=1
    while cont<num:
        if num % cont==0:
            soma_div= soma_div + cont
        cont= cont + 1
    if soma_div==num:
        resp=print('É um número perfeito.')
    else:
        resp = print('Não é um número perfeito.')

    return resp

soma_divisores=num_pft(num)