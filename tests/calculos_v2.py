# lista = ['25', '25', '25', '25', '25', '25', '25', '31', '25', '25', '25', '26', '28', '28', '45', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '10', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30']
# mRange = 5
# cuantas_veces = ""
# cuantas_veces_index = ""
# diferencia_de_temp = ""

# este_numero = 0
# lista_de_numeros = []


# for i in range(len(lista)):
#     if(i%5 == 0):
#         if (i+5) < len(lista):
#             mRange = i+5
#             lista_de_numeros.clear()
#         else:
#             mRange = len(lista)
#     for j in range(i+1, mRange):
#         print(lista[i], " - ", lista[j], " = ", abs(int(lista[i])-int(lista[j])))
#         este_numero = abs(int(lista[i])-int(lista[j]))
#         lista_de_numeros.append(este_numero)
#         print("Aqui imprimo la len lista", len(lista_de_numeros))

#         if este_numero >= 5 and i:
#             print("Entre el dia ", i+1, " y el dia ", j+1, " hay una diferencia de ", este_numero)



# lista = [22, 22, 23, 25, 29, 27, 22, 23, 25, 26, 29, 30]
# para imprimir directamente dentro del for, los dias que tienes las subidas de temp
# ventana_hasta = 10
# for i in range(0, len(lista)-(ventana_hasta-1)):
#     ventana = lista[i:i+ventana_hasta]
#     diferencia = int(ventana[0]) - int(ventana[ventana_hasta-1])
#     if abs(diferencia) > 5:
#         print("La diferencia de temp esta entre los dias", i, i+(ventana_hasta-1))


lista = ['25', '25', '25', '25', '25', '25', '25', '31', '25', '25', '25', '26', '28', '28', '45', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '10', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30']
ventana_hasta = 10

entre_dia_y_dia = []

for i in range(0, len(lista)-(ventana_hasta-1)):
    ventana = lista[i:i+ventana_hasta]
    diferencia = int(ventana[0]) - int(ventana[ventana_hasta-1])
    if abs(diferencia) > 5:
        print(entre_dia_y_dia.append(i+1))
        print(entre_dia_y_dia.append(i+(ventana_hasta-1))