mport csv
import os

FILENAME = "expenses.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Category", "Amount"])

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, category, amount])

    print("Expense added successfully!")

def view_summary():
    expenses = {}
    total = 0

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            total += amount
            expenses[row["Category"]] = expenses.get(row["Category"], 0) + amount

    print("\n Expense Summary:")
    for category, amt in expenses.items():
        print(f" - {category}: Rs. {amt:.2f}")
    print(f"\nTotal Spent: Rs. {total:.2f}")

def main():
    while True:
        print("\n Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.")

if __name__ == "__main__":
    main()
