def suc_ant(num):
    suc=num+1
    ant=num-1
    return suc,ant

num=int(input('Digite um número: '))
suc,ant=suc_ant(num)

print(f'O número {num} tem como antecessor {ant} e sucessor {suc}')