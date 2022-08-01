#É importante separar o código em arquivos diferentes para organizar, ficando mais fácil de visualizar
#e facilitando a manutenção do código

#importar a função de outro arquivo:
#import aula34canal 

#dá pra renomear o arquivo no próprio import:
import aula34canal as cn

cn.canal_nome()
print(cn.jogador["nome"])

#resultado recebe função dir pra mostrar tudo o que tem dentro de canal:
res=dir(cn)
print(res)

#Importando apenas um parâmetro específico:
from aula34canal import jogador

#dessa forma dá pra chamar diretamente:
print(jogador["nome"])

