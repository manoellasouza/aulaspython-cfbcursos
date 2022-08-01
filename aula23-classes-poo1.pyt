# Uma classe é a especificação de um objeto. É o desenho ou o conjunto de 
# regras de um determinado objeto. O objeto é uma instância da classe.
# A classe é um projeto (exemplo: planta da casa), e a casa é o objeto da planta

class Carro:
    velMax=0 #propriedade da classe
    ligado=False
    cor=""

#instanciando objetos com a classe Carro
c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=False

print(f"Velocidade máxima: {c1.velMax}")
print(f"Cor: {c1.cor}")
estado="Sim" if c1.ligado else "Não"
print(f"Ligado: {estado}")


