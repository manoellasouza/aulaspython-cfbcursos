# Herança é quando uma classe herda outra classe. Cria uma classe chamada pai
# e depois uma classe filho que vai herdar a classe pai. Tudo o que for criado na pai
# vai valer para a classe filho.

class NPC: #Base, Pai, Super Classe
    # Definindo os parâmetros de entrada do construtor que servirá de base para as classes filho:
    def __init__(self, nome, time, forca, municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True       #todos que forem criados estarão vivos
        self.energia=100     #quando forem criados a energia estará em 100%

    def info(self):
        print(f"Nome....: {self.nome}")
        print(f"Time....: {self.time}")
        print(f"Força...: {self.forca}")
        print(f"Munição.: {self.municao}")
        print("Vivo....:",("Sim" if self.vivo else "Não"))
        print(f"Energia.: {self.energia}")
        print("---------------------------------------")

# A classe soldado está herdando todo o conteúdo da classe NPC:
class Soldado(NPC):
    # Os parêmtros da classe filho vão sobrescrever os da classe Pai
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        #Invocando método ou parâmetros da classe Pai:
        super().__init__(nome, time, self.forca, self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=100
        self.municao=20
        #Invocando método ou parâmetros da classe Pai:
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca=400
        self.municao=500
        #Invocando método ou parâmetros da classe Pai:
        super().__init__(nome, time, self.forca, self.municao)
        
    #Função inf vai chamar a função info da classe Pai:
    def inf(self):
        super().info()

#Dando nomes e times aos npcs:
s1=Guarda("Jon", 1)
s2=Soldado("Daario", 1)
s3=Elite("Sam", 1)
s4=Guarda("Bran", 2)
s5=Soldado("Ned", 2)
s6=Elite("James", 2)

#Alterando estado de vivo para morto:
s1.vivo=False
s6.vivo=False

#Chamando a função info para saber os status de cada um:
s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()
