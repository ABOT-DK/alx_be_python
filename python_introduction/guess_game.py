import random
secret_number = random.randint(0, 100)

user_guess = int(input("Guess a number bewtween 0 and 100: "))

match user_guess:
    case  user_guess if user_guess == secret_number:
         print("Congratulations, you guessed it!")
         
             
    case user_guess if user_guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
    case user_guess if user_guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
    case _:
        print("Invalid input")


        