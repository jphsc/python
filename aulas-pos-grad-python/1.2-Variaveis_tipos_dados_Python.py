# inteiro
numero_int = 10
# float
numero_float = 2.5

# boolean
booleano = True

# string
texto = 'Bom dia!'

# arrays
lista = [1, 2, 3, 'nome']
print(lista)

# saída de dados
print('Saída de dados 1')
print('Saída de dados usando variáveis. ' + texto)

# entrada de dados
# nome = input('Informe seu nome: ')
# print(f'Seu nome é: {nome}')

# Saída formatada
nome = 'Rafael'
print(f'S1 - Seu nome é: {nome}')
print("S2 - Olá {}, seja bem-vindo!".format(nome))
print('S3 - ' + nome + ', seja bem-vindo!')

# para retornar o tipo de uma variável
print(type(texto))


# declarando e chamando funções
def soma(a, b):
    a = a
    b = b
    resultado = a + b
    print('Resultado: ' + str(resultado))

soma(10, 20)
