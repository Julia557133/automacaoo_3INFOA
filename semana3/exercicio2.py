'''
Exercício 2 - Semana 3
Crie um programa que imprime usando
for a figura abaixo:
*
**
***
****
*****
******
termina com 10 * na última linha
'''

def imprimir_figura():
    for i in range(1, 10):  # Loop de 1 a 6 (inclusive)
        print('*' * i)  # Imprime '*' repetido i vezes em cada linha

    # Imprime a última linha com 10 asteriscos
    print('*' * 10)

# Chama a função para imprimir a figura
imprimir_figura()
