#O Pedro é um desenvolvedor Python Junior e precisa corrigir o código abaixo que está dando erro:

#Quais alternativas ele pode usar no lugar de #AQUI para o código funcionar?

#Lembrando que para transformar um tuple em uma lista, temos a função list(..).
# Se queremos transformar de list para tuple devemos usar tuple(..) Ambas são funções built-in.

nomes_tuple = ("Nico", "Douglas", "Flavio", "Daniel")
#

nomes = list(nomes_tuple)

nomes.append("Fabio")

print(nomes)