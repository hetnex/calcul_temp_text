# datos_string = ""
# with open('temps1.txt', 'r') as file:
#     datos_string = file.read()

# print(datos_string)

#str = open('temps1.txt', 'r').read()

# with open('temps1.txt') as f:
#   s = " ".join([x.strip() for x in f]) 

# Este parece el mas comodo


# Abrimos el archivo, y metemos todas las temperaturas en una lista
datos_raw = open('temps1.txt').read()
lista_numero_temperatura = [int(x) for x in datos_raw.split(' ')]


# Calculos:

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


