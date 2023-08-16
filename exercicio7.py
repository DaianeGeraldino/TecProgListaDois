prim_angulo = float(input('Digite o primeiro angulo'))
seg_angulo = float(input('Digite o segundo angulo'))
terc_angulo = float(input('Digite o terceiro angulo'))

if (prim_angulo+seg_angulo+terc_angulo) == 180:
    if prim_angulo<90 and seg_angulo <90 and terc_angulo<90:
        print('é acutângulo')
    elif prim_angulo==90 or seg_angulo == 90 or terc_angulo==90:
        print('é retângulo')
    elif prim_angulo>90 or seg_angulo>90 or terc_angulo>90:
        print('Obtusângulo')

else:
    print('Os ângulos informados não formam um triângulo')