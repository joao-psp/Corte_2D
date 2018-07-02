#encoding: utf-8

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


def ordenarRet(retangulos):
    # ordenar por valor decrescente, do maior pro menor
    pass


def main():
    retanguloGrande = item(0,5,7)
    retangulos = []
    selecionados = []
    funcObjetivo =0

    retangulos.append(item(1,3,5,65,0,2))
    retangulos.append(item(2,2,3,60,0,2))
    retangulos.append(item(3,5,2,50,0,2))

    # for i in range(1,21):
          # TODO: ler arquivo e pegar x,y,valor, min max
    #     retangulos.append(item(x,y,valor,min, max)) valores na tabela

    # TODO:  ordenar por valor decrescente, do maior pro menor
    retOrdenados = ordenarRet(retangulos)
    retOrdenados = retangulos

    i=0
    while (i < len(retOrdenados)):
        print(retOrdenados[i].max)
        if retOrdenados[i].area <= retanguloGrande.area and retOrdenados[i].qtd < retOrdenados[i].max:
            retOrdenados[i].qtd = retOrdenados[i].qtd + 1
            retanguloGrande.area = retanguloGrande.area - retOrdenados[i].area
            selecionados.append(retOrdenados[i])
            i = 0
        else:
            i = i +1



    for i in selecionados:
        print(i.tipo, i.qtd)
        funcObjetivo = funcObjetivo + (i.valor)
    print("Valor da funcção objetivo:")
    print(funcObjetivo)


main()
