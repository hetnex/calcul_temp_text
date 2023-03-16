####################################Reading txt and creating dicctionary####################################

list_node_temperature = open('out.txt','r').readlines() # Saving the .txt, where de IPs and temperatures dates into a list
dict_node_temperature = {}                              # Dictionary where we save the IPs as key, and the temps datas as a value
dict_ip_diff_temperature = {}

#########################################User prompt variables##############################################

prompt_banner = open("banner.txt", "r")
prompt_ip_node = "Introduce la IP del equipo:"
prompt_ip_valid = "La IP que has introducido es correcta."
prompt_ip_options = ["1 - Ver temperatura más Alta", "2 - Ver temperatura más Baja", "3 - Ver temperatura media", "4 - Ver diferencia de temperaturas", "5 - Introducir otra IP", "6 - Salir"] # Cuando imprimo, imprimo por la posicion de esta lista+1
prompt_ip_invalid = "No tenemos datos de la IP que has introducido. O no has introducido una IP valida."
prompt_node_options = "Puedes elegir las siguientes opciones:"
prompt_user_options = "Introduce una opcion:"
prompt_exit_option = "Hasta luego"
prompt_none_value = "No hay datos de temperatura en esta IP"
prompt_range_of_days = "Introduce el rango de los dias:"
prompt_temperature_difference = "Introduce la diferencia de temperatura:"
prompt_line_break = "\n"
prompt_welcome_user = "Bienvenido al programa de calculo de temperaturas."
promt_option_oneip_allip = ["1 - Hacer el calculo sobre todas las IPs.", "2 - Hacer el calculo sobre IPs especificas.", "3 - Salir del programa."]


#########################################User input variables##############################################

user_input_range_days = 0 # Range of days to calculate
user_input_temperature_difference = 0 # Temperature calculations
user_input_variable_ip = "" # Variable where user input the IP

#########################################Function list to dict##############################################

def valid_ip_funct(ip_validate): # Function return True or False, if ip_validate is a valid IP
    return ip_validate.count('.') == 3 and all(0<=int(num)<256 for num in ip_validate.rstrip().split('.'))

def list_to_dict_funct(): # Function convert a list of IP and temps, into a dictionary, the key of the dict is the IP, the value is the temperatures
    in_funct_rising_num = 0

    for each_item_list in list_node_temperature:
        list_node_temperature[in_funct_rising_num] = each_item_list.rstrip()
        if valid_ip_funct(list_node_temperature[in_funct_rising_num]) == True:
            if list_node_temperature[in_funct_rising_num+1] == prompt_line_break:
                dict_node_temperature[list_node_temperature[in_funct_rising_num]] = None
            else:
                dict_node_temperature[list_node_temperature[in_funct_rising_num]] = list_node_temperature[in_funct_rising_num+1].rstrip()
        in_funct_rising_num+=1
    for each_key_dict in dict_node_temperature:
        if dict_node_temperature[each_key_dict] == None:
            pass
        else:
            dict_node_temperature[each_key_dict] = [int(each_key_dict) for each_key_dict in dict_node_temperature[each_key_dict].split()]

list_to_dict_funct() # Starting function list to excel

########################################Temperature calculations##############################################################
# Calculating average temperature 
def average_temperature_funct(in_funct_list_of_temperature): 
    in_funct_calc_temperatures = 0
    if in_funct_list_of_temperature == None: # When the IP has no temperature data, the dictionary value is None.
        return prompt_none_value
    else:
        for each_item_list in in_funct_list_of_temperature: # Itera on the list, add up each temperature and divide by the size of the list.
            in_funct_calc_temperatures+=each_item_list
        in_funct_calc_temperatures = in_funct_calc_temperatures / len(in_funct_list_of_temperature)
        return round(in_funct_calc_temperatures, 1)  # Return rounded number

# Calculating lowest temperature
def low_temperature_funct(in_funct_list_of_temperature):
    if in_funct_list_of_temperature == None: # This if is for when the IP has no temperature data, the dictionary value is None.
        return prompt_none_value
    else:
        in_funct_list_of_temperature.sort() # Sort the list, return the first position
        return in_funct_list_of_temperature[0]

