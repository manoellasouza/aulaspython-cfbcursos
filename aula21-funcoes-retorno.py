#Funções que retornam valores

valores=[1,5,3,2]
def somar(num):
    r=0
    for n in num:
        r+=n
    return r

print(f"A soma de {valores} é igual a {somar(valores)}")

#Ou também daria pra colocar a função dentro de uma variável: 
r=somar(valores)
print(f"A soma de {valores} é igual a {r}")
