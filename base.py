import json
import math


#Coletando dados do json e criando uma matriz;
class Database():
    def __init__(self):
        with open('pedidos.json', 'r', encoding="utf8") as d:
            self.base = json.load(d)

    #Pegado atributo base
    def getBase(self):
        return self.base
    
    #Coletando locais de entrega
    def locaisEntrega(self):
        local = []
        locais = [[0, self.base['nome'], self.base['localizacao'][0], self.base['localizacao'][1]]]
        for i in range(len(self.base['entregas'])):
            local.append(self.base['entregas'][i]['id'])
            local.append(self.base['entregas'][i]['destinatario'])
            local.append(self.base['entregas'][i]['localizacao'][0])
            local.append(self.base['entregas'][i]['localizacao'][1])
            locais.append(local)
            local = []
        return locais
    
    def calcularDistancias(self):
        destinos = []
        distancia = None
        locais_entrega = self.locaisEntrega()
        distancias = []
        raio_terra = 6371
        #Anotando os destinos
        for l in locais_entrega:
            destinos.append(l[1])
        #Formula de Haversine 
        for ds in range(len(locais_entrega)):
            lat1 = locais_entrega[ds][2]
            lon1 = locais_entrega[ds][3]
            #Raiz quadrada
            lat1 = math.radians(lat1)
            lon1 = math.radians(lon1)
            for ds2 in range(len(locais_entrega)):
                lat2 = locais_entrega[ds2][2]
                lon2 = locais_entrega[ds2][3]
                #Raiz quadrada
                lat2 = math.radians(lat2)
                lon2 = math.radians(lon2)
                #Diferença entre os pontos
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distancia = raio_terra * c
                distancias.append([locais_entrega[ds][1], locais_entrega[ds2][1], int(distancia)])
        return distancias