#Author: Marcus Allen
#Homework Number and Name: HW 1, Taco Sales
#Due Date: 2/4/2021
#Program Description: application to record the sales and calculate profit for tacos sold

#Here the user will input the data pertaining to the specific item and its cost, price, and quantity
Item = input("What is the name of the item being sold?")
Price = float(input("What is the price of the item being sold?"))
Cost = float(input("What is the cost of the item being sold?"))
Quantity = float(input("How many of the items were sold?"))
#Here the functions that are used to manipulate the input data into outputs are displayed 
#These functions include finding the total cost, total revenue, total profit, and percent revenue of a taco
Revenue = Quantity*Price
Total_Cost = Cost*Quantity
Total_Profit = Revenue - Total_Cost
Percent_Profit = (Total_Profit/Revenue)*100
#Here the print statements that display the output data is shown
print("Item Name: ",Item,sep="")
print("Total Revenue: $",format(Revenue,'.2f'),sep="")
print("Total Cost: $",format(Total_Cost, '.2f'),sep="")
print("Quantity Sold: ",Quantity)
print("Total_Profit: $", format(Total_Profit,'.2f'),sep="")
print("Percent Profit: ",format(Percent_Profit,'.0f'),'%', sep="")