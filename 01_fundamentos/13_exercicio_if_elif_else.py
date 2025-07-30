idade = int(input('Digite sua idade: '))
autorização_pais = input('Tem autorização dos pais? (S/N): ')

if idade >= 18:
    print('Acesso ao sistema autorizado.')
elif idade >= 16 and autorização_pais == 's':
    print('Acesso ao sistema autorizado pelo pais.')
else:
    print('Você não tem autorização.')