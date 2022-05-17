print("************************************")
print("Olá bem vindo ao jogo de Adivinhação")
print("************************************")

numero_secreto = 42

total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):

  print(f"Tentativab {rodada} de {total_de_tentativas}")

  chute_str = input("Digite o seu numero: ")

  print("Você digitou ",chute_str)

  chute = int(chute_str)

  if (chute < 1 or chute > 100):
     print("Você deve digitar um número entre 1 e 100!")
     continue

  acertou = chute == numero_secreto

  maior = chute > numero_secreto

  menor = chute < numero_secreto

  if(acertou):
    print("Parabéns! Você acertou!")
    break

  else:
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")

    print("Fim do jogo")

