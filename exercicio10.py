salario = float(input('Digite o valor do salario'))

if salario<1903.98:
    print(f'O salário líquido não há isenção de imposto é de: {salario}')

elif salario>1903.99 and salario<2826.65:
    imposto = (salario * 0.075) - 142.80 
    salario_liquido = salario-imposto
    print(f'O salário bruto é de: {salario} , a deducação de: {imposto:.2f} e o salário líquido de: {salario_liquido}')

elif salario>2826.66 and salario<3751.05:
    imposto = (salario * 0.15) - 548.82
    salario_liquido = salario-imposto
    print(f'O salário bruto é de: {salario} , a deducação de:{imposto:.2f} e o salário líquido de: {salario_liquido}')

elif salario>3751.06 and salario<4664.68:
    imposto = (salario * 0.225) - 636.13
    salario_liquido = salario-imposto
    print(f'O salário bruto é de: {salario} , a deducação de: {imposto:2f} e o salário líquido de: {salario_liquido}')
    
elif salario>4664.68:
    imposto = (salario * 0.275) - 869.36
    salario_liquido = salario-imposto
    print(f'O salário bruto é de: {salario} , a deducação de: {imposto:.2f} e o salário líquido de: {salario_liquido}')