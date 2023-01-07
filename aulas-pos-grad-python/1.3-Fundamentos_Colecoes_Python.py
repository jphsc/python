# listas -> Array de elementos
lista1 = ['Rafael Costa', 28, '11/01/93', 'Henry', 'male', True]
print(f'Posição 2 da lista: print(lista[posicao]): {lista1[1]}')

# retornando o index da lista
indexValor = lista1.index(1)
print(indexValor)

lista2 = [11, 12, [23, 24, [35, 36]]]
print(f'Acessando o segundo item do primeiro sub array: {lista2[2][1]}')

lista3 = [1, 20, 5, 90, 4]
# retornando o maio max(), menor min() e soma sum()
print(f'Maior: {max(lista3)}')
print(f'Menor: {min(lista3)}')
print(f'Soma: {sum(lista3)}')

# inserindo no final do array
lista3.append(10)
print(f'incluir no final do array = append(valor): {lista3}')

# inserindo em posição específica (exemplo na nova posição valor 20 na segunda posição)
lista3.insert(1, 'vinte')
print(f'Inserir em posição específica: insert(posição, valor): {lista3}')

# para excluir um item qualquer da lista ou uma faixa del lista[x] ou del lista [1:2]
del lista3[1]
print(f'excluir um item por index ou um faixa = del list[index] ou list[0:2]: {lista3}')

# excluir o último item da lista
lista3.pop()
print(f'Excluir o último item = pop(): {lista3}')

# excluir o item da lista por seu valor
lista3.remove(4)
print(f'Excluir por valor = remove(valor): {lista3}')

# a função clear limpa a lista lista.clear()
# lista3.clear()

# reagrupar (sortear) os itens
lista4 = [1, 20, 5, 90, 4, 10]
print(f'Posição original: {lista4}')
lista4.sort()
print(f'Sortear os itens: sort() > Posição sorteada: {lista4}')

# inverter a lista
print(f'Posição original: {lista4}')
lista4.reverse()
print(f'Inverter os itens: reverse() > Posição revertida: {lista4}')

# tamanho da lista
print(f'len(list): Tamanho da lista: {len(lista4)} itens')

# loops
lista5 = [1, 'vinte', 20, 5, 90, 4, 10]
for item in range(0, len(lista5)):
    print(f'Item da lista: {lista5[item]} de índice')
print('*-' * 40)

for item in lista5:
    print(f'Impressão de cada item da lista5: {item}')
print('*-' * 40)
# tuplas são conjuntos de itens (array) com valor e separados por vírgulas, iguais listas, porém imutáveis
tupla1 = tuple("aeiou")
tupla2 = "a", "e", "i", "o", "u"
tupla3 = ("a", "e", "i", "o", "u")
tupla = ()
print(f'Exemplo de impressão de tupla:{tupla1}')
print(tupla2[-1])

# dicionários associativos são os objetos do tipo obj = { chave : valor }
dicio = {'nome': 'Rafael', 'idade': 29, 'nascimento': '11/01/1993', 'altura': 1.79, 'adulto': True}
print(f'Dicionário: {dicio}')
# dicionários também podem ser criados usando a palavra reservada dict('chave': 'valor')
# valores de dicionários são acessados informando a chave
print(f"Valor da chave nome acessado direto: {dicio['nome']}")

# dicio.get(chave) para obter um valor e atribuir a outra variável
nome = dicio.get('nome')
print(f"Valor da chave nome acessado pelo get: {nome}")
# alterações de valores são feitos diretamente informando a chave
dicio['nome'] = 'Henrique'
print(dicio)

# inclusões de chaves e valores pelo dicio.update({'chave1':valor1, ..., 'chaveN':valorN})
dicio.update({'sexo': 'M'})
print(dicio)

# exclusão de conjunto com: del dicio['chave']
del dicio['adulto']
print(dicio)

# exclusão de conjunto exibindo msg caso não encontrado: dicio.pop('chave', 'MSG')
sexo = dicio.pop('sexo', 'Atributo sexo não localizado')
print(sexo)
adulto = dicio.pop('adulto', 'Atributo adulto não localizado')
print(adulto)
print(dicio)

# percorrendo o dicionário com for
for chave in dicio:
    print(f'Valor do item do dicionário: {dicio[chave]} - Chave do item *{chave}*')

# dicio.keys(), dicio.values() e dicio.items() -> obtem respectivamente: chaves, valores e items do dicionário
print(f'Chaves: {dicio.keys()}')
print(f'Valores: {dicio.values()}')
print(f'Itens: {dicio.items()}')