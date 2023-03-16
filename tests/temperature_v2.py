import re
# Abrimos el archivo, y metemos todas las temperaturas en una lista
# datos_raw = open('temps2.txt').read()
# lista_numero_temperatura = [int(x) for x in datos_raw.split('\n')]


datos_raw = open('temps2.txt').readlines()
diccionario = {}
i = 0
for x in range(1, len(datos_raw)-1,2):
    diccionario[datos_raw[i]] = datos_raw[x]
    i+=2

print(diccionario)
# for x in lista_numero_temperatura:
#     if x == ("\d")



