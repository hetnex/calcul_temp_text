list_node_temperature = open('temps2.txt','r').readlines() # Guardamos los datos del txt en una lista
dict_node_temperature = {}

prompt_ip_node = "Introduce la IP: "
prompt_ip_valid = "Has introducido una IP valida."
prompt_ip_options = ["1 - Ver temperatura más Alta", "2 - Ver temperatura más Baja", "3 - Ver temperatura media", "4 - Ver dias con subidas de 5 grados", "5 - Salir"] # Cuando imprimo, imprimo por la posicion de esta lista+1
prompt_node_options = "Puedes elegir las siguientes opciones: "

user_input_variable = ""

#########################################Lista to diccionari###################################################################

def list_to_dict_funct(list_of_temperatures): # Function para convertir el txt en diccionario.
    funct_variable=1

    for x in range(0, len(list_of_temperatures)-1, 2):
        dict_node_temperature[list_of_temperatures[x].rstrip()] = list_of_temperatures[funct_variable].rstrip()
        funct_variable+=2

    for x in dict_node_temperature:
        dict_node_temperature[x] = [int(x) for x in dict_node_temperature[x].split(' ')]

########################################Calculos####################################################################
# Media de las temperaturas
def average_temperature_funct(list_of_temperatures): 
    sum_temperatures = 0
    for x in list_of_temperatures: 
        sum_temperatures += x
    sum_temperatures = sum_temperatures / len(list_of_temperatures)
    return sum_temperatures

# Temperatura baja, ordenamos la lista, y sacamos la primera posicion, que es la menor de todas
def low_temperature_funct(list_of_temperatures):
  list_of_temperatures.sort()
  return list_of_temperatures[0]

# Temperatura alta, ordenamos la lista, y sacamos la ultima posicion, que es la mayor de todas
def high_temperature_funct(list_of_temperatures):
  list_of_temperatures.sort()
  return list_of_temperatures[len(list_of_temperatures)-1]

def highest_temperature_days_funct(list_of_temperatures):
    cantidad_de_item = 10 # Dias de las cuales vas a ver la diferencia de temperatura.
    lista_aux = []
    dict_de_dias_5_grados = {}
    for x in range(0, len(list_of_temperatures), cantidad_de_item): # Bucle que se encarga de coger la lista aux de solo cogemos lo que tenemos en cantidad_de_item
        lista_aux = list_of_temperatures[x:x+cantidad_de_item] # Lista donde se guarda 
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
    return dict_de_dias_5_grados # En este diccionario, key es el dia en el que esta la diferencia de temperatura, y el value es la diferencia de temperatura.
    
#############################################Llamada de funciones principales#############################################################

list_to_dict_funct(list_node_temperature) # Llamo a la funcion para que convierta el documento en diccionario

#############################################Input de usuario#############################################################

user_input_variable = str(input(prompt_ip_node))


### Comprobar si la IP esta en el diccionario ### 
def search_node_funct(bool): # Devuelve True or False
    for x in dict_node_temperature:
        if user_input_variable != x:
            return False # Podemos hacer que llame una funcion de imprimir?
        elif user_input_variable == x:
            return True  # Podemos hacer que llame una funcion


def prompt_user_funct(validacione):
    if search_node_funct(user_input_variable) == True:
        # Dado que tenemos el True de que la IP es correcta, hacemos los siguientes
        print(prompt_ip_valid)
        print("Puedes elegir las siguientes opciones: ")
        print([i for i in prompt_ip_options]) # Imprimimos las opciones

        # Dado que tenemos el True de que la IP es correcta, hacemos los siguientes
        return True
    elif search_node_funct(user_input_variable) == False:
        print("La IP que has introducido no hay datos.")
        # Dado que tenemos el False, volvamos a donde queramos
        return False


    # if numero_lista_opciones == 1:
    #     print(temperatura_alta(diccionario_nodo_temp[ip_temp]))
    # elif numero_lista_opciones == 2:
    #     print(temperatura_baja(diccionario_nodo_temp[ip_temp]))
    # elif numero_lista_opciones == 3:
    #     print(media_temperatura(diccionario_nodo_temp[ip_temp]))