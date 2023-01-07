# módulo collections
# collections defaultdict é um dicionário, converte arrays em dicionários sem se importar com a chave
from collections import defaultdict
cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]
cores_fav = defaultdict(list)

for chave, valor in cores:
    cores_fav[chave].append(valor)
print(f'Cores_Fav: {cores_fav}')

# collection Counter faz a contagem de itens em um array
from collections import Counter
cores = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']
contador = Counter(cores)
print(f'Contador: {contador}')

# collections deque transforma o array em uma lista duplamente ordenada (de duas pontas), podendo
# excluir ou add itens em qualquer ponta
from collections import deque
fila = deque() # or fila = deque('123') -> vai criar um deque com 3 elementos
fila.append('1')
fila.append('2')
fila.append('3')
print(f'Imprimindo item do tipo deque: {fila}')  # imprimir o deque lista com valores 1,2,3

# exclui elemento da direita
fila.pop()
print(fila)

# adiciona elemento na direita
fila.append('#')
print(fila)

# exclui elemento da esquerda
fila.popleft()
print(fila)

# adiciona elemento na esquerda
fila.appendleft('a')
print(fila)

# collections namedtuple
# namedtuples é util para substituir a criação de classes básicas e provém alto desempenho
from collections import namedtuple
# NomeNovoTipo = namedtuple('NomeNovoTipo', 'Nom Dos Campos') > Nome Dos Campos pode ser uma string ou um array de strings
Conta = namedtuple('Conta', ['numero', 'titular', 'saldo', 'limite'])
conta = Conta('123-4', 'João', 1000.0, 1000.0)  # estamos criando um objeto conta do tipo Conta
print(conta)
# saída: Conta(numero='123-4', titular='João', saldo=1000.0, limite=1000.0)
print(conta.titular) # saída: João
print(conta.count('João'))

# deque() é uma generalização e filas e pilhas, permitindo utilizar os mésmos atributos: appends, pops, insert, rotate, etc
newf = deque('123')
newf.appendleft('x')
print(f'Printando o deque newf: {newf}')
newf.append('b')  # adicionando elemento à direita no deque
newf.appendleft('a')  # adicionando elemento à esquerda no deque
print(f'Inclusões a esquerda (appendleft(a)) e à direita (append(b)): {newf}')
newf.pop()  # remove à direita (último)
newf.popleft()  # remove à esquerda (primeiro)
print(f'Remoções à direita (pop()) e a esquerda (popleft()): {newf}')
print(f'NomeDeque[-1] retorna o item mais à direita: {newf[-1]}')
print(f'NomeDeque[1] retorna o item mais à esquerda: {newf[0]}')
fnew = list(reversed(newf))
print(f'reversed(NomeDeque) > Inverte o deque: {fnew}')
newf.extend("!@#")
print(f'NomeDeque.extend("valoresJuntos") > Adiciona ao deque a partir do que já existe: {newf}')
