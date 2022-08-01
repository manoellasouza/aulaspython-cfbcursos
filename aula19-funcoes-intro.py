#Função é um bloco de código que fica armazenado, e que é executado
#em um momento específico. A intenção é reproveitar esse bloco de código,
#pra não ficar digitando toda hora ao precisar executá-lo novamente

n1=10
n2=5

#Em Python a função é criada através do def:
def somar():
    r=n1+n2
    print(f"A soma de {n1} + {n2} é igual a {r}")
    print("Curso de Python - CFB Cursos")

def subtrair():
    r=n1-n2
    print(f"A subtração de {n1} - {n2} é igual a {r}")
    print("Curso de Python - CFB Cursos")

def multiplicar():
    r=n1*n2
    print(f"A subtração de {n1} * {n2} é igual a {r}")
    print("Curso de Python - CFB Cursos")

#somar()
#subtrair()
#multiplicar()

#Uma função pode chamar outras funções:

def calculos():
    somar()
    subtrair()
    multiplicar()

calculos()



