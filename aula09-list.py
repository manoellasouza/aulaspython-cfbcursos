#As listas são indexáveis, ou seja, pode ser usado o índice para gerenciar
#ou retornar um elemento da lista
carros=["HRV", "Golf", "Argo", "Focus"]

#Imprimindo da esquerda para direita (Golf):
print(carros[1])

#Imprimindo da direita para esquerda (Argo):
print(carros[-2])

#Dá pra fazer alterações na lista, substituindo elementos:
carros[3] = "Fusion"
print(carros)

#Copiar uma lista para outra:
carros2 = list(carros)

#Adicionando novos itens a lista:
carros.append("Fit")
carros.append("Focus")
carros.append("Polo")
print(carros)

#Removendo um carro da lista:
carros.remove("Fusion")

#Removendo o último elemento da lista:
carros.pop()

#Removendo através do del:
del carros[2]

print(carros)

#Verificando o tamanho da lista:
print(f"{len(carros)} carros na lista")

#Limpando todos os elementos da lista, vai voltar uma lista vazia []:
carros.clear()
print(carros)

#Fundindo 2 listas:
carros3 = ["Fusca", "147", "Brasilia", "Celta"]
carros4 = carros2 + carros3
print(carros4)
print(f"{len(carros4)} carros na lista 4")