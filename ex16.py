n1=float(input('Digite o valor da nota 1(máx 10): '))
while n1>10:
    print('Erro')
    n1 = float(input('Digite o valor da nota 1(máx 10): '))
p1=float(input('Digite o valor do peso 1: '))
n2=float(input('Digite o valor da nota 2(máx 10): '))
while n2>10:
    print('Erro')
    n2 = float(input('Digite o valor da nota 2(máx 10): '))
p2=float(input('Digite o valor do peso 2: '))

media= ((n1*p1)+(n2*p2)) / p1+ p2

if (media>=7):
    print('Aprovado')

if (media==10):
    print('Aprovado com louvor')

if media <7:
    print('Reprovado')