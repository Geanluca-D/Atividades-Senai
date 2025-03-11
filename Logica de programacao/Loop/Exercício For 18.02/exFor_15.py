# Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.
# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final

compra = int(input('Digite o valor da compra: '))
desc = 0

if compra > 500:
    desc = 1
    for i in range(1, ((compra-500)//100)+1):
        desc += 1
        if desc == 25:
            porc = compra*0.25
            print(f'{compra} - 25% = {compra-porc}')
            break
    porc = compra*(desc/100)
    print(f'{compra} - {desc}% = {compra-porc}')
else:
    print('O valor da compra não atende a política de descontos')