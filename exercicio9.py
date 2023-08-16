sexo = input('Digite o sexo [fem/masc] ')
peso = float(input('Digite o peso '))
altura = float(input('digite a altura em cm '))
idade = int(input('digite a sua idade '))

if sexo=='fem':
    calorias = 66+(13.7*peso)+(5*altura)-(6.8*idade)
    print(f'O valor ideal de calorias é de: {calorias}')

elif sexo=='masc':
    calorias = 66.5+(9.6*peso)+(1.8*altura)-(4.7*idade)
    print(f'O valor ideal de calorias é de: {calorias}')