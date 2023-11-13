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
    return proximo_local

local_atual = distancias[0][0]
locais_nao_visitados = locais.copy()
locais_nao_visitados.remove(local_atual)

# n³
for _ in range(len(locais) - 1):  # -1 para evitar repetir McDonalds na primeira vez
    proximo = encontrar_proximo(local_atual, locais_nao_visitados)
    caminho.append((local_atual, proximo))
    local_atual = proximo
    locais_nao_visitados.remove(proximo) 

# Adicione o retorno ao McDonalds no final
caminho.append((local_atual, distancias[0][0]))

for origem, destino in caminho:
    print(f"{origem} para {destino}")

print(distancias)