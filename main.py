import csv


def load_sales_data(filename):
    sales_data = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append(float(row["amount"]))
    except FileNotFoundError:
        print("Error: File not found.")
        return None

    return sales_data


def calculate_statistics(sales_data):
    total_sales = sum(sales_data)
    sales_count = len(sales_data)
    highest_sale = max(sales_data)
    average_sale = total_sales / sales_count

    return {
        "total": total_sales,
        "count": sales_count,
        "highest": highest_sale,
        "average": average_sale,
    }


def display_results(stats):
    print("Sales Summary")
    print("-------------------")
    print(f"Total Revenue: £{stats['total']}")
    print(f"Number of Sales: {stats['count']}")
    print(f"Average Sale: £{stats['average']:.2f}")
    print(f"Highest Sale: £{stats['highest']}")


def main():
    filename = "sales_data.csv"
    sales_data = load_sales_data(filename)

    if sales_data:
        stats = calculate_statistics(sales_data)
        display_results(stats)


if __name__ == "__main__":
    main()
    
