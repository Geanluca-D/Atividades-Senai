#Empilhado elementos
'''
'''
#iniciando uma pilha (lista) vazia
pilha = []

#Empilhando elementos na pilha
pilha.append(10)
pilha.append(20)
pilha.append(30)

print()
print(pilha)
print()
#Mostrando o valor no topo da pilha
print('Topo da pilha: ', pilha[-1])

#Removendo o valor do topo da pilha
print('Valor removido: ', pilha.pop())  #.pop remove o ultimo valor adicionado na pilha, o ultimo index

print(pilha)
print('Pilha esta vazia? ', len(pilha) == 0)
print('Topo da pilha: ', pilha[-1])
print()

print('Valor removido: ', pilha.pop())
print(pilha)
print('Pilha esta vazia? ', len(pilha) == 0)
print('Topo da pilha: ', pilha[-1])
print()

print('Valor removido: ', pilha.pop())
print(pilha)
print('Pilha esta vazia? ', len(pilha) == 0)

#=======================================================

#Fila

from collections import deque

fila = deque()

fila.append(10)
fila.append(20)
fila.append(30)

print(fila)
#Mostrando o primeiro elemento da fila
print('Primeiro da fila: ', fila[0])
#Removendo o primeiro elemento da fila (primeiro valor que entra é o primeiro que sai)
print('Removido: ', fila.popleft())

print('Primeiro da fila: ', fila[0])

print('Removido: ', fila.popleft())

print('Pilha está vazia? ', len(fila) == 0)
print('Primeiro da fila: ', fila[0])

print('Pilha está vazia? ', len(fila) == 0)