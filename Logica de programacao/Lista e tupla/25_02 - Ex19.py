# 19. Criar uma lista e remover um elemento específico.

palavra = ['mouse', 'teclado', 'monitor', 'mousepad']

print(palavra)
remover = str(input('Digite uma das palavras acima para remover o valor da lista: '))

palavra.remove(remover)

print(palavra)