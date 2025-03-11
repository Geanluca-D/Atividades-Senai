# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos
# desejados. O programa deve calcular o valor total e permitir que o usuário finalize o
# pedido digitando 0.

h = 0
b = 0
r = 0
c = 0
print('Menu: ')
print('Hamburguer - R$20 -> 1')
print('Batata frita - R$7 -> 2')
print('Refrigerante - R$12 -> 3')
print('Combo - R$30 -> 4')
print()
pedido = int(input('Digite o código do produto desejado (Digite 0 para cancelar a ação): '))
qnt = int(input('Digite a quantidade: '))

while pedido != 0:
  if pedido == 1:
    h += 1 * qnt
  elif pedido == 2:
    b += 1 * qnt
  elif pedido == 3:
    r += 1 * qnt
  elif pedido == 4:
    c += 1 * qnt
  else:
    print('Valor inválido!')
  pedido = int(input('Digite o código do produto desejado (Digite 0 para cancelar a ação): '))
  if pedido != 0:
    qnt = int(input('Digite a quantidade: '))

total = (20*h) + (7*b) + (12*r) + (30*c)

print()
print(f'O valor total do pedido é R${total}')