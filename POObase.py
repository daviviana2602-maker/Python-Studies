#Classe
#Molde / modelo.
#Define o que o objeto será.

#Objeto
#Instância real da classe.
#Algo que você cria a partir da classe.

#Atributos
#Características do objeto (nome, idade, saldo…).

#Métodos
#Ações que o objeto executa (depositar, falar, andar…).

#Construtor __init__(self):
#Função que roda automaticamente quando um objeto é criado.
#self é automaticamente substituído pelo objeto que chama o método
#Serve pra inicializar atributos.


          #PONTOS#
          
#1. Encapsulamento
#Esconde detalhes internos.
#Usa métodos para acessar/alterar valores.
#Evita qualquer um mexer direto nos atributos.

#Exemplo:
#um objeto ContaBancaria não deixa você alterar o saldo direto — só via métodos seguros.


#2. Herança
#Uma classe pega características de outra.
#Evita repetição.
#Cria relação “é um”.

#Exemplo:
#Funcionario → Gerente herda tudo e adiciona o que é exclusivo dele.


#3. Polimorfismo
#Um mesmo método pode se comportar de maneiras diferentes dependendo do objeto.
#Reescrever métodos da classe mãe (override).
#Útil quando subclasses fazem a “mesma coisa”, mas do seu jeito.

#Exemplo:
#Animal.fazer_som()
#↳ Cachorro.fazer_som() → “au au”
#↳ Gato.fazer_som() → “miau”


#4. Abstração
#Focar só no que importa e ignorar o resto.
#Criar modelos simples de algo complexo.
#Mostrar pro usuário apenas o essencial.

#Exemplo:
#Você digita .depositar(100) e não precisa saber toda a lógica interna.