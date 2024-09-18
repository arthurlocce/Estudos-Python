a=float(input('Digite o valor do coeficiente A:'))
b=float(input('Digite o valor do coeficiente B:'))
c=float(input('Digite o valor do coeficiente C :'))
d=float(input('Digite o valor do coeficiente D:'))
e=float(input('Digite o valor do coeficiente E:'))
f=float(input('Digite o valor do coeficiente F:'))
x=0
y=0



while a<= 0 or b<= 0 or c<= 0 or d<= 0 or e<= 0 or f<= 0:
    print('Erro, nenhum coeficiente pode ser menor ou igual a zero!')
    a = float(input('Digite o valor do coeficiente A:'))
    b = float(input('Digite o valor do coeficiente B:'))
    c = float(input('Digite o valor do coeficiente C :'))
    d = float(input('Digite o valor do coeficiente D:'))
    e = float(input('Digite o valor do coeficiente E:'))
    f = float(input('Digite o valor do coeficiente F:'))

x= (c*e)-(b*f)/ (a*e)-(b*d)
y= (a*f)-(c*d)/(a*e)-(b*d)

if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
    print(f'x= {x}\ny= {y}')
else:
    print (f'O sistema não tem solução')