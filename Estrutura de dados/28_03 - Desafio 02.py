#2) Crie uma função que receba uma lista de tuplas, onde cada tupla contém o nome de um aluno e sua nota, 
#   e retorne o nome do aluno com a maior nota.

lista = [
    ('Douglas', 8.5),
    ('Jonas', 10),
    ('Gabriel', 8)
    ]

def mNota (lis):
    maior = 0
    name = ''
    for nome, nota in lis:
        if nota > maior:
            maior = nota
            name = nome
    return name, maior

print(f'A maior nota é: {mNota(lista)}')