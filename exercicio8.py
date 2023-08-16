distancia = float(input('Digite a distancia percorrida pelo carro'))
gasolina = float(input('quantidade de gasolina consumida'))

consumo = distancia/gasolina

if consumo<8:
    print("Venda o carro!")
elif consumo>8 and consumo<14:
    print('Econômico!')
elif consumo>12:
    print('Super econômico!')