#Author: Marcus Allen
#Homework Number and Name: HW 3, Retirement Account
#Due Date: 2/22/2021
#Program Description: program that helps users compute retirement information

# annual savings amount for the account
annual_savings = input("What is your annual savings amount?")
while annual_savings == '':
    print("annual savings cannot be blank")
    annual_savings = input("What is your annual savings amount?")
annual_savings = float(annual_savings)
while annual_savings <= 0:
    print("annual savings amount must be a positive number")
    annual_savings = float(input("What is your annual savings amount?"))
# start year for the retirement account
start_year = input("What year do you want to start saving?")
while start_year == '':
    print("start year cannot be blank")
    start_year = input("What year do you want to start saving?")
start_year = int(start_year)
while start_year < 2021 or start_year > 2050:
    print("start year must be between 2021 and 2050, inclusive.")
    start_year = int(input("What year do you want to start saving?"))
# year that saving will cease
end_year = input("What year do you want to stop saving?")
while end_year == '':
    print("end year cannot be blank")
    end_year = input("What year do you want to stop saving?")
end_year = int(end_year)
while end_year < 2021 or end_year > 2100 or end_year < start_year:
    print("end year must be between 2021 and 2100.")
    end_year = int(input("What year do you want to stop saving?"))
# year the individual will retire
retirement_year = input("what year do you want to retire?")
while retirement_year == '':
    print("Retirement year cannot be blank")
    retirement_year = input("what year do you want to retire?")
retirement_year = int(retirement_year)
while retirement_year < 2021 or retirement_year > 2100 or retirement_year < end_year:
    print('retirement must be greater than or equal to end year and between 2021 and 2100, and cannot be blank')
    retirement_year = int(input("what year do you want to retire?"))
# interest rate for the account
interest = float(input("what is the interest rate?"))
while interest < .05 or interest > .15 :
    print('Interest rate must be between .05 and .15 inclusively.')
    interest = float(input("what is the interest rate?"))

print("Year",format("Savings",'>15s'),format("Interest",'>15s'),format("Total",'>15s'))
print("-----------------------------------------------------------------------")

# Here are the calculations
additional_savings = annual_savings
interest_earned = additional_savings*interest
total_savings = additional_savings + interest_earned

# Here is the for loop
for current_year in range(start_year, retirement_year+1):
    print(current_year,format(additional_savings,'15,.0f'), format(interest_earned,'15,.0f') , format(total_savings, '15,.0f'))
    if current_year <= end_year-1:
        additional_savings = annual_savings
    else:
        additional_savings = 0
    interest_earned = (total_savings+additional_savings)*interest
    total_savings += additional_savings + interest_earned
    
        

    
    

        




















