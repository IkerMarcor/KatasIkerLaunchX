###### Manejo de errores ######
## Tracebacks ##
open("/path/to/mars.jpg")

## Try y Except de los bloques ##
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()

## Situaciones en errores genericos ##
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)

# Salida: got a problem trying to read the file: [Errno 2] No such file or directory: 'mars.jpg'

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")

# Dependiendio en numero de error que se genere imprimira el mesaje correspondiente.

## Caso de Astronautas ##
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left(5, 100, 2)
# Salida: 'Total water left after 2 days is: -10 liters'

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left(5, 100, 2)
#Salida:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in water_left
# RuntimeError: There is not enough water for 5 astronauts after 2 days!

try:
    water_left(5, 100, None)
except RuntimeError as err:
    print(err)
#Salida:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in water_left
# TypeError: can't multiply sequence by non-int of type 'NoneType'

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left("3", "200", None)

# Salida:
# Traceback (most recent call last):
#   File "<stdin>", line 5, in water_left
# TypeError: unsupported operand type(s) for /: 'str' and 'int'