import math

valor_z = float(input('Digite o valor de z '))
valor_w = float(input('Digite o valor de w '))

if valor_z>0 or valor_w<7:
    x=((5*valor_w)+1)/3
    t=(5*valor_z)+2

else:
    x=(5*valor_z)+2
    t=((5*valor_w)+1)/3

y=(7*(math.pow(x,0.3)))-(3*(math.pow(x,0.5)))-(8*t)/(5*(x+1))
print(f'{y:.2f}')