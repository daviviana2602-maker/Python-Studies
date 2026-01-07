print('hello, good morning'.find('llo')) #llo started in position two
print('hello' in 'hello, good morning') #Verify if the string exists
print('hello, good morning'.replace('hello', 'olá')) #change strings

print('hello, good morning'.capitalize())
print('hello, good morning'.title())
print('HELLO, GOOD MORNING'.lower())
print('hello, good morning'.upper())

print('   hello, good morning   '.strip()) #removes extra spaces
print('   hello, good morning   '.lstrip()) #removes extra spaces at the beginning
print('   hello, good morning   '.rstrip()) #removes extra spaces at the end

print('hello, good morning bro'.split()) #divide the strings into a list
print(' '.join(['hello,', 'good', 'morning', 'bro'])) #join the strings

frase = 'arroz'
print('A' in frase.upper())