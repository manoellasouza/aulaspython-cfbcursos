# A matriz é uma coleção de arrays, trabalhando com linhas e colunas
#carros=["HRV", "Golf", "Focus", "Argo"] #array/lista

carros=[
    ["Modelo", "HRV"],       #linha 0
    ["Fabricante", "Honda"], #linha 1
    ["Ano", 2016]            #linha 2
]

# Adicionando elementos na lista:
carros.append(["Cor", "Prata"])

print(carros[2][1]) #linha 0 e coluna 1

# Alterando um valor da matriz:
carros[2][1]=2019

for l,c in carros:
    print(f"{l}: {c}")