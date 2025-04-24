#Uma impressora trabalha com um sistema de fila para processar documentos
#enviados para impressão. Cada documento enviado entra no final da fila e será
#impresso na ordem em que chegou.

from collections import deque

imp = deque()

imp.append('Lista de exercícios')
imp.append('Prova')
imp.append('Recuperção')

for i in range(1, len(imp)+1):
    print('Documento a ser imprimido: ', imp[0])
    print(f'{imp[0]} foi imprimido com sucesso!')
    imp.popleft()
    print()

if len(imp) == 0:
    print('Não há mais documentos para serem impressos!')