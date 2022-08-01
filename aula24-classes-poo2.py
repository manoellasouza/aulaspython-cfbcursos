#Construtor é uma função que vai ser chamada aumaticamente quando for instanciada um novo
#objeto da classe. É possível criar um construtor pra definir os valoers das propriedades.

class Carro:
    velMax=0 #propriedade da classe
    ligado=False
    cor=""

    #Definindo o construtor:
    def __init__(self, v, l, c): #Entre () vão os parâmetros de entrada. Self quer dizer que as propriedades definidas são
        self.velMax=v            # para o próprio método. Ou seja, self faz referência para a própria classe. 
        self.ligado=l            
        self.cor=c 

    #Método para imprimir as informações de todos os carros que forem chamados:
    def mostrar(self):
        print(f"Velocidade máxima: {self.velMax}")
        print(f"Cor: {self.cor}")
        estado="Sim" if self.ligado else "Não"
        print(f"Ligado: {estado}")
        print("------------------------------")

    #Método para ligar o carro:
    def ligar(self):
        self.ligado=True
    
    #Método para desligar o carro:
    def desligar(self):
        self.ligado=False
    
    #Método para saber se o carro está andando:
    def andar(self):
        if (self.ligado):
            print("Andando")
        else:
            print("Carro desligado")


#definindo os valores de entrada dos objetos através do construtor:
c1=Carro(200, False, "Preto")
c2=Carro(120, False, "Branco")
c3=Carro(350, False, "Vermelho")

c1.ligar()
c2.ligar()

#Nesse caso o carro vai aparecer como ligado para C1 e ligado e andando para C2:
c1.mostrar()
c2.mostrar()
c3.mostrar()

c2.andar()

