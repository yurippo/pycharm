#o grande sorteo O professor Flávio tem o costume de sortear um livro da Casa do Código ao final de todos os seus cursos para os seus 3 melhores alunos. Desta vez, os três melhores alunos foram:
#Paulo,Juliana,Tamires
#crie um python code que faca isso

import random

numero_sorteado = random.randrange(4)

print(numero_sorteado)

if (numero_sorteado == 1):
    print (f'O numero sortead foi {numero_sorteado} Paulo venceu')
elif (numero_sorteado == 2):
    print(f'O numero sortead foi {numero_sorteado} Juliana venceu')
elif (numero_sorteado == 3):
    print(f'O numero sortead foi {numero_sorteado} Tamires venceu')
else:
    print('Tente outra vez')