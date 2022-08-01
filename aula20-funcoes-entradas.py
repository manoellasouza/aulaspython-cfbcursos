#Funções que recebem valores de entrada mas não retornam valor nenhum

#n1 e n2 são os parâmetros de entrada
def somar(n1, n2):
    r=n1+n2
    print(f"A soma de {n1} + {n2} é igual a {r}")

#A mesma função pode somar valores diferentes:
somar(5,7)
somar(12,8)

#Argumentos arbitrários: *n
#Nesse caso é passado um número qualquer de argumentos

#Dá pra chamar cada argumento assim:
def textos(*t):
    print(t[0])
    print(t[1])
    print(t[2])

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

#Ou chamar todos os argumentos sem se preocupar em chamar um por um:
def palavras(*txt):
    for t in txt:
        print(t)

palavras("C#", "JavaScript", "Java")

def calculo(*num):
    r=0
    #o n vai percorrer cada agumento de entrada do num e será feita 
    # a soma dentro do r
    for n in num:
        r+=n
    print(f"A soma dos valores {num} é igual a {r}")

calculo(5,2,13,9,157)

# Também dá pra fazer através de listas:
valores=[1,5,3,2]
def somaval(num):
    r=0
    for n in num:
        r+=n
    print(f"A soma dos valores {num} é igual a {r}")

somaval(valores)


#Nesse caso, a função vai retornar o valor padrão que está na função:
def carros(c="Golf"):
    print(f"Modelo: {c}")

carros()

#Ao chamar a função passando um valor, ele vai imprimir o valor passado
#Nesse caso, a função retornaria HRV
carros("HRV")
