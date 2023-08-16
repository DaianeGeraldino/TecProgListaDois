nome = input("Digite seu nome")
nota_um = float(input("Digite a primeira nota"))
nota_dois = float(input("Digite a segunda nota"))

media = (nota_um+nota_dois)/2

if (media>=0 and media<5):
    print(f'{nome} está reprovado com uma nota de {media}')
elif (media>=5 and media<7):
    print(f'{nome} está de recuperação com uma nota de: {media}')
elif (media>=7 and media<=10):
    print(f'{nome} está aprovado com uma média de: {media}')