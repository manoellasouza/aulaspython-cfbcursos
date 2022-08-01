#As funções lambdas ou anônimas são funções simples, pode entrar com
#quantos argumentos quiser, mas a função terá somente uma expressão
#São funções simples e anônimas, então não é pra colocar o nome da função

#Exemplo 1
soma=lambda a,b:a+b
mult=lambda a,b,c:(a+b)*c

print(soma(2,5))
print(mult(2,5,3))

#Também dá pra imprimir a função diretamente:
print((lambda a,b: a+b)(3,2))

#Exemplo 2
#Passou os argumentos x e func. E a expressão ficou: x + resultado da função
r=lambda x,func: x+func(x)

# Então foi passado o valor 2 para x e para a função foi passado uma função lambda
# que multiplica x por ele mesmo.
res=r(2, lambda x: x*x)
print(res)

#Aqui a lambda vai somar o x com 3:
res=r(2, lambda x: x+3)
print(res)