#Problemas combinatórios: Problema da Mochila 0/1 - (0/1 Knapsack Problem)

cesta_de_frutas = [
    {'nome': 'Abacate', 'peso': 3, 'valor': 8},
    {'nome': 'Abacaxi', 'peso': 5, 'valor': 7},
    {'nome': 'Manga', 'peso': 4, 'valor': 4},
    {'nome': 'Maça', 'peso': 2, 'valor': 6},
]

capacidade_cesta = 9
numero_de_itens = len(cesta_de_frutas)

total_de_combinacoes = 2 ** numero_de_itens

melhor_combinacao = []
maior_valor_encontrado = 0
peso_da_melhor_combinacao = 0

print(f'Frutas disponiveis: {[item['nome'] for item in cesta_de_frutas]}')
print(f'Capacidade máxima da cesta: {capacidade_cesta}')
print(f'Total de combinações: {total_de_combinacoes}')
print('-' * 45)
print('.' * 45)

for numero in range(total_de_combinacoes):
    escolhas = bin(numero)[2:].zfill(numero_de_itens)
    combinacao_atual = []
    peso_atual = 0
    valor_atual = 0

    for indice in range(numero_de_itens):
        if escolhas[indice] == '1':
            item = cesta_de_frutas[indice]
            combinacao_atual.append(item['nome'])
            peso_atual += item['peso']
            valor_atual += item['valor']

    if len(combinacao_atual) == 0:
        texto_itens = '[] - (conjunto vazio)'
    else:
        texto_itens = '{' + ', '.join(combinacao_atual) + '}'

    if peso_atual <= capacidade_cesta:
        status = '(válido)'
        if valor_atual > maior_valor_encontrado:
            maior_valor_encontrado = valor_atual
            peso_da_melhor_combinacao = peso_atual
            melhor_combinacao = texto_itens
    else:
        status = f'(inválido: peso {peso_atual} > capacidade maxima ({capacidade_cesta}))'

    print(f' {texto_itens}: peso {peso_atual}, valor {valor_atual} {status}')
    print('.' * 45)

print('-' * 45)
print(f'Melhor combinação encontrada: {melhor_combinacao}')
print(f'Peso total da melhor combinação: {peso_da_melhor_combinacao}')
print(f'Valor total da melhor combinação: {maior_valor_encontrado}')