import base


base = base.Database()
carga_total = int(input("Digite o valor de carga total: "))
itens = []

#Mochila Binaria
def mochila(pesos, valores, carga_total, n):
    if(n == 0 or carga_total == 0):
        return 0
    if(pesos[n-1] > carga_total):
        return mochila(pesos, valores, carga_total, n-1)
    else:
        itens.append([valores[n-1], pesos[n-1]])
        return max(valores[n-1] + mochila(pesos, valores, carga_total - pesos[n-1], n-1), mochila(pesos, valores, carga_total, n-1))

valor_entrega = mochila(base.pesos(), base.valores(), carga_total, len(base.pesos()))

itens.remove(itens[len(itens) - 1])

print(f"Todos os Pesos: {base.pesos()}")
print(f"Todos os Valores: {base.valores()}")
print(f"O limte de carga: {carga_total} kg")
print(f"Quantidade de itens: {len(base.pesos())}")
print(f"Valor total das entregas: R$ {valor_entrega} \n")
print(f"De acordo com a nossa analise, se a sua capacidade de carga é {carga_total} kg com os itens cadastrados... A melhor opção é levar os itens de peso e preço: ")

for peso in range(len(itens)):
    print(f"{peso+1}º Item de peso {itens[peso][1]} e preço {itens[peso][0]}")

