hora_inicio = int(input("Digite a hora de início do jogo (0 a 23): "))
min_inicio = int(input("Digite os minutos de início do jogo (0 a 59): "))
hora_termino = int(input("Digite a hora de término do jogo (0 a 23): "))
min_termino = int(input("Digite os minutos de término do jogo (0 a 59): "))

if hora_inicio < 0 or hora_inicio > 23 or min_inicio < 0 or min_inicio > 59 or \
    hora_termino < 0 or hora_termino > 23 or min_termino < 0 or min_termino > 59:
    print("Entrada de dados não é válida.")
else:
    minutos_total_inicio = hora_inicio * 60 + min_inicio
    minutos_total_termino = hora_termino * 60 + min_termino
    
    if minutos_total_termino >= minutos_total_inicio:
        duracao_minutos = minutos_total_termino - minutos_total_inicio
    else:
        duracao_minutos = (24 * 60 - minutos_total_inicio) + minutos_total_termino
    
    duracao_horas = duracao_minutos // 60
    duracao_minutos = duracao_minutos % 60
    
    print(f"A duração do jogo é de {duracao_horas} horas e {duracao_minutos} minutos.")