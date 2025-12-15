p = input('digite algo: ')
print('só tem números?' ,p.isnumeric())  #verifica se é número
print('é alfabético?' ,p.isalpha())    #verifica se é letra
print('é letra ou número?' ,p.isalnum())    #verifica se é letra ou número
print('está maiúsculo?' ,p.isupper())    #verifica se está em maiúsculo
print('está minúsculo?' ,p.islower())    #verifica se está em minúsculo
print('é espaço?' ,p.isspace())    #verifica se é espaço
print('está capitalizado?' ,p.istitle())    #verifica se está capitalizada