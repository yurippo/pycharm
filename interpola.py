#Temos as seguintes instruções
#Veja como séra impresso no console

print("R$ {:7.1f}".format(1000.12))

print("R$ {:07.2f}".format(4.11))

print("R$ {:7.1f}".format(1000.16))

#fstring para interporlar texto e variavel

nome = 'YURI'
print(f'Meu nome é {nome}')

#Além de variáveis, podemos passar também funções e métodos

print(f'Meu nome é {nome.lower()}')
