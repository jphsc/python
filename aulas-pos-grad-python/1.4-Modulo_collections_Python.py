# módulo collections
# collections defaultdict é um dicionário, convert arrays em dicionários sem se importar com a chave
from collections import defaultdict
cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]
cores_fav = defaultdict(list)

for chave, valor in cores:
    cores_fav[chave].append(valor)
print(cores_fav)

# collection Counter faz a contagem de itens em um array
from collections import Counter
cores = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']
contador = Counter(cores)
print(contador)

# collections deque transforma o array em uma lista duplamente ordenada (de duas pontas), podendo
# excluir ou add itens em qualquer ponta
from collections import deque
fila = deque() # or fila = deque('123') -> vai criar um deque com 3 elementos
fila.append('1')
fila.append('2')
fila.append('3')
print(fila)

# exclui elemento da direita
fila.pop()
print(fila)

# adiciona elemento na direita
fila.append('3')
print(fila)

# exclui elemento da esquerda
fila.popleft()
print(fila)

# adiciona elemento na esquerda
fila.appendleft('1')
print(fila)

# collections namedtuple
from collections import namedtuple
Conta = namedtuple('Conta', ['numero', 'titular', 'saldo', 'limite'])
conta = Conta('123-4', 'João', 1000.0, 1000.0)
print(conta)
# saída: Conta(numero='123-4', titular='João', saldo=1000.0, limite=1000.0)
print(conta.titular) # saída: João
print(conta.count('João'))

newf = deque('123')
print(newf)
print(list[newf])