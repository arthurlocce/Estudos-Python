print('|Reajuste Salarial')
sa=float(input('Qual é o seu salário atual?'))
percentual=float(input('Qual foi o percentual de reajuste?'))

print(f'O novo salário equivale a R$ {sa+(sa*(percentual/100)):.2f}')