import re

# Mas alta,
# Mas baja,
# Media de todas temperaturas,
# Indicación de la subida de 5 grados en 10 dias, cada temp es de 1 dia

# Promtp de que quieres ver de las opciones anteriores


# Abrimos el archivo, y metemos todas las temperaturas en una lista
datos_raw = open('temps2.txt').readlines()

diccionario = {}
diccionario_aux = {}
i = 0

# Incluyo datos_raw al diccionario, siendo key la ip, y temp el value
for x in range(1, len(datos_raw)-1,2):
    diccionario[datos_raw[i]] = datos_raw[x]
    i+=2


# Modifico el value, para que sea una lista, con "," de separacion
for x in diccionario:
    diccionario_aux[x] = [x for x in diccionario[x].split(' ')]


# Quito el salto de linea de las listas de temps
for x in diccionario_aux:
    diccionario_aux[x.remove("\n")].remove("\n")

print(diccionario_aux)


####### Calculos: ###########

# Suma de las temperaturas
def suma_temperatura(la_suma_temp):
    total = 0
    for temps in la_suma_temp: 
        total += temps
    return total

# Media de las temperaturas
def media_temperatura(la_media_temp):
  suma_temp = suma_temperatura(la_media_temp)
  average = suma_temp / len(la_media_temp)
  return average

# Temperatura baja, ordenamos la lista, y sacamos la primera posicion, que es la menor de todas
def temperatura_baja(lista_temperatura):
  lista_temperatura.sort()
  return lista_temperatura[0]

# Temperatura alta, ordenamos la lista, y sacamos la ultima posicion, que es la mayor de todas
def temperatura_alta(lista_temperatura):
  lista_temperatura.sort()
  return lista_temperatura[len(lista_temperatura)-1]



