### Strings ###

my_string = "Mi_string"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string  = "\\tEste es un String \\n escapado"
print(my_scape_string)

## Formateo 

name,surname, age = "Jony", "BTT", 43

print("Mi nombre es ¨{} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("Mi nombre es " + name + " " + surname + " mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

name,surname, age = "Jonathan", "BTT" , 45
print( "Mi nombre es %s %s y mi edad es %s" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")



