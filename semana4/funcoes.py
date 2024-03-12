





















'''
As funções permitem modularizar o código, dividir ele em partes menores que podem ser reaproveitadas. Isso simplifica a codificação.

Estrutura função em python

def nomes_funcao(param1, param2, entradaN):
    //algum codigo que a função faz 
    return saída_da_funcao


#Cria uma função que calcula a área de um triângulo
def calculateTringleArea(base, altura):
    area = (base * altura) / 2
    return area :

#Exemplo 1: chamar função
area1 = calculateTringleArea(100,10)
print("A área do triângulo é: ", area)

#Exemplo 2: Chamar a função novamente
base = float(input('Digite a base: '))
altura =  float(input('Digite a altura: '))
area2 = calculateTringleArea(base, altura)
print("A área do triângulo 2 é", area2)
'''