#Essas são variáveis globais que podem ser acessadas de 
#qualquer parte do programa:
num1=num2=res=0

#Variável global declarada dentro de uma função:
def cn():
    global canal
    canal ="CFB Cursos"

cn()

print(canal)