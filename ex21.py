quant=int(input('Quantos números deseja inserir?'))
while quant <=0:
    print('Erro')
    quant = int(input('Quantos números deseja inserir?'))
cont= 1
soma_par=0
impar=0
while cont<=quant:
    num=float(input('Digite um número'))
    if num % 2 ==0:
        soma_par= soma_par + num
    else:
        impar= impar + 1
    cont= cont + 1

print(soma_par)
print(impar)