lista_dicionarios = []
with open("iris.data") as arquivo: 
    for line in arquivo:
        dicio = dict()
        lista = line.replace(",", ' ')
        lista = lista.split()
        print(lista)
        id_dado = 0
        for item in lista:
            if id_dado == 0:
                dicio["sepal-lenght"] = item
            elif id_dado == 1:
                dicio["petal-lenght"] = item
            elif id_dado == 2:
                dicio["sepal-widht"] = item
            elif id_dado == 3:
                dicio["petal-widht"] = item
            else:
                dicio["class"] = item
            id_dado += 1
        if len(dicio) == 0:
            pass
        else:
            lista_dicionarios.append(dicio)
print(lista_dicionarios)
        
