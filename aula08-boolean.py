#Podemos utilizar para validar se existem elementos em uma coleção ou não
#Pode retornar True ou False,

aula = False
print(aula)

exp=10<15
print(exp)

ex ="CFB Cursos"
#Nesse caso vai retornar True, pois é utilizado para verificar se uma string possui
#um valor ou não
print(bool(ex))

#Retornando False:
ex = ""
if ex:
    print("Possui texto")
else:
    print("Vazio")
print(bool(ex))

#Variáveis inteiras valendo 0 retornam False:
x=1; y=0
print(bool(x))
print(bool(y))

#O mesmo acontece com as tuplas, set, dictionary, list... Todos esses elementos quando
#estão vazios retornam False