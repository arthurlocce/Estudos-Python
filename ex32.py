'''Elabore um programa que possua duas funções:
• Uma função que leia um número inteiro
• Uma função que some três valores inteiros
• O programa deverá ler três valores inteiros e imprimir a soma
desses valores, usando as funções acima'''

def ler_num():
    num=int(input('Digite um número: '))
    return num

def somar3(n1,n2,n3):
    soma= n1 + n2 + n3
    return soma


n1=ler_num()
n2=ler_num()
n3=ler_num()
resultado=somar3(n1,n2,n3)

print(f'A soma desses três números é: {resultado}')





