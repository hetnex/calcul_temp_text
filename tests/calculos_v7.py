lista = [25, 25, 25, 25, 25, 25, 25, 31, 25, 25, 25, 26, 28, 28, 45, 29, 29, 25, 25, 25, 25, 25, 25, 29, 28, 28, 10, 29, 29, 29, 29, 29, 25, 26, 26, 26, 26, 26, 26, 29, 29, 29, 28, 29, 29, 29, 29, 28, 28, 29, 27, 24, 24, 27, 27, 27, 27, 29, 28, 28, 25, 25, 25, 25, 25, 25, 25, 28, 28, 29, 28, 29, 28, 28, 26, 26, 26, 26, 26, 26, 26, 30]
ventana_lista = 10

for x in range(0, len(lista), ventana_lista):
    lista_aux = sorted(lista[x:x+ventana_lista])
    minV = lista_aux[0]
    for j,i in enumerate(lista_aux):
        if abs(minV-i) >= 5:
            print("diff-temp", i-minV, "min", minV, "break", i, "dia", j+1+x)
            break
