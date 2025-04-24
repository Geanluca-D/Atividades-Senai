#Você foi contratado para desenvolver uma funcionalidade de “Desfazer/Refazer"
#para um editor de texto simples. O editor permite que o usuário escreva palavras
#em um documento, e, caso cometa um erro, pode desfazer a última ação ou
#refazê-la caso mude de ideia.
refazer = []

texto = list(input('Digite seu texto: ').split())
print(texto)
print()

while True:
    desfazer = input('Digite "d" se quiser desfazer a última palavra, ou "c" para continuar: ')
    while desfazer != 'c':
        refazer.insert(0, texto[-1])
        texto.pop()
        print(texto)
        print()
        desfazer = input('Digite "d" se quiser desfazer a última palavra, ou "c" para continuar: ')
    print()
    if len(refazer) > 0:
         refaz = input('Digite "r" se deseja refazer as palavras desfeitas, ou "t" para exibir o texto: ')
         if refaz == 'r':
            texto.append(refazer)
            print(texto)
            break
         elif refaz == 't':
            print(texto)
            break
         else:
            print('Valor inválido')
            break
    if desfazer == 'c':
        print()
        print(texto)
        break