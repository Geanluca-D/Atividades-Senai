# O usuário deve digitar a senha correta (1234). Enquanto errar, o
# programa deve pedir novamente.

senha = '1234'
tentativa = input('Digite a senha: ')

while tentativa != senha:
  tentativa = input('Senha incorreta, tente novamente: ')
print('Senha correta!')