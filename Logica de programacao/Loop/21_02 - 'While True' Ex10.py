# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo
# (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de
# votos nulos e brancos. A entrada 0 encerra a votação.

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
bran = 0

voto = int(input('Vote nos candidatos (1 a 4), ou nulo (5), ou branco (6), ou 0 para cancelar a ação: '))

while voto != 0:
  if voto == 1:
    cand1 += 1
  elif voto == 2:
    cand2 += 1
  elif voto == 3:
    cand3 += 1
  elif voto == 4:
    cand4 += 1
  elif voto == 5:
    nulo += 1
  elif voto == 6:
    bran += 1
  else:
    print('Valor inválido!')
  voto = int(input('Vote nos candidatos (1 a 4), ou nulo (5), ou branco (6), ou 0 para cancelar a ação: '))

totalCand = cand1 + cand2 + cand3 + cand4
total = totalCand+nulo+bran

print(f'O total do votos foi {total}')
print(f'O total de votos em candidatos foi de {totalCand}')
print(f'O candidato 1 recebeu {cand1} votos')
print(f'O candidato 2 recebeu {cand2} votos')
print(f'O candidato 3 recebeu {cand3} votos')
print(f'O candidato 4 recebeu {cand4} votos')
print(f'Houveram {nulo} votos nulos e {bran} votos em branco')
print(f'A % de votos nulos foi de {100*nulo/total} e a % de votos em branco foi de {100*bran/total}')