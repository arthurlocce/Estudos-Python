num=float(input('Digite um número:'))
cont=1
divisiveis_por_4=1

while cont<=num:
    num = num - 1
    if num % 4 == 0:
        print(num)
    cont= cont + 1
