pint=0
sint=0
tint=0
qint=0

while True:
    num=float(input('Digite um número(negatio para sair):'))

    if num >=0 and num <=25:
        pint= pint + 1

    if num >=26 and num <=50:
        sint= sint + 1

    if num >=51 and num <=75:
        tint= tint + 1

    if num >=76 and num <=100:
        qint= qint + 1


    if num<0:
        break

print(pint)
print(sint)
print(tint)
print(qint)