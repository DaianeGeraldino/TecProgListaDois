tipo = input('Digite o tipo industrial [I/C/R] ')
consumo = float(input('Digite a quantidade consumida '))

if tipo=='I':
    calculo = (0.68*consumo) + 34
    print(f'O valor da ftura será de: {calculo}')
elif tipo=='C':
    calculo = (0.37*consumo) + 45
    print(f'O valor da fatura será de: {calculo}')
elif tipo=='R':
    calculo = (0.77*consumo) -22
    print(f'O valor da fatura será de: {calculo}')