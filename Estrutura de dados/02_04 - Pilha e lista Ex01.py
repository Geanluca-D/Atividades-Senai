#Implementar uma pilha simples utilizando uma lista.

pilha = []

pilha.append(5)
pilha.append(10)
pilha.append(15)
print(pilha)
print()

while len(pilha) != 0:
    print('Valor do topo da pilha: ', pilha[-1])
    print('Valor removido: ', pilha.pop())
    print(pilha)
    print()

if len(pilha) == 0:
    print('Pilha final: ', pilha)