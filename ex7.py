print('|Cálculo de IMC|')
peso=float(input('Me de o valor do seu peso (kg): '))
altura=float(input('Me de o valor da sua altura (m): '))

print(f'IMC= {peso/(altura**2):.2f}')