# Calculating highest temperature
def high_temperature_funct(in_funct_list_of_temperature):
    if in_funct_list_of_temperature == None: # This if is for when the IP has no temperature data, the dictionary value is None.
        return prompt_none_value
    else:
        in_funct_list_of_temperature.sort() # Sort the list, return the last position
        return in_funct_list_of_temperature[len(in_funct_list_of_temperature)-1]

# Calculating, on a range of days, the change in temperature
def highest_temperature_days_funct(in_funct_list_of_temperature):
    in_funct_list_aux = []
    in_funct_dict = {}
    if in_funct_list_of_temperature == None: # This if is for when the IP has no temperature data, the dictionary value is None.
        return None
    else:
        for each_range_of_days in range(0, len(in_funct_list_of_temperature), user_input_range_days): # Loop in a range of days
            in_funct_list_aux = in_funct_list_of_temperature[each_range_of_days:each_range_of_days+user_input_range_days] # Creating a list, including only the user_input_range_days.
            in_loop_rising_num = 0
            in_funct_temperature_difference = 0
            
            for each_item_list in in_funct_list_aux: # Iterate on the list, where we only have user_input_range_days temperature.
                in_loop_rising_num+=1 
                if in_loop_rising_num >= len(in_funct_list_aux): # To stop the loop when you reach the end of the list
                    break
                in_funct_temperature_difference = each_item_list - in_funct_list_aux[in_loop_rising_num] # I save the temperature difference between the [i] position of the list item and the [z] position of list item.
                # print(in_funct_temperature_difference)
                if in_funct_temperature_difference <= user_input_temperature_difference: # If we get to the temperature difference
                    in_funct_dict[each_range_of_days+in_loop_rising_num+1] = in_funct_temperature_difference # I save into a dict, the key (day of the temperature difference), the value (the total of the temperature difference)
                    # Can be printed ("Hay una diferencia de 5 grados. Entre los dias", each_range_of_days+1, each_range_of_days+user_input_range_days, "Es decir, el dia", each_range_of_days+z+1)
                    break
        return in_funct_dict # Return a dictionary, where key is the day, value is the temperature difference


def count_dict_ip(in_funct_dict): # Function that counts how many IPs is in the dict_ip_diff_temperature, to prompt to the user
    num_rising_loop=0
    for each_key_dict in in_funct_dict: # The values of the dict have 3 different types of data
        if in_funct_dict[each_key_dict] == None: # This means that this IP has no temperatures values
            pass
        elif in_funct_dict[each_key_dict] == {}: # This means that this IP do not have the difference of temperature
            pass
        else: # The only one who has data
            num_rising_loop+=1
    return num_rising_loop

def list_ip_prompt_print(in_funct_dict): # Return a list of the IPs inside of the dict_ip_diff_temperature, to prompt to the user
    in_funct_list = []
    for each_key_dict in in_funct_dict:
        if in_funct_dict[each_key_dict] == None:
            pass
        elif in_funct_dict[each_key_dict] == {}:
            pass
        else:
            in_funct_list.append(each_key_dict)
    return in_funct_list

#############################################User input##########################################################

### Check if the user_input_variable_ip is in the dict_node_temperature ### 
def search_node_funct(user_input_variable_ip): # If the IP it is the dictionary True, If is not False
    in_funct_user_ip = False
    for each_key_dict in dict_node_temperature:
        if user_input_variable_ip == each_key_dict:
            in_funct_user_ip = True
            break

    return in_funct_user_ip

