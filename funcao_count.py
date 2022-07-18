#Um jeito fácil de contar o número de ocorrências de um determinado elemento
# em uma lista é a função .count()

valores = [0,0,0,1,2,3,4]

print(valores.count(0))

#O código acima nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela.

#Utilizando a função .count() podemos por exemplo, detectar quantas letras ainda faltam para
# o nosso usuário preencher:

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

#Uma outra função que pode ser bastante útil é a função .index(), que
#nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista, veja:

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

#O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista
# frutas (lembre-se nas listas começamos a contar do índice 0).
#Só tome cuidado quando utilizar a função .index(), pois a mesma pode retornar um erro caso você tente
# buscar pelo índice de um elemento que não existe. Veja o caso abaixo:

#frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
#print(frutas.index('Melancia'))

#Ao tentar buscar pela fruta 'Melancia', obteremos o erro "ValueError: 'Melancia' is not in
# list" no console, já que é impossível buscar o índice de algo que não está na lista. Por isto,
# é sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter
# o seu índice. Um código ideal que faz uso da função index() é demonstrado abaixo:

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))


#Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice,
#evitando assim de receber um erro no console.

