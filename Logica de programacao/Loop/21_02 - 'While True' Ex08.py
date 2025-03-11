# 8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba
# o troco. Após isso, o programa deve reiniciar para um novo cliente.

while True:
  soma = 0

  while True:
    val = float(input('Digite o valor do produto (digite 0 para cancelar a ação): '))
    soma += val
    if val == 0:
      break

  print(f'O total da compra deu {soma}')
  pag = float(input('Digite o valor pago: '))

  while pag < soma:
      print(f'O troco não paga o valor total')
      pag2 = float(input('Digite o valor do restante do pagamento: '))
      pag += pag2

  print(f'O troco a ser entregue é de {pag-soma}')
  print()
  loop = str(input('Deseja cancelar o loop?(s/n): '))
  print()
  if loop == 's':
    break

print('loop cancelado')