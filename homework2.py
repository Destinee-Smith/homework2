# 1. Kilometers to Smoots
def kilometers_to_smoots():
    kilometers = float(input("Enter distance in kilometers: "))
    meters = kilometers * 1000
    smoots = meters / 1.70
    print("Distance in smoots:", smoots)


# 2. Centimeters to Mickeys
def centimeters_to_mickeys():
    centimeters = float(input("Enter distance in centimeters: "))
    millimeters = centimeters * 10
    mickeys = millimeters * 16
    print("Distance in mickeys:", mickeys)


# 3. X followers to Wheatons
def followers_to_wheatons():
    followers = float(input("Enter number of X followers: "))
    wheatons = followers / 500000
    print("Followers in Wheatons:", wheatons)


# 4. Celsius to Kelvin
def celsius_to_kelvin():
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)


# 5. Fahrenheit to Kelvin
def fahrenheit_to_kelvin():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)
