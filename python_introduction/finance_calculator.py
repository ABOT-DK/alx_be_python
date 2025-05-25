monthlyincome = int(input("Enter your monthly income:"))
totalexpenses = int(input("Enter your total monthly expenses:"))
monthlysavings = monthlyincome - totalexpenses
savingrate = 0.05

projected_savings = monthlysavings * 12 + (monthlysavings * 12 * savingrate)


print(f"Your monthly savings are {monthlysavings}")
print(f"Projected savings after one year, with interest, is:  {projected_savings}")