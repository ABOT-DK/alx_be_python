def employ_details():
    name = input("Enter your Name: ")
    age = int(input("Enter your age: "))
    job = input("Enter your job title")
    
    return {"name":name, "age":age, "job": job}

def salary_details():
    salary = float(input("Enter your monthly salary: "))
    months = int(input("How many months have you worked"))
    bonus_percent = float(input("Enter your performance bonus: "))
    
    return salary, months, bonus_percent

def calculate_net_income(salary,months, bonus_percent):

    total_earnings = salary *months
    bonus_amount = (bonus_percent / 100) * total_earnings
    net_income = bonus_amount + total_earnings
    
    return net_income, bonus_amount, total_earnings
    
def classify_earner(net_income):
    
    if net_income >= 1000000:
        return "High Earner"
    elif net_income > 500000 and net_income < 1000000:
        return "Average income earner"
    
    else:
        return "Low income Earner"
    
def expenses():
    expenses =[]
    
    for i in range(3):
        expenses_name = input(f"Expense {i +1}  name: ")
        expenses_amount = float(input(f" Amount for {expenses_name} : "))
        expenses.append({"expenses_name": expenses_name, "expenses_amount":expenses_amount})
        
      
        
        return expenses, expenses_amount, expenses_name
    

    
    