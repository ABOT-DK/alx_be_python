value = input("Enter a value (number or string): ")

match value:
    case int():
        print("The value you have entered an integer: ",value)
    case str():
        print("The value entered is a string: ", value)
    case _:
        print("Invalid data type entered.")