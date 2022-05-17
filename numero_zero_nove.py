#O menor numero possivel e o zero e o maior número possível é o 9.

import random

aleatorio = random.randrange(10)
print(aleatorio)

#uma instrução do Python capaz de gerar um número inteiro aleatório entre 0 e 100 (incluindo 100, ou seja [0,100])

numero_ale_zero_cem = random.randrange(0,101)

print(numero_ale_zero_cem)

# another way to accomplish that

numero_ale_novo = int(random.random() * 101)

print(numero_ale_novo)