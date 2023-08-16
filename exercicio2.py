temp_carroUm = float(input('Digite a tempo do primero carro '))
print("")
dist_carroUm = float(input('Digite a distância percorrida pelo primeiro carro '))
print("")

temp_carroDois = float(input('Digite a tempo do segundo carro '))
print("")
dist_carroDois = float(input('Digite a distância percorrida pelo segundo carro '))
print("")

vel_mediaUm = dist_carroUm/temp_carroUm
vel_mediaDois = dist_carroDois/temp_carroDois

if(vel_mediaUm<vel_mediaDois):
    print(f'A velocidade maior é do segundo carro com: {vel_mediaDois}')

elif(vel_mediaUm==vel_mediaDois):
    print('Os dois carros possuem as mesmas velocidades médias')

elif(vel_mediaUm>vel_mediaDois):
    print('A velocidade do carro um é superior')