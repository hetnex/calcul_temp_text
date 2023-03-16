# square_dict = {num: num*num for num in range(1, 11)}
# print(square_dict)

# funct_variable=1

# for x in range(0, len(txt_to_list_node)-1, 2):
#     dict_node_temperature[txt_to_list_node[x].rstrip()] = txt_to_list_node[funct_variable].rstrip()
#     funct_variable+=2
prompt_ip_options = ["1 - Ver temperatura más Alta", "2 - Ver temperatura más Baja", "3 - Ver temperatura media", "4 - Ver dias con subidas de 5 grados", "5 - Salir"] # Cuando imprimo, imprimo por la posicion de esta lista+1
prompt_ip_valid = "Has introducido una IP valida."
prompt_node_options = "Puedes elegir las siguientes opciones: "

print("\n", prompt_ip_valid, "\n", prompt_node_options)
[print(i) for i in prompt_ip_options]


# for x in prompt_ip_options: # Llamo a la lista de arriba, donde tengo ["1 - Ver temp high", "2 - Ver temp low", "3 - Ver media temp"]
#     print(x)