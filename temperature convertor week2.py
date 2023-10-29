def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    print("Welcome to Temperature Converter")
    while True:
        try:
            temperature = float(input("Enter the temperature value: "))
            from_unit = input("From unit (C, F, K): ").upper()
            to_unit = input("To unit (C, F, K): ").upper()

            if from_unit == to_unit:
                converted_temperature = temperature
            elif from_unit == "C" and to_unit == "F":
                converted_temperature = celsius_to_fahrenheit(temperature)
            elif from_unit == "F" and to_unit == "C":
                converted_temperature = fahrenheit_to_celsius(temperature)
            elif from_unit == "C" and to_unit == "K":
                converted_temperature = celsius_to_kelvin(temperature)
            elif from_unit == "K" and to_unit == "C":
                converted_temperature = kelvin_to_celsius(temperature)
            elif from_unit == "F" and to_unit == "K":
                converted_temperature = fahrenheit_to_kelvin(temperature)
            elif from_unit == "K" and to_unit == "F":
                converted_temperature = kelvin_to_fahrenheit(temperature)
            else:
                print("Invalid units. Please use C, F, or K.")
                continue

            print(f"{temperature} {from_unit} is equal to {converted_temperature} {to_unit}")

        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")

        another_conversion = input("Do you want to convert another temperature? (yes/no): ").lower()
        if another_conversion != "yes":
            break

if __name__ == "__main__":
    temperature_converter()
