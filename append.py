arroz = float(input('qual o valor do arroz?'))
print(f'o preço do arroz é {arroz:.2f} reais')
if arroz >= 20:
    print('valor alto')
else:
    print('valor baixo')
feijão = float(input('e qual é o valor do feijão?'))
print(f'o preço do feijão é {feijão:.2f} reais')
if feijão >=14:
    print('valor alto')
else:
    print('valor baixo')
    
listadeprecos=[]
listadeprecos.append(arroz)
listadeprecos.append(feijão)
print(f'preços {listadeprecos}')