quant=int(input('Quantos números deseja digitar?(>=10): '))
cont=1
maior=0
menor=0
aux=0


while cont <= quant:
    num = int(input('Digite um número:'))
    if cont == 1:
        menor = maior = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    cont= cont + 1


print(f'Maior={maior}\nMenor={menor}')