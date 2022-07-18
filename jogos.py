import forca
import adivinhacao

#bibliotecas iguais a modulos em Python

def escolhe_jogo():
    print("************************************")
    print("********Escolha o seu jogo*********!")
    print("************************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando forca")
        # para chamar a função eu uso o nome da classe = modulo em python ponto e chamo a função ;)
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        # para chamar a função eu uso o nome da classe = modulo em python ponto e chamo a função ;)
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()