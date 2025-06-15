def greet(name):
    
    print(f"Good morning {name}")
    
greet(name="Gucha")


def area_of_rectangle(length, width):
    area = length * width
    return area
    

length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))

result =(area_of_rectangle(length=length, width=width))

print(f"The area of the rectangle with length {length} and widht {width} is : {result}")



def odd_or_even(number):
    if number % 2 == 0:
        print(f"The number {number} is an even number")
    else:
         print(f"The number {number} is an odd number")
         
number_tested= int(input("Enter number to check whether it is odd or even: "))
print =(odd_or_even(number=number_tested))