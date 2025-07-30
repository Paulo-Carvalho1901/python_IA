# Usuario logago

login = input('Digite seu login: ')
senha = int(input('Digite sua senha: '))

usuario_login = 'Admin'
senha_permitida = 1234

if login == usuario_login and senha == senha_permitida:
    print('Usuário logado no sistema!')
else:
    print('Usuário ou senha incorretos!')