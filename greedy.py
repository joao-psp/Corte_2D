#encoding: utf-8
import pandas as pd
import time
import timeit
"""
Acho que isso vai funcionar pelo menos vai ser um gulosão...
Tipo se eu tenho uma chapa de 50 x 10 = 500 , então cabem no max 500 unidades de área,
como cada retangulinho tem uma área tem como "aproximar" ....
"""

class item:
    def __init__(self, tipo,x, y,valor=0,min=0,max=0):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.valor = valor
        self.area = x*y
        self.min = min
        self.max = max
        self.qtd = 0
        self.heuristic = self.valor/self.area


def ordenarRet(retangulos):
    # ordenar por valor decrescente, do maior pro menor
    return sorted(retangulos, key=lambda x: x.heuristic, reverse=True)

def calcNovos(retangulos,x,y):
    ret = []
    for i in retangulos:
        if i.x <= x and i.y <= y:
            ret.append(i)
    return ret


def main():
    retanguloGrande = item(0,30,30)
    retangulos = []
    selecionados = []
    funcObjetivo =0

    # retangulos.append(item(1,3,5,65,0,2))
    # retangulos.append(item(2,2,3,60,0,2))
    # retangulos.append(item(3,5,2,50,0,2)) # alterar os parametros 2 e 3 para ver que funciona +-

    # for i in range(1,21):
          # TODO: ler arquivo e pegar x,y,valor, min max só copiar os  dados da tabela do artigo
    #     retangulos.append(item(x,y,valor,min, max)) valores na tabela

    # TODO:  ordenar por valor decrescente, do maior pro menor

    df = pd.read_csv("dados.csv", sep=";")
    for index, row in df.iterrows():
        retangulos.append(item(row["peca"], row["l"], row["w"], row["v"], row["p"],row["q"]))

    retOrdenados = ordenarRet(retangulos)
    retOrdenados = retangulos

    inicio = timeit.default_timer()
    i=0
    while (i < len(retOrdenados)):
        print(retOrdenados[i].max)
        if retOrdenados[i].area <= retanguloGrande.area and retOrdenados[i].qtd < retOrdenados[i].max:
            retOrdenados[i].qtd = retOrdenados[i].qtd + 1
            retanguloGrande.area = retanguloGrande.area - retOrdenados[i].area
            auxX = retanguloGrande.x - retOrdenados[i].x
            auxY = retanguloGrande.y - retOrdenados[i].y
            selecionados.append(retOrdenados[i])
            #i = 0
        else:
            i = i +1
            retOrdenados = calcNovos(retOrdenados,auxX,auxY)


    fim = timeit.default_timer()
    for i in selecionados:
        print("Tipo: %d Quantidade: %d"%(i.tipo, i.qtd)) # insere repetido na lista msm...
        funcObjetivo = funcObjetivo + (i.valor)
    print("Valor da funcção objetivo:")
    print(funcObjetivo)

    print("Tempo de execução %f segundos"%((fim-inicio)*1000))


main()
