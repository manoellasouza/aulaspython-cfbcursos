a=(int(input("Digite um número inteiro: ")))
b=(int(input("Digite outro número inteiro: ")))
resp=0

print("")
op=input("Qual operação você quer fazer?\nEscolha entre: +, -, * ou /: ")
print("")

if op=="+":
    resp=a+b
elif op == "-":
    resp=a-b
elif op == "*":
    resp=a*b
elif op == "/":
    resp=a/b
else:
    print("Operador inválido")

print(f"Resultado: {a}{op}{b} = {resp}")