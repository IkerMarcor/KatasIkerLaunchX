# Un programa python
sum = 1 + 2
print(sum)

# Funcion print()
print("Hola desde la consola")

# Variables
sum = 1 + 2       # sum vale 3
product = sum * 2 # pruduct vale 6
print(product)

# Tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri)) 

# Operadores
left_side = 10
right_side = 5
left_side / right_side # 2

# Operadores aritmeticos
op_suma = 1 + 1
op_resta = 1 - 2
op_division = 10 / 2
op_multiplicacion = 2 * 2

# Operadores de asignacion
x = 2  # x ahora contiene 2
x += 2 # x ahora contiene 4
x -= 2 # x ahora contiene 2
x /= 2 # x ahora contiene 1
x *= 2 # x ahora contiene 2

# Fechas
from datetime import date

print(date.today())
print("Today's date is: " + str(date.today()))

# Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Trabajar con numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(float(first_number) + float(second_number))

