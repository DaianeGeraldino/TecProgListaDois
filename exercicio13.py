haste_aco = int(input('Digite a quantidade de hastes de aço compradas '))
haste_cobre = int(input('Digite a quantidade de hastes de cobre compradas '))
haste_aluminio = int(input('Digite a quantidade de hastes de aluminio compradas '))

valor_compra = (haste_aco*2.5) + (haste_cobre*4) + (haste_aluminio*5)
quantidade = haste_aco+haste_aluminio+haste_cobre

if quantidade<6:
    print(f'não há desconto é o valor da compra é de: {valor_compra}')

elif quantidade>7 and quantidade<15:
    porcentual = valor_compra * 0.10
    desconto = valor_compra - porcentual
    print(f'há desconto é o valor da compra é de: {desconto}')

elif quantidade>16 and quantidade<20:
    porcentual = valor_compra * 0.15
    desconto = valor_compra - porcentual
    print(f'há desconto é o valor da compra é de: {desconto}')

elif quantidade>20:
    porcentual = valor_compra * 0.20
    desconto = valor_compra - porcentual
    print(f'há desconto é o valor da compra é de: {desconto}')




