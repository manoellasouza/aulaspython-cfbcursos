#Tratamento de erros / exceções
#Comando para verificar erros: Try
#Caso a rotina retorne um erro, ele cai no except e executa
#a rotina de except. O finally vai executar se tiver um erro ou não

#Dessa forma não vai imprimir a mensagem de erro padrão do sistema e 
#sim a mensagem personalizada:
try:
    print(x)
except:
    print("ERRO!")

#Tratando um except conhecido, como o NameError (não definido, não inicializado, não criado...)
try:
    print(x)
except NameError:
    print("X não definido")
except:
    print("Erro desconhecido")

#Caso não gere o erro, dá pra colocar um else:
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo!")

#O finally vai execurar de qualquer jeito, com erro ou sem:
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo!")
finally:
    print("Fim do tratamento")

num=-10

if num < 1:     #Para gerar uma exceção precisa do comando raise, dessa forma vai gerar um erro para o usuário
    raise Exception("Valor não permitido")
            
valor="Bruno"
if not type(valor) is int:     ##Para gerar uma exceção precisa do comando raise, dessa forma vai gerar um erro para o usuário
    raise Exception("Somente números permitidos!")  
else:
    print(valor)