monthly_income = int(input("Enter your monthly income:"))
totalexpenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - totalexpenses
savingrate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * savingrate)


print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is:  {projected_savings}")