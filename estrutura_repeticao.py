sequencia = [] # criei uma lista vazia

for i in range(1, 11): # cria um loop que percorre de 1 á 10
    sequencia.append(i) # adiciona o valor q esta sendo passado no looping
print(sequencia) # mostra o resultado depois que o looping é finalizado

lista_pares = [] # cria lista vazia para armazenar os valores pares
soma_pares = 0 # variavel para controlar a soma dos numeros

while soma_pares < 20:  
    novo_valor = len(lista_pares) * 2 + 2 # calcula o proximo numero par
    lista_pares.append(novo_valor) # adiciona o numero par a lista de pares
    soma_pares += sum(lista_pares) # atualiza a soma total da lista 
    
print(f'A lista gerada foi: {lista_pares}') # mostra os itens da lista
print(f'A soma é {soma_pares}') # mostra a soma final