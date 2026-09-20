# I attempted the base level with some intermmedite elements
# Updated Expense Records
# Date        Description                         AmountCategory            
# --------------------------------------------------------------------------
# 2026-09-19  Gas                                  80.00Travel              
# 2026-09-19  Bill                                250.00Electric Bill       
# 2026-09-19  McDonalds                             5.99Meals               
#
# Enter a keyword to search for: Meals
#
#Search Results for 'Meals'
#Date        Description                         AmountCategory            
# --------------------------------------------------------------------------
# 2026-09-19  McDonalds                             5.99Meals               
#
# Expense Totals by Category
# -----------------------------------
# Travel               $     80.00
# Electric Bill        $    250.00
# Meals                $      5.99
# -----------------------------------
# Updated Expense Records
# Date        Description                         AmountCategory            
# --------------------------------------------------------------------------
# 2026-09-19  Gas                                  80.00Travel              
# 2026-09-19  Bill                                250.00Electric Bill       
# 2026-09-19  McDonalds                             5.99Meals               
# 2026-09-19  Gas                                  74.00200                 
# 2026-09-19  Meals                                54.00Meals               
# 2026-09-19  Gas                                  54.00Travel              
# 2026-09-19  McDonalds                            20.99Meals               

# Enter a keyword to search for: Meals

# Search Results for 'Meals'
# Date        Description                         AmountCategory            
# --------------------------------------------------------------------------
# 2026-09-19  McDonalds                             5.99Meals               
# 2026-09-19  Meals                                54.00Meals               
# 2026-09-19  McDonalds                            20.99Meals               

# Expense Totals by Category
# -----------------------------------
# Travel               $    134.00
# Electric Bill        $    250.00
# Meals                $     80.98
# 200                  $     74.00
# -----------------------------------

# Expense tracker program has finished.


# Expense Report
import os
import csv
import datetime


def build_record(date, description, amount, category):
    """Build and return one formatted expense record."""

    # Limit description to 30 characters
    description = description[:30]

    # Format amount to exactly two decimal places
    formatted_amount = f"{amount:.2f}"

    # Create a record containing four fields
    record = [date, description, formatted_amount, category]

    return record


def load_records(filename):
    """Read saved expenses and return a list of lists."""

    records = []

    # Check if the file exists before opening it
    if os.path.exists(filename):

        # Use csv.reader to read the CSV file
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for record in reader:
                # Skip blank records
                if not record:
                    continue

                records.append(record)

    return records


def display_records(records):
    """Print expense records in a readable, aligned format."""

    if not records:
        print("No expenses on record yet.")
        return

    # Print header row
    print(
        f"{'Date':<12}"
        f"{'Description':<32}"
        f"{'Amount':>10}"
        f"{'Category':<20}"
    )

    # Print separator line
    print("-" * 74)

    # Print each record
    for record in records:
        print(
            f"{record[0]:<12}"
            f"{record[1]:<32}"
            f"{record[2]:>10}"
            f"{record[3]:<20}"
        )


def search_records(records, keyword):
    """Return records matching a keyword, ignoring case."""

    matches = []

    keyword = keyword.lower()

    for record in records:
        description = record[1].lower()
        category = record[3].lower()

        if keyword in description or keyword in category:
            matches.append(record)

    return matches


def calculate_totals(records):
    """Calculate and display expense totals by category."""

    totals = {}

    for record in records:
        category = record[3]
        amount = float(record[2])

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\nExpense Totals by Category")
    print("-" * 35)

    if not totals:
        print("No expenses on record yet.")
        return

    for category, total in totals.items():
        print(f"{category:<20} ${total:>10.2f}")

    print("-" * 35)


# Main program flow
filename = "expenses.csv"

try:
    # Load and display existing records
    records = load_records(filename)
    display_records(records)

    # Ask how many new expenses to add
    number_of_expenses = int(
        input("\nHow many new expenses would you like to add? ")
    )

    # Collect new expenses
    for i in range(number_of_expenses):
        print(f"\nExpense {i + 1}")

        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: $"))
        category = input("Enter expense category: ")

        date = str(datetime.date.today())

        # Build the expense record
        record = build_record(
            date,
            description,
            amount,
            category
        )

        # Append the new record using csv.writer and writerow()
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(record)

    # Reload and display all records
    records = load_records(filename)

    print("\nUpdated Expense Records")
    display_records(records)

    # Search for expenses
    keyword = input("\nEnter a keyword to search for: ")
    search_results = search_records(records, keyword)

    print(f"\nSearch Results for '{keyword}'")
    display_records(search_results)

    # Calculate totals by category
    calculate_totals(records)

except ValueError:
    print("\nError: Please enter a valid number.")

except FileNotFoundError:
    print("\nError: The expense file could not be accessed.")

except Exception as error:
    print(f"\nAn unexpected error occurred: {error}")

finally:
    print("\nExpense tracker program has finished.")
