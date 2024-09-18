valor_compra=float(input('Digite o valor da compra'))
valor_pago=float(input('Digite o valor pago do cliente'))
dif= valor_pago-valor_compra

cédulas_20= (dif)//20
cédulas_10= (dif % 20)//10
cédulas_5= ((dif % 20)%10)//5
cédulas_1= (((dif % 20)%10)%5)//1
print(f'Cédulas de R$ 20= {cédulas_20} \nCédulas de R$ 10= {cédulas_10} \nCéduças de R$ 5= {cédulas_5} \nCédulas de R$ 1= {cédulas_1} ')