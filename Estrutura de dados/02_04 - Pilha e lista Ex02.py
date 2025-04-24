#Criar uma pilha e manipular seus elementos.

pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)
print(pilha)
print()

while len(pilha) != 0:
    print('Valor do topo da pilha: ', pilha[-1])
    print('Valor removido: ', pilha.pop())
    print(pilha)
    print()

if len(pilha) == 0:
    print('Pilha final: ', pilha)