import indexador
import base

indexadores = []
base = base.Database()

class ControllerIndexador():
    def inserirIndexador(indexador):
        indexadores.append(indexador)

    def buscarIndexador(indexador):
        for i in indexadores:
            if(i == indexador):
                return i
            else:
                return "Indexador não existe"

    def excluirIndexador(indexador):
        indexadores.remove(indexador)

    def criarIndexadores(self):
        for e in range(len(base.getBase()['estabelecimentos'])):
            estabelecimentoid = base.getBase()['estabelecimentos'][e]['id']
            for p in range(len(base.getBase()['estabelecimentos'][e]['entregas'])):
                pedidosid = base.getBase()['estabelecimentos'][e]['entregas'][p]['id']
                indexadores.append([estabelecimentoid, pedidosid])
        return indexadores