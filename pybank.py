import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")


print("opening", csvpath)

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
  
    print(csvreader)

    csv_header =next(csvfile)

    print(f"Header: {csv_header}")
    total_months = 0
    profit_loss = 0
    value = 0
    change = 0
    dates = []
    profits = []

    for row in csvreader:

      
        dates.append(row[0])
        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        total_months += 1
        profit_loss += int(row[1])

   
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]

        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]

    avg_change = sum(profits)/len(profits)

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(profit_loss)}")
    print(f"Average Change: ${str(round(avg_change,2))}")
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

    # Create the financial analysis report text
report = f"{' Financial Analysis ':-^48}\n"                             \
         f"{'Total Months:':24}{total_months:24,.0f}\n"                   \
         f"{'Net Profits:':24}{profit_loss:24,.0f}\n"                   \
         f"{'Avg Change:':24}{avg_change:24,.2f}\n"                       \
         f"{'Max Increase:':14}{greatest_date:^20}{greatest_increase:14,.0f}\n" \
         f"{'Max Decrease:':14}{worst_date:^20}{greatest_decrease:14,.0f}\n" \
         f"{'--':-^48}"

# Assemble the output resource path. Include the base and
# repo paths to allow for both absolute and relative paths
resource_path = 'Resources/budget_analysis.txt'
output_path = os.path.join(resource_path)

# Open the analysis resource text file and write the report to it
with open(output_path, "w") as textfile:
    textfile.write(report)