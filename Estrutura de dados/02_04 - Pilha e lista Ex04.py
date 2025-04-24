#Criar uma implementação simples de uma fila (Queue) usando listas.

from collections import deque

fila = deque()

fila.append(10)
fila.append(20)
fila.append(30)

print(fila)
print()

while len(fila) != 0:
    print('Primeiro número da fila: ', fila[0])
    print('Valor removido: ', fila.popleft())
    print(fila)
    print()

print('A fila está vazia? ', len(fila) == 0)