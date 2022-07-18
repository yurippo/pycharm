import random

def jogar():

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

  print('Qual nivel de dificuldade ?')
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

    chute_str = input("Digite o seu numero secreto entre 1 e 100: ")

    print(f"Você digitou {chute_str}")

    chute = int(chute_str)

    if (chute < 1):
      print("Você deve digitar um número entre 1 e 100!")
      continue


    acertou = chute == numero_secreto

    maior = chute > numero_secreto

    menor = chute < numero_secreto

    pontos_perdidos = abs(numero_secreto - chute)  # 40-60 = -20 vou precisar usar a funcao abs para numero absoluto abs(-10) = 10 e abs(10) = 10
    pontos = pontos - pontos_perdidos

    if(acertou):
      print(f"Parabéns! Você acertou o numero secreto era {numero_secreto} fez {pontos} pontos!")
      break
    else:
      if(maior):
          print(f"O seu chute foi maior do que o número secreto !!")
          if (rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {}".format(
              numero_secreto, pontos))
      elif(menor):
          print(f"O seu chute foi menor do que o número secreto !!")
          if (rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {}".format(
              numero_secreto, pontos))
    rodada = rodada + 1

  print("Fim do jogo")

if(__name__== "__main__"):
  jogar()