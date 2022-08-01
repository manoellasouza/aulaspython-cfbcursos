curso=" Curso de Python "
#Strip: Método para remover espaços no início e fim da string:
curso = curso.strip()

#Imprimindo posição 0 a 4:
print(curso[9:15])

#Saber tamanho da string
print(curso)
print(f"Tamanho: {len(curso)}")

#Imprimindo somente uma posição determinada do array:
print(curso[9])

#Deixando tudo minúsculo:
print(curso.lower())
#Também daria pra juntar dois métodos, por exemplo:
#print(curso.lower().strip())

#Deixando tudo maiúsculo:
print(curso.upper())

#Substituindo uma string ou um caractere:
print(curso.replace("Python", "C#"))

#Subdivide a string de acordo com o que for indicado
a=curso.split(" ")
#O a virou uma list com 3 posições, por isso ele retorna a palavra Curso:
print(a[0])

