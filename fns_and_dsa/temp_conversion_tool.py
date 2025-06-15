FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def user_input():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    return temperature, unit

def convert_to_celsius():
    temperature, unit = user_input()
    
    if unit == "F":
        celcius = (temperature - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
        return f"{temperature}°F is {celcius}°C"
        
    else:
        print("The temperature is already in Celcius")
        
    
        
    
def convert_to_fahrenheit():
    temperature, unit = user_input()
    
    if unit == "C":
        fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return f"{temperature}°C is {fahrenheit}°F"
        
    else:
        print("The temperature is already in Fahrenheit")
        
        
fahrenheit = convert_to_fahrenheit()
print(fahrenheit)

celsius = convert_to_celsius()
print(celsius)
        
        
        
    
        
  
        
        