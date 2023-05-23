def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def feet_to_meters(feet):
    meters = feet * 0.3048
    return meters

def meters_to_feet(meters):
    feet = meters / 0.3048
    return feet

def lbs_to_kg(lbs):
    kg = lbs * 0.453592
    return kg

def kg_to_lbs(kg):
    lbs = kg / 0.453592
    return lbs

print("Welcome to the Unit Converter!")

while True:
    print("\nSelect the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Feet to Meters")
    print("4. Meters to Feet")
    print("5. Pounds (lbs) to Kilograms (kg)")
    print("6. Kilograms (kg) to Pounds (lbs)")
    print("0. Exit")

    choice = input("Enter your choice (0-6): ")

    if choice == "0":
        print("Thank you for using the Unit Converter!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please try again.")
        continue

    value = float(input("Enter the value to be converted: "))

    if choice == "1":
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C is equal to {result}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F is equal to {result}°C")
    elif choice == "3":
        result = feet_to_meters(value)
        print(f"{value} ft is equal to {result} m")
    elif choice == "4":
        result = meters_to_feet(value)
        print(f"{value} m is equal to {result} ft")
    elif choice == "5":
        result = lbs_to_kg(value)
        print(f"{value} lbs is equal to {result} kg")
    elif choice == "6":
        result = kg_to_lbs(value)
        print(f"{value} kg is equal to {result} lbs")
