# Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha
# correta definida previamente.

senha = '1234'
tentativa = input('Digite a senha: ')

while tentativa != senha:
  tentativa = input('Senha incorreta. Tente de novo: ')