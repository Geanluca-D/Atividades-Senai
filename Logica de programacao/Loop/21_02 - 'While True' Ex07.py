# 7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B
# com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para
# que a população do país A ultrapasse a população do país B.

ano = 0
paisA = 80000
paisB = 200000

while paisA <= paisB:
  paisA = paisA * 0.03 + paisA
  paisB = paisB * 0.015 + paisB
  ano += 1

print(f'Vai demorar {ano} anos para a população do país A ultrapassar a do país B')