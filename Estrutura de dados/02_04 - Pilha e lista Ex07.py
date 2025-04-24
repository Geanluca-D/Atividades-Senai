#Uma central de atendimento telefônico gerencia chamadas em espera usando
#uma pilha. Isso significa que a última chamada recebida será a primeira a ser
#atendida.

chamadas = []

chamadas.append('(11)91234-1234')
chamadas.append('(11)99999-1111')
chamadas.append('(11)95555-6666')

for i in range(1, len(chamadas)+1):
    print(f'{i}º número a ser atendido: {chamadas[-1]}')
    chamadas.pop()
    print()

if len(chamadas) == 0:
    print('Foram atendidos todos os números')
