import datetime

#sistema vai retornar data atual
data=datetime.datetime.now()
print (data)

#data atual, vai sair assim por exemplo: 31/07/2022
print(f"{data.day}/{data.month}/{data.year}")

#strf time: vai devolver algo de acordo com o que for colocado no ()
#por exemplo, colocando %A ele retorna o dia da semana da data indicada 
nasc=datetime.datetime(1985,3,7)
print(nasc.strftime("%W"))

# %a = dia da semana abreviado Thu
# %A = dia da semana completo  Thursday
# %w = número do dia da semana 4      domingo é 0
# %d = dia do mês              7
# %b = nome do mês abreviado   Mar
# %B = nome do mês completo    March
# %m = número do mês           3
# %y = ano com 2 dígitos       85 
# %y = ano com 4 dígitos       1985 
# %j = dia do ano              066     001 a 366 
# %W - número da semana        09

# %H = hora com 2 dígitos, de 00 a 23
# %I = hora com 2 dígitos, de 00 a 12
# %p = indica AM/PM
# %M = minutos
# %S = segundos
# %f = microsegundos

