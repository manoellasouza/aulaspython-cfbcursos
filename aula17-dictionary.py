#Dictionary é uma coleção do tipo chave e valor
#Ele é indexável, então dá pra alterar o valores

#Chave/Key - Valor/Value
carro={"Fabricante": "Honda", 
    "Modelo": "HRV", 
    "Ano": 2016, 
    "Cor": "Prata"
}

#Imprime tudo 
print(carro)    

#Vai imprimir o valor da chave, no caso HRV
print(carro["Modelo"])

#Duas formas de colocar o valor dentro de outra variável:
fab=carro["Fabricante"]   #fab=carro.get("Fabricante")
print(fab)

#Mudando o valor de uma chave:
carro["Cor"]="Preto"
print(carro["Cor"])

#Imprimindo os valores com o método itens:
for c,v in carro.items():
    print (f"{c}: {v}")

#Encontrando uma chave ou valor dentro do dicionário:
if "Modelo" in carro:
    print("O modelo é uma chave")

#Para saber a quantidade de conjuntos do dicionário:
print(f"Tamanho do Dictionary: {len(carro)}")

#Adicionando mais um conjunto ao dicionário:
carro["Câmbio"]="Automático"

#Removendo um conjunto do dicionário:
carro.pop("Câmbio") 

#Também pode ser usado o del:
#del carro["Câmbio"]

#Limpando o Dictionary:
carro.clear()

#Dictionary composto por chaves, onde cada uma possui um novo dictionary

carros={
    "Carro 1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro 2":{
        "Fabricante":"Volksvagem",
        "Modelo":"Golf"
    },
    "Carro 3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }

}

# Imprimindo chave e valor do carro 1:
print(carros["Carro 1"])

#Imprimindo o valor do modelo do carro :
print(carros["Carro 1"]["Modelo"])


#Criando 3 dictionarys separados que serão adicionados em ourto dictionary:
Carro1={
        "Fabricante":"Honda",
        "Modelo":"HRV"
    }

Carro2={
        "Fabricante":"Volksvagem",
        "Modelo":"Golf"
    }

Carro3={
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }

Carros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}

# Imprimindo chave e valor do carro 1:
print(Carros["C1"])