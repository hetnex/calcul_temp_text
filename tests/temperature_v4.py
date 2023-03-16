v_bienvenido = "Buenas, bienvenido al programa de Papo, para calcular temperaturas.\nTienes que introducir una IP del cual quieres conocer su temperatura."

datos_raw = open('temps.txt','r').readlines() # Guardamos los datos del txt en una lista
diccionario_nodo_temp = {} # Creamos un diccionario, donde guardaremos los datos
# Creamos un loop, donde guardamos la key(IP) junto al value(datos temps)
# Tambien borramos los saltos de linea

i=1
for x in range(0, len(datos_raw)-1, 2):
    diccionario_nodo_temp[datos_raw[x].rstrip()] = datos_raw[i].rstrip()
    i+=2

# Modifico el value, para que sea una lista, con "," de separacion
for x in diccionario_nodo_temp:
    diccionario_nodo_temp[x] = [x for x in diccionario_nodo_temp[x].split(' ')]

####### Calculos: ###########

# Suma de las temperaturas
def suma_temperatura(la_suma_temp):
    total = 0
    for temps in la_suma_temp: 
        total += int(temps)
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

# Funcion imprimir
def imprimir_pantalla(a_imprimir):
  print(a_imprimir)

imprimir_pantalla(v_bienvenido)
ip_temp = str(input("Introduce la IP"))



