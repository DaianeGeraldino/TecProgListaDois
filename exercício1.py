salario = float(input('Digite o valor do seu salário'))
valor_financiamento = float(input('Digite o valor do seu financiamento pretendido'))

if(valor_financiamento<=5*salario):
    print("financiamento concedido")
else:
    print("Financiamento negado")

print('Obrigado por nos consultar')
