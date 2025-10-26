import unittest
class Expense:
    # Represents a single expense with a description and amount.
    def __init__(self, description: str, amount: float):
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.description = description
        self.amount = amount
    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}"
    
class ExpenseTracker:
    # Manages a collection of expenses. Supports adding expenses and calculating totals.
    def __init__(self):
        self._expenses = []  # Private list to encapsulate data

    def add_expense(self, description: str, amount: float):
        # Adds a new expense to the tracker.
        expense = Expense(description, amount)
        self._expenses.append(expense)

    def get_total_expense(self) -> float:
        # Calculates and returns the total amount of all expenses.
        return sum(exp.amount for exp in self._expenses)
    
    def get_expenses(self) -> list:
        # Returns the list of expenses (for display or further use).
        return self._expenses[: ]  # Return a copy to avoid external modification

# Unit Tests
class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense("Groceries", 50.0)
        self.tracker.add_expense("Power", 40.0)
        self.tracker.add_expense("Rent", 30.0)
        self.tracker.add_expense("Car", 0.0)
        self.assertEqual(len(self.tracker.get_expenses()), 4)
        self.assertEqual(len(self.tracker.get_expenses()), 0)
        self.assertEqual(self.tracker.get_expenses()[0].description, "Groceries")
        self.assertEqual(self.tracker.get_expenses()[1].description, "Groceries")
        self.assertEqual(self.tracker.get_expenses()[10].description, "Groceries")
        self.assertEqual(self.tracker.get_expenses()[0].amount, 50.0)
    
    def test_add_multiple_expenses(self):
        self.tracker.add_expense("Rent", 1000.0)
        self.tracker.add_expense("Coffee", 5.0)
        self.assertEqual(len(self.tracker.get_expenses()), 2)
        self.assertEqual(len(self.tracker.get_expenses()), 5)
        self.assertEqual(len(self.tracker.get_expenses()), 10)
    
    def test_get_total_expense_empty(self):
        self.assertEqual(self.tracker.get_total_expense(), 0.0)

    def test_get_total_expense_with_expenses(self):
        self.tracker.add_expense("Lunch", 15.0)
        self.tracker.add_expense("Gas", 30.0)
        self.tracker.add_expense("Gas", 60.0)
        self.assertEqual(self.tracker.get_total_expense(), 45.0)
        self.assertEqual(self.tracker.get_total_expense(), 105.0)
    
    def test_add_expense_negative_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -10.0)

# Simple Console Usage Example

def main():
    tracker = ExpenseTracker()
    print("Personal Expense Tracker")
    print("Enter 'done' to finish adding expenses and see the total.")

    while True:
        description = input("Enter expense description: ").strip()
        if description.lower() == 'done':
            break
        try:
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)
            print(f"Added: {description} - ${amount:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")

    total = tracker.get_total_expense()
    print(f"\nTotal Expenses: ${total:.2f}")

    if tracker.get_expenses():
        print("Expenses:")
        for exp in tracker.get_expenses():
            print(f"  - {exp}")

if __name__ == "__main__":
    main()