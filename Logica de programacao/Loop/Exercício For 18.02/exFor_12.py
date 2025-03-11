# Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

cand1 = 0
cand2 = 0
cand3 = 0

eleit = int(input('Digite o número de eleitores: '))

if eleit > 0:
    for i in range(1, eleit + 1):
        voto = str(input('Vote no cand1, cand2 ou cand3: ')).lower()
        if voto == 'cand1':
            cand1 += 1
        elif voto == 'cand2':
            cand2 += 1
        elif voto == 'cand3':
            cand3 += 1
        else:
            print('Candidato inválido!!')
            print()
print(f'O cand1 recebeu {cand1} votos, O cand2 recebeu {cand2} votos, O cand3 recebeu {cand3} votos')