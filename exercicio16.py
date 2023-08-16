numero = int(input('Digite um numeros de três algarismos '))

if 100 <= numero <= 999:
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10
    soma = centenas + dezenas + unidades
        
    print(f"A soma dos dígitos de {numero} é {soma}.")
else:
    print("Número inválido. Por favor, digite um número de três dígitos.")

if soma%16 == 0 and soma% 4 == 0:
    print("O número é divisor de 16 e múltiplo de 4.")
else: 
    print('O número não é divisor de 4 e 16 ao mesmo tempo')