# Michael Williamson
# Conversions: Distance and Weight
# 7/23/2020

convertKiloToPounds: float = 2.20462
convertMileToKilos: float = 1.60934

while True:
    print("What do you wish to convert from?")
    print("1: Kilograms to Pounds")
    print("2: Pounds to Kilograms")
    print("3: Kilometers to Miles")
    print("4: Miles to Kilometers")
    choice = input("Pick a conversion: ")

    if int(choice) == 1:
        kilograms = input("How many kilograms? ")
        print("Pounds - " + str(float(kilograms) * convertKiloToPounds))
    elif int(choice) == 2:
        pounds = input("How many pounds? ")
        print("Kilograms - " + str(float(pounds) / convertKiloToPounds))
    elif int(choice) == 3:
        kilometers = input("How many kilometers? ")
        print("Miles - " + str(float(kilometers) / convertMileToKilos))
    elif int(choice) == 4:
        miles = input("How many miles? ")
        print("Kilometers - " + str(float(miles) * convertMileToKilos))
    else:
        print("Not a valid choice, please choose again.")
    another = input("Would you like to do another conversion? ")
    if another != "yes" and another != "Yes":
        break