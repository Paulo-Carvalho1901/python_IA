nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

idade_int = int(idade)
# fruta_favorita = input('Qual sua fruta favorita? ')

# Sem f-string
# print('Olá', nome, 'Você tem', idade, 'anos de idade.')

# f-string
# print(f'Olá, {nome} você tem {idade} anos de idade e sua fruta favorita é {fruta_favorita}.')

print(f'Olá {nome} daqui 5 anos você tera {idade_int + 5} de idade.')
