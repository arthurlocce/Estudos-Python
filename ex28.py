print('|Mostre os dois maiores números digitados pelo usuário|')
quant = 10
cont = 1
_1nmaior = 0
_2nmaior = 0
while cont <= quant:
    num = float(input('Digite um número: '))
    if num > _1nmaior:
        _2nmaior = _1nmaior
        _1nmaior = num
    elif num>_2nmaior:
        _2nmaior = num
    cont = cont + 1
print('O maior número é:', _1nmaior)
print('O segundo maior número é:', _2nmaior)