plano=int(input('Qual é o seu plano de trabalho? '))
while plano != 1 and plano != 2 and plano != 3:
    print('Erro')
    plano = int(input('Qual é o seu plano de trabalho? '))
sa=float(input('Qual é o seu salário atual?'))

if plano==1:
    sa= sa*1.1

if plano==2:
    sa = sa * 1.15

if plano == 3:
    sa= sa* 1.2

print(f'Seu novo salário é de R$ {sa:.2f}')