nome_um = input('Digite o nome da primeira pessoa ')
idade_um = int(input('Digite a idade da primeira pessoa '))
print("")
nome_dois = input("Digite o nome da segunda pessoa ")
idade_dois = int(input("Digite a idade da segunda pessoa "))
print("")
ano_atual = int("Digite o ano atual")

calculo_ano_um = ano_atual-idade_um
calculo_ano_dois = ano_atual-idade_dois

if(idade_um>idade_dois):
    print(f'A pessoa mais nova é a {nome_dois} em: {calculo_ano_dois}')
elif(idade_um<idade_dois):
    print(f'A pessoa mais nova é a {nome_um} nascida em: {calculo_ano_um}') 
elif(idade_um==idade_dois):
    print(f'A {nome_um} e {nome_dois} possuem as mesmas idades nascidas em: {calculo_ano_um}')