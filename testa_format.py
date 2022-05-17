# Pedro precisa criar a seguinte string:
#"Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

#primeira forma

print(f"Em {ano} o Carnaval acontece em {mes} do dia {dia_ini} até o dia {dia_fim}")

#segunda forma

print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano,mes,dia_ini,dia_fim))