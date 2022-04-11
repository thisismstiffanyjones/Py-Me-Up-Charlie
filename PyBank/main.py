# Modeules
import os
import csv


# Setting up variables
total_months = 0
total_profit = 0.0
avg_change_in_profit = 0.0
greatest_increase = 0.0
greatest_increase_month = "month"
greatest_decrease = 0.0
greatest_decrease_month = "month"


# Lists to store data
months = []
values = []
changes = []


# Pulling and reading the csv file. Putting the months into one list and values into another
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        values.append(row[1])

        
# The total number of months included in the dataset
total_months = len(months)


# The net total amount of "Profit/Losses" over the entire period
for number in values:
    total_profit = total_profit + int(number)


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
for number in range(len(values)-1):
    changes.append(int(values[number+1])-int(values[number]))


sum_of_changes = 0
for number in changes:
    sum_of_changes = sum_of_changes + number

avg_change_in_profit = round(sum_of_changes / (total_months-1), 2)


# The greatest increase in profits (date and amount) over the entire period
goat = changes[0]

for number in changes:
    
    if number > goat:
        goat = number

greatest_increase = goat
greatest_increase_month=months[changes.index(goat)+1]


# The greatest decrease in profits (date and amount) over the entire period
not_goat = changes[0]

for number in changes:
    if number < not_goat:
        not_goat = number

greatest_decrease = not_goat

greatest_decrease = not_goat
greatest_decrease_month=months[changes.index(not_goat)+1]


# Printing of Financial Analysis to Terminal
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(avg_change_in_profit))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")


# Printing of Financial Analysis to Text File

   