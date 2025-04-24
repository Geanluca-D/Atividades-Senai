#Um navegador de internet usa uma pilha para armazenar o histórico de
#navegação. Cada vez que o usuário acessa uma nova página, ela é adicionada
#ao histórico. O usuário pode voltar para a página anterior ou avançar
#novamente.

pag = []
save = []

for i in range(1, 4):
    acess = input(f'Digite {i}º página acessada: ')
    pag.append(acess)

print('Última página acessada: ', pag[-1])

while True:
    vol = input('Deseja voltar a página anterior?(s/n): ')
    if vol == 's':
        save.append(pag[-1])
        pag.pop
        print(pag[-1])
        break
    elif vol == 'n':
        break
    else:
        print('Valor inválido')
        break

print('Última página acessada: ', pag[-1])