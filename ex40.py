'''Construa um programa que seja constituído de uma lista
GAB de 10 elementos caracteres ( esta lista pode ser
constituída somente dos caracteres a, b, c, d e e. O programa
irá ler o nome e a resposta de 10 alunos de uma turma e
deverá imprimir a nota de cada aluno (considerando que
cada questão vale 1,0 ponto). O programa deverá também
imprimir a média da sala'''

gab=['a','b']
nomes=[]
acerto=0
resp_geral=[]
resp_paluno=[]
acertos=[]

for x in range (2):
    nome=str(input('Digite seu nome: '))
    nomes.append(nome)
    resp_paluno = []
    for y in range (2):
        resp=str(f'Qual foi sua resposta na questão {y}?')
        resp_paluno.append(resp)
    resp_geral.append(resp_paluno)

for aluno in resp_geral:
    for sublista in range (len(aluno)):
        print(aluno[sublista])
