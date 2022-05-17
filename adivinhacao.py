import random

print("************************************")
print("Olá bem vindo ao jogo de Adivinhação")
print("************************************")

##numero_secreto = random.randint(0,100) gera o numero int aleatorio entre 0 e 100  ou posso usar

#random.random() gera un numero float entre 0 e um por isso usei a função round() para arredondar

#random.randrange() gera um numero inteiro aleatorio entre por exemplo (1,101)

numero_secreto = random.randrange(1,101)

#print(numero_secreto)

total_de_tentativas = 0
pontos = 1000

print(f'Qual nivel de dificuldade {numero_secreto}?')
print('(1) Facil (2) Medio (3) Dificil')

nivel = int(input('Define o nivel:'))

if(nivel ==1):
  total_de_tentativas = 20
elif(nivel==2):
  total_de_tentativas = 10
else:
  total_de_tentativas = 5

rodada =1

while (rodada <= total_de_tentativas):

  print(f"Tentativa {rodada} de {total_de_tentativas}")

  chute_str = input("Digite o seu numero entre 1 e 100: ")

  print("Você digitou ",chute_str)

  chute = int(chute_str)

  if (chute < 1):
    print("Você deve digitar um número entre 1 e 100!")
    continue


  acertou = chute == numero_secreto

  maior = chute > numero_secreto

  menor = chute < numero_secreto

  if(acertou):
    print(f"Parabéns! Você acertou e fez {pontos} pontos!")
    break
  else:
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")
    pontos_perdidos = abs(numero_secreto - chute) #40-60 = -20 vou precisar usar a funcao abs para numero absoluto abs(-10) = 10 e abs(10) = 10
    pontos = pontos - pontos_perdidos

    print(f"Fim do jogo o seu total de pontos foi {pontos}")

  rodada = rodada + 1

