media = float(input('Digite sua média'))
falta = int(input('Digite a quantidade de faltas'))

if media>=7 and falta<=32:
    print("Voce está aprovado")
elif media<7 and falta<=32 or media>=7 and falta>32 or media<7 and falta>32:
    print('Voce está reprovado')