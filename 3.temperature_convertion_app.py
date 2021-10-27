print("Welcome to the Temperature Conversion App")


def show_table(celsius, fahrenheit, kelvin):
    print(f"\nDegrees Celsius: {round(celsius, 2)}°C")
    print(f"Degrees Fahrenheit: {round(fahrenheit, 2)}°F")
    print(f"Degrees Kelvin: {round(kelvin, 2)}°K")

# menu
while True:
    print("\nMenú de selección de conversión")
    print("1. Fahrenheit to Celsius/Kelvin")
    print("2. Celsius to Fahrenheit/Kelvin")
    print("3. Kelvin to Celsius/Fahrenheit")
    print("4. Quit the program")
    selection = int(
        input("\nIntroduzca un número de acuerdo a la acción que desea ejecutar: "))

    if selection == 1:
        try:
            fahrenheit = float(
                input("\nWhat is the given temperature in degrees Fahrenheit: "))
        except ValueError:
            print(
                "Los valores ingresados son incorrectos, debe ingresar solo digitos numéricos.")
            continue
        # Formular de fahrenheit to celsius
        celsius = (fahrenheit - 32) * 5/9
        # Formular de fahrenheit to kelvin
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        show_table(celsius, fahrenheit, kelvin)
        break
    if selection == 2:
        try:
            celsius = float(
                input("\nWhat is the given temperature in degrees Celsius: "))
        except ValueError:
            print(
                "Los valores ingresados son incorrectos, debe ingresar solo digitos numéricos.")
            continue
        # Formular de celsius to fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        # Formular de celsius to kelvin
        kelvin = celsius + 273.15
        show_table(celsius, fahrenheit, kelvin)
        break
    if selection == 3:
        try:
            kelvin = float(
                input("\nWhat is the given temperature in degrees Kelvin: "))
        except ValueError:
            print(
                "Los valores ingresados son incorrectos, debe ingresar solo digitos numéricos.")
            continue
        # Formular de kelvin to celsius
        celsius = kelvin - 273.15
        # Formular de kelvin to fahrenheit
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        show_table(celsius, fahrenheit, kelvin)
        break
    if selection == 4:
        break
    else:
        print(selection)
        print("You most choose a option in the menu")
