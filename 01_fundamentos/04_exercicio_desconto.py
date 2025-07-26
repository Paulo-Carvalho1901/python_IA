preco = float(input('Digite o valor do produto: ')) # valor em R$
desconto = float(input('Digite o desconto ser dados no produto: ')) # desconto em %

preco_desconto = preco - (preco * desconto / 100)
print(f'O valor do produto com desconto é de {preco_desconto}')
