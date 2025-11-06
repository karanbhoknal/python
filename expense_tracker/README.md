💰 Personal Expense Tracker Web App
🧠 Overview

The Personal Expense Tracker Web App is a clean and interactive application built using Python (OOP + Flask) with a modern HTML, CSS, and JavaScript frontend.

It allows users to easily add, view, and calculate total expenses in real-time. This project demonstrates how Python classes and functions can be integrated with frontend technologies to create a full-stack web app.

🚀 Features

Add expenses with amount, category, and date

View all expenses in a structured table format

Automatically calculate total expenses

Highlight large expenses using JavaScript

Designed with Object-Oriented Programming (OOP) in Python

Simple, responsive, and user-friendly interface

🧩 Tech Stack
Layer	Technologies Used
Backend	Python, Flask
Frontend	HTML, CSS, JavaScript
Architecture	Object-Oriented Programming
Tools	VS Code, Virtual Environment
📁 Folder Structure
expense_tracker/
│
├── templates/
│   └── index.html          # Frontend template
│
├── static/
│   ├── style.css           # CSS styling
│   └── script.js           # JavaScript interactivity
│
├── app.py                  # Flask backend and OOP logic
└── README.md               # Project documentation

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate the Virtual Environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4️⃣ Install Flask
pip install flask

5️⃣ Run the Application
python app.py

6️⃣ Open in Browser

Open:
👉 http://127.0.0.1:5000/

💻 How It Works

User enters expense amount and category.

Flask processes the input and creates an Expense object.

ExpenseManager class stores and manages all expense records.

Expenses are displayed in a dynamic HTML table.

Total expense is calculated automatically using Python functions.

🧾 Example Output
Date	Category	Amount ($)
2025-11-06	Groceries	250.00
2025-11-06	Rent	1200.00
2025-11-06	Utilities	300.00

Total Expense: 💵 $1750.00

🔮 Future Enhancements

Add SQLite database for permanent storage

Add Login & Registration functionality

Integrate Chart.js for data visualization

Add category filters and CSV export options

👨‍💻 Author

Karan Bhoknal
Python Developer | Data Engineering Enthusiast
📫 [https://www.linkedin.com/in/karan-bhoknal-2bb947297/]

🌟 Support

If you like this project, please give it a ⭐ on GitHub!
Your support motivates me to build more amazing projects 🚀

🏷️ Tags

#Python #Flask #HTML #CSS #JavaScript #OOP #FullStack #ExpenseTracker #WebApp #CodingJourney