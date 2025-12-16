n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor:'))
s = n1 + n2 #soma
sub = n1 - n2 #subtração
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divisão inteira
p = n1 ** n2 #potência
rq = n1 ** (1/2) #raiz quadrada
rq2 = n2 ** (1/2) #raiz quadrada
rc = n1 ** (1/3) #raiz cúbica
rc2 = n2 ** (1/3) #raiz cúbica
print(f'\nSoma: {s}', end = ' ') 
print(f'Subtração: {sub}')
print(str('------------------------------'))
print(f'Multiplicação: {m}', end = ' ')
print(f'Potência: {p}')
print(f'Divisão: {d:.2f}', end = ' ')
print(f'Divisão inteira: {di}')
print(str('------------------------------'))
print(f'Raiz quadrada: {n1} → {rq:.2f}, {n2} → {rq2:.2f}')
print(f'Raiz cúbica: {n1} → {rc:.2f}, {n2} → {rc2:.2f}')

#ordem de precedência: 1º parênteses, 2º potência, 3º multiplicação/divisão, 4º soma/subtração