def prompt_user_option_funct(user_input_option): # Each IF return the result of the calculation and prompt
    global user_input_variable_ip # Use global, python need this, so we can use those variables 
    global user_input_range_days
    global user_input_temperature_difference
    print(user_input_variable_ip)
    in_funct_days = ""
    
    if user_input_option == "1":
        print("Esta es la temperatura más alta:", high_temperature_funct(dict_node_temperature[user_input_variable_ip]), prompt_line_break)
    elif user_input_option == "2":
        print("Esta es la temperatura más baja:", low_temperature_funct(dict_node_temperature[user_input_variable_ip]), prompt_line_break) 
    elif user_input_option == "3":
        print("Esta es la temperatura media:", average_temperature_funct(dict_node_temperature[user_input_variable_ip]), prompt_line_break) 
    elif user_input_option == "4":
        print(user_input_variable_ip)
        user_input_range_days = int(input(prompt_range_of_days))
        user_input_temperature_difference = int(input(prompt_temperature_difference))
        user_input_temperature_difference = -user_input_temperature_difference
        if len(highest_temperature_days_funct(dict_node_temperature[user_input_variable_ip])) == 0:
            print("En", user_input_range_days, "dias, no hay una diferencia de", abs(user_input_temperature_difference), "grados.", prompt_line_break)
        else:
            for each_key_dict in highest_temperature_days_funct(dict_node_temperature[user_input_variable_ip]):
	            in_funct_days += str(each_key_dict) + ", "
            print("En los dias", in_funct_days, "hay una diferencia de mas de", abs(user_input_temperature_difference), "grados.", prompt_line_break) 
    elif user_input_option == "5":
        user_input_variable_ip = str(input(prompt_ip_node)) # User input the IP
        
    elif user_input_option == "6":
        exit(prompt_exit_option)
    else:
        print("Has elegido una opcion incorrecta")

def prompt_user_funct(): # Main function
    global user_input_variable_ip
    global user_input_option
    global user_input_range_days
    global user_input_temperature_difference
    in_funct_user_input = ""

    print("He registrado", len(dict_node_temperature), "IPs dentro del archivo out.txt", prompt_line_break)
    print(prompt_node_options, prompt_line_break)
    print(*(x for x in promt_option_oneip_allip), sep=prompt_line_break)
    user_input_option = input(prompt_user_options)
    

    if user_input_option == "1": # All IP address!
        while True: # Loop the prompt part of the code
            
            user_input_range_days = int(input(prompt_range_of_days))
            user_input_temperature_difference = int(input(prompt_temperature_difference))
            user_input_temperature_difference = -user_input_temperature_difference
            for each_key_dict in dict_node_temperature: 
                dict_ip_diff_temperature[each_key_dict] = highest_temperature_days_funct(dict_node_temperature[each_key_dict])
            print("En el rango", user_input_range_days, "dias, se ha registrado un total de", count_dict_ip(dict_ip_diff_temperature), "IPs, con una diferencia de temperatura de mas de", abs(user_input_temperature_difference), "grados.")
            in_funct_user_input = input("¿Quieres ver en pantalla las IPs?(Si o No): ")
            if in_funct_user_input == "Si":
                print(*(x for x in list_ip_prompt_print(dict_ip_diff_temperature)), sep=prompt_line_break)
                print("Volviendo al menu principal", prompt_line_break, prompt_line_break)
                prompt_user_funct()
            elif in_funct_user_input == "No":
                print("De acuerdo. Volviendo a la pantalla principal", prompt_line_break, prompt_line_break)
                prompt_user_funct()
            
    elif user_input_option == "2": # Specific IP address!
        user_input_variable_ip = str(input(prompt_ip_node)) # User input the IP
        print(user_input_variable_ip)
        while True: # Loop the prompt part of the code
            if search_node_funct(user_input_variable_ip) == True: # The IP enter is in the dict_node_temperature
                print(prompt_ip_valid, prompt_node_options, prompt_line_break)
                print(*(x for x in prompt_ip_options), sep=prompt_line_break) # Comprenhension of the list prompt_ip_options
                user_input_option = input(prompt_user_options)
                prompt_user_option_funct(user_input_option)
            
            elif user_input_variable_ip == "exit":
                exit("Hasta luego")

            elif search_node_funct(user_input_variable_ip) == False:
                print(prompt_ip_invalid)
                user_input_variable_ip = str(input(prompt_ip_node)) # User input the IP

    elif user_input_option == "3":
        exit(prompt_exit_option)

    else:
        print("Has introducido una opcion no valida. Elige 1 o 2.", prompt_line_break, prompt_line_break, prompt_line_break, prompt_line_break)
        prompt_user_funct()
               

#############################################Starting the prompt part of the script##########################################################

print(prompt_banner.read()) # Initiate the banner
print(prompt_welcome_user, prompt_line_break)
prompt_user_funct() # Initiate the script
