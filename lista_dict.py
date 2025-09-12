lista = [1, 3, 7, 4, 2, 8] # lista com valores numericos

lista.append(9) # adicionar um elemento a lista
lista[2] = 5 # atualizar um elemento por indice
lista.remove(3) # remover o elemento 3

print(lista)

dicionario = {
    'produto': 'celular'
} # dicionario vazio

dicionario['preço'] = 1500 # adicionando nova chave 'preço com valor 1500
dicionario['preço'] = 1200 # atualizando a chave 'preço' para o valor 1200
del dicionario['produto'] # deletando uma chave 'produto'e seu valor
print(dicionario)

