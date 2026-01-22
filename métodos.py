p = input('digite algo: ')
print('só tem números?' ,p.isnumeric())  # verifica exclusivamente se é número (inteiro)
print('é alfabético?' ,p.isalpha())    # verifica exclusivamente se é letra (aceita acentos)
print('é letra ou número?' ,p.isalnum())    # verifica exclusivamente se é letra ou número (aceita acentos)
print('está maiúsculo?' ,p.isupper())    # verifica exclusivamente se está em maiúsculo
print('está minúsculo?' ,p.islower())    # verifica exclusivamente se está em minúsculo
print('é espaço?' ,p.isspace())    # verifica exclusivamente se é espaço
print('está capitalizado?' ,p.istitle())    # verifica exclusivamente se está capitalizada

#VERIFICAR SE ALGO É UNICAMENTE PALAVRA (PODE TER ACENTO) -->
#name = input('enter the product name here: ').strip()
    #if name.replace(' ', '').isalpha():