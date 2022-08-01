#lista:
#l_carros=["HRV", "Golf", "Argo"]

#for x in l_carros:
    #print(x)

#tupla utiliza parênteses e não pode ser diretamente alterada:
t_carros=("HRV", "Golf", "Argo")
#print(t_carros[0])

#Para ser alterada, o que pode ser feito é "converter" a tupla para uma lista
l_carros=list(t_carros)

#Alterando a variável dentro da lista nova:
l_carros[2]="Focus"

#Convertendo a lista para tupla e inserindo na tupla original:
t_carros=tuple(l_carros)

for x in t_carros:
    print(x)
