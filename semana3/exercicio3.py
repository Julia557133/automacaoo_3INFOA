'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

def dividir_em_grupos(matriculas):
    grupo1 = []
    grupo2 = []
    grupo3 = []

    for matricula in matriculas:
        if matricula % 3 == 0:
            grupo1.append(matricula)
        elif matricula % 3 == 1:
            grupo2.append(matricula)
        else:
            grupo3.append(matricula)

    return grupo1, grupo2, grupo3

def ler_matriculas():
    matriculas = []
    while True:
        matricula = int(input("Digite a matrícula (digite 0 para parar): "))
        if matricula == 0:
            break
        matriculas.append(matricula)
    return matriculas

# Lê as matrículas do teclado
matriculas = ler_matriculas()

# Divide as matrículas em grupos
grupo1, grupo2, grupo3 = dividir_em_grupos(matriculas)

# Imprime os grupos
print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)
print("Grupo 3:", grupo3)
