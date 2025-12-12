n1 = int(input('digite um valor:'))
n2 = int(input('digite outro valor:'))
soma = n1 + n2
print(f'{n1} somado a {n2} é {soma}')

n1 = float(input('digite um valor:'))
n2 = float(input('digite outro valor:'))
soma = n1 + n2
print(f'{n1} somado a {n2} é {soma}')

n1 = input('digite um valor: ')
n2 = input('digite outro valor: ')
soma = n1 + n2
print(f'{n1} somado a {n2} é {soma}')

idade = 18
print("Você tem " + str(idade) + " anos") #str = string
idade = 18
print(f"Você tem {idade} anos") #f pode ser usado para formatar strings

idade = int(input("Digite sua idade: "))
maior = idade >= 18   # isso aqui é um bool (True ou False)
print(f"Você é maior de idade? {maior} ")
if maior:
    print("Entrada permitida.")
else:
    print("Entrada negada.")