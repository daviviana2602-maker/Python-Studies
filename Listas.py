print ("lista de produtos")
listadeprodutos=['iphone', 'carro', 'casa']
for produto in listadeprodutos:
    print(produto)
    
print ("lista de preços")
listadepreços=[1000, 1500, 2000]
for preço in listadepreços:
    print(preço)
    
nome = input('olá, qual é o seu nome?')
print(f'olá, {nome}! prazer em te conhecer!')
dia = input(f'em que dia você nasceu, {nome}?')
mes = input('que mes você nasceu?')
ano = input('em que ano você nasceu?')
print(f'você nasceu no dia {dia} de {mes} de {ano}. Correto?')
