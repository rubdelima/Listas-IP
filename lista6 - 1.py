dicc = {}
matriz = []
for i in range(5):
    lista = input().split(" - ")
    lista[1] = int(lista[1])
    if lista[1] not in dicc:
        dicc[lista[1]] = []
    dicc[lista[1]].append(lista[0])
print(dicc)
