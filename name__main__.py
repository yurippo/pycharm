# mesmo um módulo solitário pode executar alguma funcionalidade quando
# executado isoladamente, basta adicionar um if no final do código para
# verificar a váriavel __name__

def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()