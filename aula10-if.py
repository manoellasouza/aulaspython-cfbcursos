a=True

if a:
    print("CFB Cursos")

print("Fim do programa")

a=10
b=5
res=2
op="*"

if a>b:
    print("É maior!")

if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b

print(f"Operação {a}{op}{b} = {res}")