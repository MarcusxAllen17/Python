#Author: Marcus Allen
#Assignment Number: 5
#Date: 3/30/2021
#Description: Helping a multi-national company store and analyze its sales data
    
#In this function the user inputs the country name  
def request_countryname():
    while True:
        try:
            country = input("Please enter the country's name:")
            if len(country) <= 1:
                 raise Exception 
        except Exception as err:
            print('Exception handling section, system message:', err)
            print("Country name must be at least 2 characters in length")
        else:
            break
    return country

#In this function the user inputs the sales for the county's 3 products        
def request_sales(product, country):
    while True:
        try:
            sales = float(input("Please enter the total sales for " + product
        + " in " + country +':'))
            if sales < 0:
                raise Exception 
        except Exception as err:
             print('Exception handling section, system message:', err)
             print('Sales must be numeric and positive')
        else:
            break
    return sales

#In this function a file is created that writes the countries sales data    
def request_data(file_name):
    outfile = open(file_name, 'w')
    count = 0
    loop = 'Y'
    while loop == 'Y' or loop == 'y':
        country_name = request_countryname()
        software_sales = request_sales('software', country_name)
        hardware_sales = request_sales('hardware', country_name)
        accessories_sales = request_sales('accessories', country_name)
        outfile.write(country_name + '\n')
        outfile.write(str(software_sales)+ '\n') 
        outfile.write(str(hardware_sales) + '\n')
        outfile.write(str(accessories_sales) + '\n')
        count += 1
        loop = input("Do you want to add another country? (Enter Y/y for yes\
any other key to stop):")
    print(count,"record(s) successfully added to file")
    print('-------------------------------------------')
    print('')
    outfile.close()  
    
#In this function the sales data is analyzed and printed
def analyze_data(file_name):
    count = 0
    software_sales = 0
    hardware_sales = 0
    accessories_sales = 0
    infile = open(file_name, 'r')
    line = infile.readline()
    while line != '':
        software_sales += float(infile.readline())
        hardware_sales += float(infile.readline())
        accessories_sales += float(infile.readline())
        count += 1
        line = infile.readline()
    avg_software_sales = (software_sales/count)
    avg_hardware_sales = (hardware_sales/count)
    avg_accessories_sales = (accessories_sales/count)
    total_sales = (software_sales + hardware_sales + accessories_sales)
    print('Average software sales per country: $', format(avg_software_sales,
'.2f'))
    print('Average hardware sales per country: $', format(avg_hardware_sales,
'.2f'))
    print('Average accessories sales per country: $',
          format(avg_accessories_sales,'.2f'))
    print('')
    print('Total software sales: $', format(software_sales, ',.2f'))
    print('Total hardware sales: $', format(hardware_sales, ',.2f'))
    print('Total accessories sales: $', format(accessories_sales, ',.2f'))
    print('')
    print('Total Sales:', format(total_sales, ',.2f'))
    infile.close()
  
#In this function the whole program is called and ran
def main():  
    request_data("sales_data.txt")    
    analyze_data("sales_data.txt")
main()   










