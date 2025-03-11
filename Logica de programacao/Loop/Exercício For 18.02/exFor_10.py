# Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.

cont = 0

for i in range(1, 6):
    cli = str(input('Digite o nome do cliente: '))
    fat = float(input('Digite o faturamento do mesmo cliente: '))
    print()
    cont += fat
if cont > 54000:
    print(f'O faturamento da loja A superou o da loja B por R${cont - 54000}')
else:
    print(f'O faturamento da loja A NÃO superou o da loja B por R${54000 - cont}')