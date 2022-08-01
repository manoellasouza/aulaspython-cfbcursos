import os
os.system('cls') #windows

#Precisa de uma condição para informar se vai continuar a ser executado ou não
#Enquanto o teste retornar true vai executar os comandos, ele precisa retornar false
#em algum momento, senão vai ficar em um loop infinito

#exemplo1
i=0

while i<10:     #while (teste logico)
    print(i)    #   comando
    i+= 1       #   incremento ou decremento da variável de controle
    if i>=5:
        break
print("Fim do loop")

#exemplo2
carros=["HRV", "Golf", "Argo", "Onix", "Focus"]
i=0
tam=len(carros)

while i < tam:
    print(carros[i])
    i+=1
print("\nFim do loop")

#exemplo3
carros=[]
carro=input("Digite o nome do novo carro: ")

#entrando com quantos carros quiser com while:
while carro != "sair": #não vai sair do loop enquanto não digitar esse comando
    carros.append(carro) #adicionando carro na lista
    carro=input("Digite o nome do novo carro: ")

#percorrendo o array com for:
for x in carros: #criou a variável x pra percorrer o array e imprimir o valor dos carros
    print(x)

print("Fim do loop")