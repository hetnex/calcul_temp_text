lista_1 = ['25', '25', '25', '25', '25', '25', '25', '31', '25', '25', '25', '26', '28', '28', '45', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '10', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30']


def calculo_temp_dias (lista):
    cantidad_de_item = 10 # Dias de las cuales vas a ver la diferencia de temperatura.
    lista_aux = []
    dict_de_dias_5_grados = {}
    for x in range(0, len(lista), cantidad_de_item): # Bucle que se encarga de coger la lista aux de solo cogemos lo que tenemos en cantidad_de_item
        lista_aux = lista[x:x+cantidad_de_item] # Lista donde se guarda 
        z = 0 # 2 Variables, donde utilizamos en el bucle de diferencia de temps
        b = 0
        for i in lista_aux: # Itero con la lista (en la cual solo tengo cantidad_de_item), para coger cada item de la lista, y poder trabajar con el
            z += 1 # Sumo esta variable, para coger siempre el numero siguiente a la lista
            if z >= len(lista_aux): # Esto es para parar cuando z llega al ultimo numero de la lista
                break
            b += abs(int(i)-int(lista_aux[z])) # La diferencia de cada item, la guardo en b
            if b > 5: # Si b es igual a los grados que queremos medir, paro ahi
                dict_de_dias_5_grados[x+z+1] = b # Guardo los resultados en el dicionario, key = dias donde se encuentra la diferencia. value = la diferencia de temps
                # print("Hay una diferencia de 5 grados. Entre los dias", x+1, "y", x+cantidad_de_item, "Es decir, el dia", x+z+1)
                break
    return dict_de_dias_5_grados
print(calculo_temp_dias(lista_1))
