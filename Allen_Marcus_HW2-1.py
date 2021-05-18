#Author: Marcus Allen
#Homework Number and Name: HW 2, Audiobooks Subsidiary 
#Due Date: 2/11/2021
#Program Description: program that accepts information from the user and calculates the price of the books sold

#Here are the input values
price = 9.98
free_books = 0
customer_type = 'Regular'
membership_fee = 0
name = input("What is your name?")
books = int(input("What is the number of books you purchased?"))
membership = input("What type of member are you? R for Regular; P for premium.")
upgrade = 'N'
#Here are my if statements 
if membership == 'R':
    upgrade = input("Would you like to become a member? Y for yes and N for no.")
elif membership == 'P':
    price = 8.54
    customer_type = 'Premium'
if membership == 'P' and books > 5:
    free_books = 1
elif membership =='P' and books > 9:
    free_books = 2

if upgrade == 'Y':
    print("\nYour membership fee is $5.30")
    price = 8.54
    customer_type = 'Premium'
    membership_fee = 5.30    
if upgrade == 'Y' and books > 5:
    free_books = 1
elif upgrade =='Y' and books > 9:
    free_books = 2
elif upgrade == 'N' and books > 7:
    free_books = 1
elif upgrade =='N' and books > 12:
    free_books = 2

#Here are my calculations
  
#This is how much the customer owes before the sales tax
pre_tax = price*(books-free_books)+ membership_fee
#This is the constant sales tax rate
sales_tax_rate= .0825
#This is the sales tax total
sales_tax_total = sales_tax_rate*pre_tax
#This is how much the customer owes after the sales tax is added
total = sales_tax_total+pre_tax
   
#Here are the outputs
print("\nCustomer name:", name)
print("Type of Customer:", customer_type)
print("Total number of books recieved:", books)
print("Price of books before sales tax: $", format(pre_tax,'.2f'),sep ="")
print("Sales tax: $", format(sales_tax_total, '.2f'),sep ="")
print( "Total Amount Due: $", format(total, '.2f'),sep ="")

if upgrade == 'Y':
    print("Thank you for upgrading to premium membership!")
elif membership == 'P':
    print("Your membership is helping you save.")

























