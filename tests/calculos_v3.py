lista = ['25', '25', '25', '25', '25', '25', '25', '31', '25', '25', '25', '26', '28', '28', '45', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '10', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30']

ventana_hasta = 10

def calculo_temp_dias(lista_grados):
    entre_dia_y_dia = []

    for i in range(0, len(lista_grados)-(ventana_hasta-1)):
        ventana = lista_grados[i:i+ventana_hasta]
        diferencia = int(ventana[0]) - int(ventana[ventana_hasta-1])
        if abs(diferencia) > 5:
            entre_dia_y_dia.append(i+1)
            entre_dia_y_dia.append(i+ventana_hasta)
    return entre_dia_y_dia

# print(calculo_temp_dias(lista))


print(calculo_temp_dias(lista))

