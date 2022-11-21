
# retorno = map(funcao, collections)
def dobro(n):
    return n * 2

numeros = (5, 4, 3, 2, 1)
numerosDobrados = map(dobro, numeros) # usando map
print(tuple(numerosDobrados)) # converter para uma collection para ser facilmente entendível

print('-' * 42)
print('Exemplificando com map\n')
def capitalizar(n):
    return n.capitalize()
nome = 'rafael', 'henrique', 'costa'
nomeM = map(capitalizar, nome)
print(tuple(nomeM))

print('-' * 42)

import random
total_questoes = 10
alternativas = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
candidatos = {0: 'Marilda', 1: 'Marcelo', 2: 'Matheus'}

def simular_questoes(grade, total):
    global alternativas
    n = 0
    while n < total:
        n += 1
        resposta = random.randint(0, 4)
        grade.append(alternativas[resposta])
    return grade

def verificar_acertos(gabarito, candidato):
    if (gabarito == candidato):
        return '1'
    else:
        return '0'

gabarito = []
gabarito = simular_questoes(gabarito, total_questoes)
correcoes = []
maior_acerto = 0
total_candidatos = len(candidatos)
for indice in range(total_candidatos):
    print(f'Gabarito: {gabarito}')
    candidato = []
    candidato = simular_questoes(candidato, total_questoes)
    print(f'{candidatos[indice]}: {candidato}')
    correcao = tuple(map(verificar_acertos, gabarito, candidato))
    acertos = correcao.count('1')
    print(f'{candidatos[indice]}: { correcao } = {acertos} acertos.')
    if acertos > maior_acerto:
        maior_acerto = acertos
        vencedor = candidatos[indice]
        print("") # linha em branco para facilitar a visualização
        print(f'O vencedor é {vencedor} com {maior_acerto} acertos.')