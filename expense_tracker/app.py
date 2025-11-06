from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# --- Python OOP Classes ---
class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def total_expense(self):
        return sum(e.amount for e in self.expenses)

# Initialize Expense Manager
manager = ExpenseManager()

# --- Flask Routes ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        expense = Expense(amount, category)
        manager.add_expense(expense)
        return redirect("/")
    
    expenses = manager.get_expenses()
    total = manager.total_expense()
    return render_template("index.html", expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)
