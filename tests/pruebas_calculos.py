

# ####### Calculos: ###########

# # Suma de las temperaturas
# def suma_temperatura(la_suma_temp):
#     total = 0
#     for temps in la_suma_temp: 
#         total += int(temps)
#     return total

# # Media de las temperaturas
# def media_temperatura(la_media_temp):
#   suma_temp = suma_temperatura(la_media_temp)
#   average = suma_temp / len(la_media_temp)
#   return average

# # Temperatura baja, ordenamos la lista, y sacamos la primera posicion, que es la menor de todas
# def temperatura_baja(lista_temperatura):
#   lista_temperatura.sort()
#   return lista_temperatura[0]

# # Temperatura alta, ordenamos la lista, y sacamos la ultima posicion, que es la mayor de todas
# def temperatura_alta(lista_temperatura):
#   lista_temperatura.sort()
#   return lista_temperatura[len(lista_temperatura)-1]

# ####### Calculos: ###########




# Calculo de subida de 10 grades en menos de 10 dias.
# Si index(0) hasta index(9) subida de 5 grados
# 
# lista_prueba = ["1", "5", "3", "7", "5", "6", "1", "1", "3", "3"]
# i = 0
# for x in range(1, len(lista_prueba)-1):
#   if int(lista_prueba[i]) - int(lista_prueba[x]) >= 5:
#     print("Es mas grande que 5")
#   elif i == len(datos_raw):
#     print("Hasta aqui")
#   else:
#     print("No es mas grade que 5")
#   i+=1

# Para transfor -1 a 1, con abs(-)

# dias = 5
# lista_prueba_aux = []
# lista_prueba_aux = lista_prueba[0:5]
# z = 0
# for x in range(z,z+dias):
#   print(z,x)
#   z += dias

# for i in range(len(lista_prueba)):
#   for j in range(i+1, lista_prueba):
#     print(lista_prueba[i], lista_prueba[j])



######################################################################
######################################################################
######################################################################

# lista = [1, 4, 8, 2, 5, 7, 3, 9, 5, 1, 10, 11, 12]
# dias = 5

# for i in range(len(lista)): # Bucle principal
#   if(i%5 == 0): # Si i%5 es igual a cero, ejemplo (i(1)%5 == 0, ó, i(5)%==0)
#     if (i+5) < len(lista): # Aqui, si i(potencia de 5) es (más pequeño) que len(lista)
#       dias = i+5 # 
#     else: # Si i no es potencia de 5, es igual a len(lista)
#       dias = len(lista) 
#   for j in range(i+1, dias): # Si i=(0) pasa a i=(1), y j empieza desde 1, pero abajo podemos utilizar i, que sigue siendo (0) 
#     print(lista[i], " - ", lista[j], " = ", (abs(lista[i]-lista[j])))

######################################################################
######################################################################
######################################################################

datos_raw = ['25', '25', '25', '25', '25', '25', '25', '31', '25', '25', '25', '26', '28', '28', '45', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '10', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30']
dias_medicion = 5
cuantas_veces = ""
cuantas_veces_index = ""
diferencia_de_temp = ""

for i in range(len(datos_raw)): # Bucle principal
  if(i%5 == 0): # Si i%5 es igual a cero, ejemplo (i(1)%5 == 0, ó, i(5)%==0)
    if (i+5) < len(datos_raw): # Aqui, si i(potencia de 5) es (más pequeño) que len(lista)
      dias_medicion = i+5 # 
    else: # Si i no es potencia de 5, es igual a len(lista)
      dias_medicion = len(datos_raw) 
  for j in range(i+1, dias_medicion): # Si i=(0) pasa a i=(1), y j empieza desde 1, pero abajo podemos utilizar i, que sigue siendo (0) 
    # abs(int(datos_raw[i])-int(datos_raw[j]))
    if abs(int(datos_raw[i])-int(datos_raw[j])) > 5:
      cuantas_veces += str(datos_raw[i]) + " "
      cuantas_veces_index += str(i+1) + " "
      diferencia_de_temp += str(abs(int(datos_raw[i])-int(datos_raw[j]))) + " "

print("En el dia             ", cuantas_veces_index)
print("Hay una diferencia de ", diferencia_de_temp)
print("Temp del dia          ", cuantas_veces)

