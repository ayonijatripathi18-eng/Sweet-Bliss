# SWEET BLISS CAFÉ – Python Management System

A Python-based café and bakery management system using CSV storage, NumPy analytics, and Matplotlib charts.  
This project manages menu display, multi-item orders, billing, analytics, expenses, and customer feedback — all inside the terminal.



## Features

### Menu Management
- Load menu from CSV  
- Display menu in the terminal  
- Show menu as a bar graph using Matplotlib  

### Order System
- Place multiple-item orders at once  
- Calculates price automatically  
- Saves all orders in `orders.csv`  
- Generates unique order IDs  

### Billing
- Generates a clean, readable bill  
- Shows item name, quantity, and total price  
- Shows grand total  

### Sales Analytics (NumPy + Matplotlib)
- Total sales  
- Average order value  
- Highest sale  
- Sales quantity bar chart  

### Expense Tracking
- Add expenses  
- Store in `expenses.csv`  
- Calculate total monthly expenses  

### Customer Feedback
- Stores name, rating, and comments  
- Permanently saved in `feedback.csv`  



## Project Structure


Sweet-Bliss-Cafe/
│
├── src/
│   ├── main.py
│   ├── menu.py
│   ├── orders.py
│   ├── bill.py
│   ├── analytics.py
│   ├── expenses.py
│   ├── feedback.py
│
├── data/
│   ├── menu.csv
│   ├── orders.csv
│   ├── expenses.csv
│   ├── feedback.csv
│
├── STATEMENT.md
├── README.md
└── requirements.txt


## Requirements

Create a file named `requirements.txt` and include:

numpy
matplotlib

*(csv is a built-in Python module — no installation needed.)*

Install libraries using:

pip install -r requirements.txt




## How to Run the Project

1. Open the folder in VS Code.  
2. Ensure all CSV files are inside the `data/` folder.  
3. Run the program in terminal:


python src/main.py




## Sample Outputs You Can Include in Report

✔ Menu display  
✔ Menu bar graph  
✔ Multiple-item ordering screen  
✔ Bill generation  
✔ Sales summary  
✔ Sales quantity chart  
✔ Expense added  
✔ Total expenses  
✔ Customer feedback entry  
✔ Exit message  



## System Architecture (Simple English)

- **main.py** — Controls all features and user choices.  
- **menu.py** — Shows menu + menu graph.  
- **orders.py** — Takes multi-item orders and saves them.  
- **bill.py** — Prints the bill.  
- **analytics.py** — Generates sales summary + charts.  
- **expenses.py** — Adds and totals expenses.  
- **feedback.py** — Saves customer reviews.  



## Purpose of the Project

This project replaces manual café operations with a lightweight digital system.  
Ideal for Python learners looking to practice:

- modular programming  
- CSV handling  
- NumPy  
- Matplotlib  
- terminal-based applications  
