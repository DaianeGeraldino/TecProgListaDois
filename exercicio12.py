sexo = input('Digite o sexo [fem/masc] ')
idade = int(input('digite a idade '))

if sexo=='masc' and idade>=21 or sexo=='fem' and idade>=18:
    print('maior de idade')
else:
    print('menor de idade')