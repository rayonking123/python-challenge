import csv
import os

file_to_load = "C:\\Users\\rockm\\Desktop\\School\\homework\\Python-challenge\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

# Parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]
total_revenue = 0

with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        total_months += 1
        total_revenue += int(row["Profit/Losses"])

        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list.append(revenue_change)  # Use append to add to a list
        month_of_change.append(row["Date"])

        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Average Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list) 

output = (
    f"\nFinancial Analysis\n"

    f"__________________________\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg:.2f}\n" 
    f"Greatest Increase: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)

print(output)

