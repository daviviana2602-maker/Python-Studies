vendas=(1000+1500+2000)
custo=(500+750+1000)
if vendas > 4000:# bool aqui
    print("funcionário ganhou bônus")
else:
    print("funcionário não ganhou bônus")
lucro=vendas-custo
print(lucro)
if lucro > 1500:
    print("bom resultado")
else:
    print("resultado ruim")

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
    
for i in range(3):

        print("quem será o funcionário do mês?")
