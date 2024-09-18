comp=float(input('Qual é a medida do comprimento da sala (em metro)? '))
larg=float(input('Qual é a medida da largura da sala (em metro)? '))
pmetro2=float(input('Qual é o preço do metro quadrado do carpete?'))
print(f'O custo total para forrar o piso da sala é de: R${(comp*larg)*pmetro2:.2f}')