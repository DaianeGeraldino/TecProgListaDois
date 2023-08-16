mes = int(input('Digite o mes em número '))
ano = int(input('Digite o ano '))
ano_bissexto = False

if ano%4==0:
    ano_bissexto = True

if mes == 1 or mes ==3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30

if ano_bissexto:
    if mes == 2:
        dias = 29
else:
    dias = 28

if mes<1 and mes>12:
    print('Digite um mês valido')
else:
    print(f'O mes {mes} do ano {ano} possui {dias}')
