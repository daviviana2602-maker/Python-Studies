from math import sqrt
num = int(input('digite um número e descubra sua raiz quadrada: '))
if num < 0:
    print('este número não contém raiz quadrada real')
else:
    raiz = sqrt(num)
    print(f'a raíz quadrada de {num} é {raiz:.2f}')