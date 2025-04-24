#AULA 41 - LISTA, TUPLA, DICIONÁRIOS E CONJUNTOS
'''

'''
#Listas =================================================================
frutas = ['maça', 'melância', 'manga'] #Lista de strings
numeros = [1, 2, 3] #Lista de números
print(frutas)
frutas.append('laranja') #Adiciona um elemento na lista
print(frutas)
print()
#========================================================================



#Tuplas =================================================================
cores = ('vermelho', 'roxo', 'azul')
print(cores[1])
#========================================================================



#Estruturas homogêneas ==================================================
lista_homogenea = [1, 2, 3, 4]
print(lista_homogenea)
#========================================================================



#Estruturas heterogêneas ================================================
lista_heterogenea = [1, 2.8, 'string', True] #tipos de dados misturados
tupla_heterogenea = [1, 2.8, 'string', True]
print(lista_heterogenea)
#========================================================================



#Dicionário =============================================================
aluno = {
    'nome' : 'Douglas',
    'idade' : 20,
    'curso' : 'gestao de esportes'
}

print(aluno)
print()
#Acessando valores pelo nome da "chave"
print(aluno['nome'])
print(aluno['idade'])
print()

#Adiciona uma nova linha
aluno['email'] = 'dg@gmail.com'
print(aluno)
print()

#Modifica um valor
aluno['idade'] = 21
print(aluno)
print()

#Remove um item pelo nome da chve
del aluno['curso']
print(aluno)
print()

#Retorna verdadeiro ou falso
print('idade' in aluno)
print('curso' in aluno)
print()

#Reorganiza o dicionário
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
print()
#========================================================================



#Lista de dicionários ===================================================
alunos = {
    'nome' : 'Douglas',
    'idade' : 20,
    'curso' : 'gestao de esportes'
},{
    'nome' : 'Jonas',
    'idade' : 19,
    'curso' : 'ADS'
},{
    'nome' : 'Gabriel',
    'idade' : 21,
    'curso' : 'DEV'
}

for aluno in alunos:
    print('Dados do aluno: ')
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('-' * 20)
print()
#========================================================================



#CONJUNTO ===============================================================
frutas2 = {'maça', 'maça', 'banana', 'uva'} #Conjuntos removem itens repetidos e exibe de forma aleatória
print(frutas2)
print()

frutas2.add('morango') #Adiciona elementos no conjunto (se já existir o valor que vai ser adicionado, ele vai ser ignorado)
print(frutas2)
print()

frutas2.remove('banana') #Remove elementos do conjunto
print(frutas2)
print()
#========================================================================



#OPERAÇÕES ENTRE CONJUNTOS ==============================================
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

#União entre dois conjuntos
uniao = conjunto_a | conjunto_b
print(uniao)
print()

#Intersecção (retorna elementos comuns entre os conjuntos)
interseccao = conjunto_a & conjunto_b
print(interseccao)
print()

#Diferença (retorna elementos que estão no conjunto_a mas não estão no conjunto_b)
diferenca = conjunto_a - conjunto_b
print(diferenca)
print()

#Diferença simétrica (retorna elementos que estão em um OU outro conjunto, mas não em ambos (retorna elementos incomuns entre os conjuntos))
diferenca_simetrica = conjunto_a ^ conjunto_b
print(diferenca_simetrica)
print()
#========================================================================