customer_name = input("Enter your name: ")
purchase_amount = float(input("Enter your purchase amount: "))

standard_dicount = 0.05
premium_discount = 0.1

standard_purchase = 5000
premium_purchase = 15000

if purchase_amount >= standard_purchase and purchase_amount < premium_purchase:
    discount = purchase_amount * standard_dicount
    total_pay = purchase_amount - discount
    
    print("Hello", customer_name,'you have received Ksh.',discount,'discount!', 'Your total pay is now: Ksh.', total_pay)
    print("Thank you for shopping with us today!")
    
elif purchase_amount >= premium_purchase:
    discount = purchase_amount * premium_discount
    total_pay = purchase_amount - discount
    print("Hello", customer_name,'you have received Ksh.',discount,'discount!', 'Your total pay is now: Ksh.', total_pay)
    print("Thank you for shopping with us today!")
else:
    print("Hello", customer_name, 'Your purchase amount is below our discount program!')
    print("Your total pay is: Ksh.",purchase_amount)
    print("Terrms of the discount program: Customer must spend atleast", standard_purchase, 'to earn a standard discount of', standard_dicount, 'or spend',premium_purchase,'to earn our premium discount of', premium_discount)
    print("Thank you for shopping with us today!")