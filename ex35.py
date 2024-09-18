'''Elabore um programa que leia um número inteiro e construa duas
funções: uma que some os dígitos desse número inteiro e outra que
determine o maior digito desse número. Exemplo: número = 1063,'''

def soma_digitos(num):
    soma=0
    for x in num:
        soma= int(x) + soma
    return soma

def maior_digito(num):
    maior=0
    for x in num:
        if int(x)>maior:
            maior=int(x)
    return maior

num=input('Digite um número:')
soma=soma_digitos(num)
maior=maior_digito(num)
print(f'A soma dos dígitos de {num} é {soma} e o maior número dentre os dígitos é {maior}.')



