import csv

total_sales = 0
sales_count = 0
highest_sale = 0

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        amount = float(row["amount"])
        total_sales += amount
        sales_count += 1
        
        if amount > highest_sale:
            highest_sale = amount

average_sale = total_sales / sales_count

print("Sales Summary")
print("-------------------")
print(f"Total Revenue: £{total_sales}")
print(f"Number of Sales: {sales_count}")
print(f"Average Sale: £{average_sale:.2f}")
print(f"Highest Sale: £{highest_sale}")
