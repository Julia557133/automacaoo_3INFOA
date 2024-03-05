'''
Exercício 1 - Semana 3
Crie um programa que imprime todos 
os números pares no intervalo de 
0 a 20.
'''

def imprimir_numeros_pares():
    print("Números pares no intervalo de 0 a 20:")
    for i in range(0, 21, 2):  # Começa em 0, vai até 20 (inclusive), pulando de 2 em 2
        print(i)

# Chama a função para imprimir os números pares
imprimir_numeros_pares()
