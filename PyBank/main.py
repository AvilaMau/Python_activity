# Create a Python script to analyze the financial records of your company based on the financial dataset called budget_data.csv. which is composed of two columns: "Date" and "Profit/Losses".

# Create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import csv


monthtotal = 0
amounttotal = 0
previousprofit = 0
profitchange = 0
profitchangetotal = 0
monthlyprofitchange = 0
greatestincrease = 0
greatestincreasemonth = ""
greatestdecrease = 0
greatestdecreasemonth = ""

with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    
    for row in csv_reader:
        monthtotal = monthtotal + 1
        amounttotal = amounttotal + int(row[1])

        currentprofit = int(row[1])

        if previousprofit != 0:
            profitchange = currentprofit - previousprofit
            profitchangetotal = profitchangetotal + profitchange 
            monthlyprofitchange = monthlyprofitchange + 1
            

        previousprofit = currentprofit    


        if profitchange > greatestincrease:
            greatestincrease = profitchange
            greatestincreasemonth = row[0]

        if profitchange < greatestdecrease:
            greatestdecrease = profitchange
            greatestdecreasemonth = row[0]

print(greatestdecreasemonth)

output = f"""
Financial Analysis
----------------------------
Total Months: {monthtotal}
Total: ${amounttotal}
Average Change: ${profitchangetotal/monthlyprofitchange:.2f}
Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})
Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})
"""
    
print(output)

with open('Analysis/budget_analysis.text',"w") as analysis_file:
    analysis_file.write(output)


