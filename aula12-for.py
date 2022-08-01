#Loop for para trabalhar com coleções

carros=["HRV", "Golf", "Argo", "Focus"]

#Vai percorrer a lista elemento a elemento:
for x in carros:
    print(x)
    if (x=="Golf"):
        print (" VW")

#Também poderia ser a lista diretamente:
for x in ["HRV", "Golf", "Argo", "Focus"]:
    print(x)

#Vai percorrer a lista elemento a elemento e parar 
# quando chegar no Argo:
for x in carros:
    print(x)
    if (x=="Argo"):
        break

#Vai percorrer a string elemento a elemento:
for x in "CFB Cursos":
    print(x)

