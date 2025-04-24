#Um consultório odontológico precisa gerenciar a ordem de atendimento dos
#pacientes. Para isso, foi decidido implementar uma fila onde os pacientes são
#chamados na ordem em que chegaram (FIFO – First In, First Out).

from collections import deque

pacientes = deque()

fila = int(input('Digite a quantidade de pacientes: '))

for i in range(1, fila+1):
    ordem = input(f'Digite o nome do {i}º paciente(ordem de chegada):')
    pacientes.append(ordem)

while len(pacientes) != 0:
    print()
    print('Lista de pacientes em ordem de chegada: ', pacientes)
    print('Paciente atendido: ', pacientes.popleft())

if len(pacientes) == 0:
    print()
    print('Todos os pacientes foram atendidos!')
