#Global Variables
data = []
threeDlist = []
week = 1


#Here the stock prices from the file are put into a list
def read(infile):
    file = open(infile, 'r')
    for line in file:
        data.append(float(line.rstrip('\n')))
    file.close()
    

#Here the user inputs the start week for the analysis
def start_week():
    try:
        start = int(input('Please enter the start week:') or '1')
        if start < 1 or start > 52:
            raise Exception
    except Exception as err:
        print(err, 'Input must be between 1 and 52, inclusive')
        start = int(input('Please enter the start week:'))
    return start

#Here the user inputs the end week for the analysis
def end_week():
    try:
        end = int(input('Please enter the end week:') or '52')
        if end < 1 or end > 52:
            raise Exception
    except Exception as err:
        print(err, 'Input must be between 1 and 52, inclusive')
        end = int(input('Please enter the end week:'))
    return end

# Here the change in stock price from week to week is calculated              
def nested_list():
    initial_3dlist = [format(data[0], '.2f'), 0, 1]
    threeDlist.append(initial_3dlist)
    for i in range(1,52):
        week = i +1
        temp_threeDlist = [format(data[i], '.2f'), format(data[i] - data[i-1],
                                                          '.2f'), week]
        threeDlist.append(temp_threeDlist)
    #print(threeDlist)    
 
#Here the max, min, and average change in stock prices is found and displayed
def calculate_trends(a,b):
    new_list = []
    for i in range(a-1,b):
        new_list.append(float(threeDlist[i][1]))
    max_change = (max(new_list))
    min_change = (min(new_list))
    avg_change = (format(sum(new_list)/((b-(a-1))),'.2f'))
    max_change_wk = new_list.index(max_change) + a 
    min_change_wk = new_list.index(min_change) + a 
    print('The average change is ', str(avg_change), sep='')
    print('The week with the highest growth is week '+ str(max_change_wk) +
          ' with a change of '+ str(max_change))
    print('The week with the lowest growth is week '+ str(min_change_wk) +
          ' with a change of '+ str(min_change))
    #print(new_list)
  
#This is the function that brings the whole program together
def main():
    read('ApplePrices.txt')
    start = start_week()
    end = end_week()
    nested_list()
    calculate_trends(start, end)

main()
      