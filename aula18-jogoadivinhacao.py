#Game de adivinhação com o conteúdo visto até agora
#Tentar adivinhar o número que o sistema pensou e ao final ele vai
#dizer quantas tentativas foram necessárias para adivinhar

# Biblioteca com o comando para sortear número:
from random import randrange
#Biblioteca com o comando para poder limpar a tela:
from os import system

erros=0
sorteado=randrange(0,20)
jogador=int(input("Digite seu número: "))

while sorteado != jogador:
    system("cls")
    if (sorteado>jogador):
        print("ERRO! Número é maior!")
    else:
        print("ERRO! Número é menor!")
    erros+=1
    jogador=int(input("Digite seu número: "))
    
print(f"Número sorteado: {jogador}\nVocê acertou em {erros+1} tentativas")