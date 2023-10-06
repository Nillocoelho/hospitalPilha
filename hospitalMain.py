from hospital.hospital import FilaEncadeada, Paciente
    
fila = FilaEncadeada()
p = Paciente()

while True:
    numero = int(input("""\nClinica Medica - Atendimento
    =============
    1. Incluir paciente
    2. Realizar chamada
    3. Consultar a posição atual
    4. Listar a quantidade de pacientes atendidos
    5. Sair\n"""))
    
    
    if numero == 1:
        p1 = Paciente('Jose', 123456, 'PlusMed')
        p2 = Paciente('Joao', 125895, 'Hapvida')

        fila.enfileirar(p1)
        fila.enfileirar(p2)
        print(fila)

    if numero == 2:
    
        fila.desenfileirar()
        print(fila)

    if numero == 3:
        print(fila.consulta())

    if numero == 4:
        print(fila.contagem())

    if numero == 5: 
        break
    