day = input("Enter the day of the week: ").lower()

match day:
    case "monday":
        print("Ugh, Mondays....")
    case "tuesday":
        print("Just another workday...")
        
    case "wednesday":
        print("Hump day!")
        
    case "thursday":
        print("Almost there....")
        
    case ("friday"):
        print("TGIF!")
    case "saturday" | "sunday":
        print("weekend vibes")
    case _:
        print("Invalid day entered.")
            