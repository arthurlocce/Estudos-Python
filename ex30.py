lista=[]
def inverter(num):
    for digito in num:
        lista.append(int(digito))

    for digito in reversed(lista):
        inverso=print(f'{digito}', end='')
    return inverso

num=(input('Digite um número: '))
num_inv=inverter(num)



