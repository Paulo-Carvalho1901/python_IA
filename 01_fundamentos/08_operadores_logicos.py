# Operadores logicos

"""
And = Apnas retorna verdadeiro
apena quando todas as resposta forem verdadeira

or = Apenas retorna verdadeiro
apena quando uma das opções foram verdadeiras
ou uma ou outra

not = Inverte o os valores logicos
quando for False é True
quando for True é False
"""

usuario = input('Digite o seu usuario: ')
senha = input('Digite a sua senha: ')


login_valido = usuario == 'Admin' and senha == '1234'

print(f'Logado no sistema: {login_valido}')
