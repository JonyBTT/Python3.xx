# Variables 

my_String_variable = "My String variable"
print(my_String_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable =str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de varibables en un print 

print(my_String_variable,my_int_to_str_variable,my_bool_variable)

print("Este es el valor de:",  my_bool_variable)
# Algunas Funciones  del sistema

print(len(my_String_variable))

# Variables en una sola linea   ¡Cuidado con abusar con esta sintaxis! 

name, surname, alias, age ="Jony","jou","JonyBTT" ,43

print("Me llamo:",name, surname, ". Mi edad es:", age, ". Y mi Alias es:" ,alias)

# Inputs 

name = input ('¿Cual es tu nombre? ')
age = input('¿Cuantos años tienes? ')

print(name)
print(age)


# Cambiamos su tipo

name = 35
age = "Brais"

print(name)
print(age)

# ¿Forzamos el tipo???

address: str = "Mi direccion"
address =  True
address = 5
address = 1.2
print(type(address))