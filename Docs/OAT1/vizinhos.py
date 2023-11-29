import base

base = base.Database()

distancias = base.calcularDistancias() # 2n + n²

locais = [distancias[0][0]]

for d in distancias:
    if(d[0] != locais[len(locais) - 1]):
        locais.append(d[0])
caminho = []

def encontrar_proximo(local_atual, locais_nao_visitados): # n²
    menor_distancia = float('inf')
    proximo_local = None
    for destino in locais_nao_visitados:
        if destino != local_atual:
            distancia = [item[2] for item in distancias if item[0] == local_atual and item[1] == destino][0]
            if distancia < menor_distancia:
                menor_distancia = distancia
                proximo_local = destino
    return [proximo_local, menor_distancia]

local_atual = distancias[0][0]
locais_nao_visitados = locais.copy()
locais_nao_visitados.remove(local_atual)

# n³
for x in range(len(locais) - 1):  # -1 rodar o código sem erros
    proximo = encontrar_proximo(local_atual, locais_nao_visitados)
    caminho.append((local_atual, proximo[0], proximo[1]))
    local_atual = proximo[0]
    locais_nao_visitados.remove(proximo[0])

# Adicione o retorno ao Estabelecimento no final
estabelecimento = distancias[0][0]
for y in distancias:
    if(y[1] == estabelecimento and y[0] == local_atual):
        caminho.append((y[0], y[1], y[2]))

for origem, destino, distancia in caminho:
    print(f"{origem} para {destino} em uma distancia de: {distancia} Km")