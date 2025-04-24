#1) Crie uma função que receba duas listas de números inteiros e retorne
#   uma nova lista contendo os elementos que aparecem em ambas as listas (interseção).

def inter (l1, l2):
    return set(l1) & set(l2)

lista1 = list(map(int, input('Insira uma lista de numeros separados por espaço: ').split()))
lista2 = list(map(int, input('Insira uma segunda lista de numeros separados por espaço: ').split()))

print(f'A intersecção de valores das listas são: {inter(lista1, lista2)}')