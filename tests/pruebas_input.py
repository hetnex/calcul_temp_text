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

# # print("Tienes que introducir una IP del cual quieres conocer su temperatura")
# # ip_temp = input()
# # print("As introducido", ip_temp)
# # print("O imprimir en pantalla todos nodos")
# diccionario_nodo_temp = {'10.167.52.198': ['25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '26', '28', '28', '28', '29', '29', '25', '25', '25', '25', '25', '25', '29', '28', '28', '28', '29', '29', '29', '29', '29', '25', '26', '26', '26', '26', '26', '26', '29', '29', '29', '28', '29', '29', '29', '29', '28', '28', '29', '27', '24', '24', '27', '27', '27', '27', '29', '28', '28', '25', '25', '25', '25', '25', '25', '25', '28', '28', '29', '28', '29', '28', '28', '26', '26', '26', '26', '26', '26', '26', '30'], '10.167.33.94': ['43', '43', '43', '43', '43', '43', '43', '44', '45', '45', '43', '43', '43', '43', '44', '44', '43', '43', '43', '43', '44', '44', '42', '43', '44', '44', '43', '45', '45', '45', '45', '42', '43', '43', '42', '42', '42', '44', '42', '43', '43', '43', '44', '44', '44', '44', '44', '43', '43', '45', '45', '44', '44', '43', '43', '43', '44', '44', '44', '44', '44', '44', '44', '45', '45', '45', '44', '44', '44', '44', '44', '44', '44', '44', '44', '44', '44', '45', '44', '44', '44', '44'], '10.167.12.162': ['35', '35', '35', '34', '34', '35', '34', '34', '34', '35', '35', '35', '35', '34', '34', '35', '34', '34', '34', '35', '35', '35', '35', '35', '34', '34', '34', '34', '35', '35', '34', '35', '34', '35', '34', '34', '34', '35', '35', '35', '34', '35', '34', '34', '35', '35', '35', '34', '34', '35', '35', '34', '35', '34', '34', '35', '34', '34', '35', '35', '34', '35', '34', '35', '34', '33', '34', '34', '33', '33', '34', '33', '34', '34', '34', '35', '35', '35', '35', '35', '34', '35']}
# lista_opciones = ["1 - Ver temp high", "2 - Ver temp low", "3 - Ver media temp"]

# ip_temp = str(input("Introduce la IP: "))

# def buscar_ip(cliente_input):
#     for x in diccionario_nodo_temp:
#         if ip_temp != x:
#             return False
#         elif ip_temp == x:
#             return True

# def ip_valida(validacione):
#     if buscar_ip(ip_temp) == True:
#         print("Has introducido una IP valida.")
#         return True
#     elif buscar_ip(ip_temp) == False:
#         print("La IP que has introducido no hay datos.")
#         return False

# if ip_valida(bool) == True:
#     print("¿Que quieres ver ahora?")
#     for x in lista_opciones:
#         print(x)

# num_option = int(input())

# def imprimicion_final(numero_lista_opciones):
#     if numero_lista_opciones == 1:
#         print(temperatura_alta(diccionario_nodo_temp[ip_temp]))
#     elif numero_lista_opciones == 2:
#         print(temperatura_baja(diccionario_nodo_temp[ip_temp]))
#     elif numero_lista_opciones == 3:
#         print(media_temperatura(diccionario_nodo_temp[ip_temp]))

# imprimicion_final(num_option)




#################################Open archivo into variable#########################################################
datos_raw = open('temps2.txt','r').readlines() # Guardamos los datos del txt en una lista
####################################################################################################################

####################################################################################################################
diccionario_nodo_temp = {} # Diccionario final
ventana_hasta = 10 # Dias en el que 
lista_opciones = ["1 - Ver temperatura más Alta", "2 - Ver temperatura más Baja", "3 - Ver temperatura media", "4 - Ver dias con subidas de 5 grados", "5 - Salir"] # Cuando imprimo, imprimo por la posicion de esta lista+1

# Metemos los datos en el diccionario, sacando los saltos de linea
###Deberia de ser una funcion###
i=1
for x in range(0, len(datos_raw)-1, 2):
    diccionario_nodo_temp[datos_raw[x].rstrip()] = datos_raw[i].rstrip()
    i+=2

# Modifico el value, para que sea una lista, con "," de separacion
###Deberia de ser una funcion###
for x in diccionario_nodo_temp:
    diccionario_nodo_temp[x] = [x for x in diccionario_nodo_temp[x].split(' ')]

####################################################################################################################


# Calculos de alarma de temp, 5 grados en 10 dias
def calculo_temp_dias(lista_grados):
    entre_dia_y_dia = []
    for i in range(0, len(lista_grados)-(ventana_hasta-1)):
        ventana = lista_grados[i:i+ventana_hasta]
        diferencia = int(ventana[0]) - int(ventana[ventana_hasta-1])
        if abs(diferencia) > 5:
            entre_dia_y_dia.append(i+1)
            entre_dia_y_dia.append(i+ventana_hasta)
    return entre_dia_y_dia

####################################################################################################################
# Input de usuario
###Deberia de ser una funcion###
ip_temp = str(input("Introduce una IP: "))

# Buscamos si la IP introducida existe en el diccionario, devuelve True-False
def buscar_ip(cliente_input):
    for x in diccionario_nodo_temp:
        if ip_temp != x:
            return False
        elif ip_temp == x:
            return True

def ip_valida(validacione):
    if buscar_ip(ip_temp) == True:
        print("Has introducido una IP valida.")
        return True
    elif buscar_ip(ip_temp) == False:
        print("La IP que has introducido no hay datos.")
        return False

####################################################################################################################
# En este if llamo a las funciones para que me devuelvan true o false, y con eso decido que hacer
# Podria utilizar una def funcion(comprovar), que dentro haya un for x in ip_valida(bool), if x == True: Que quieres hacer ahora, elif x == False: No hay esa IP que has introducido

if ip_valida(bool) == True:
    print("¿Que quieres ver ahora?")
    for x in lista_opciones: # Llamo a la lista de arriba, donde tengo ["1 - Ver temp high", "2 - Ver temp low", "3 - Ver media temp"]
        print(x)

num_option = int(input())

####################################################################################################################

def imprimicion_final(numero_lista_opciones):
    if numero_lista_opciones == 4:
        print("Los dias donde la temperatura a subido a más de 5 grados", calculo_temp_dias(diccionario_nodo_temp[ip_temp]))
    elif numero_lista_opciones == 5:
        exit()

imprimicion_final(num_option)

