texto="Curso de Python"

#Verificar se existe uma palavra dentro da string
res="Python" in texto
print(res)

#Verificar se NÃO existe uma palavra dentro da string:
res="python" not in texto
print(res)

palavra="python"
#Como a palavra pesquisada tem que ser exatamente igual,
#o indicado é converter ela inteira para fazer a pesquisa:
rest=palavra.upper() in texto.upper()
print(res)

curso="Curso de C#"
canal="CFB Cursos"

#Concatenar o conteúdo das duas strings acima:
res=curso + " " + canal
print(res)

cidade = "Palhoça"
dia=28
mes="Julho"
ano=2022
canal="CBF Cursos"

# Esses são exemplos de caracteres de escape:
# \n ir para linha debaixo, \"{}\" vai fazer com que as aspas apareçam no terminal
# \' aspas simples, \r enter, \b backspace, \t tabulação
data="{}, {} de {} de {}\n \"{}\""

#Algumas formas de escrever data:
print(f"{cidade}, {dia} de {mes} de {ano}")

#No método format ele vai substituir as variáveis passadas como
#parâmetro e adicionando na sequência:
print(data.format(cidade,dia,mes,ano, canal))

