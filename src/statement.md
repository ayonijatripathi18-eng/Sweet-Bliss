# Café Management System — Project Statement

## 1. Problem Statement
Small cafés and bakeries often handle daily operations manually — including taking orders, calculating bills, managing expenses, recording feedback, and analyzing sales.  
Manual management leads to:

- Billing errors  
- Poor tracking of revenue & expenses  
- No sales insights or analytics  
- Lack of customer feedback records  
- Difficulty storing and viewing historical data  

To improve workflow and efficiency, there is a need for a simple, digital, and lightweight management system.



## 2. Scope
This project is a **Python-based, terminal-operated Café Management System** that provides core café operations in digital form.

The system allows the café to:

- Display menu and prices from a CSV file  
- Take **multiple-item orders** at once  
- Auto-calculate totals and generate printed bills  
- Store orders permanently using CSV  
- Track expenses & generate total monthly expense  
- Record customer feedback  
- Display menu charts & sales analytics using Matplotlib  
- Perform basic statistical analysis using NumPy  

The system works fully offline and requires no GUI or database.



## 3. Target Users
### **Primary Target Users**
- Small cafés  
- Bakery shops  
- Student cafés  
- Home bakeries  

### **Secondary Users**
- Students creating projects for Python practice  
- Beginners learning file handling, NumPy & Matplotlib  
- Anyone wanting a simple digital management system  



## 4. High-Level Features

### **Menu Management**
- Load menu from `menu.csv`  
- Show menu in terminal  
- Display graphical menu chart (Matplotlib)

### **Order Management**
- Take **multiple items** in one order  
- Automatically calculate total  
- Store every order in `orders.csv`  
- Generate item-wise sales data  

### **Bill Generation**
- Print clean, formatted bills  
- Show item name, quantity, and item-wise totals  
- Generate unique order ID

### **Sales Analytics** (NumPy)
- Total daily/monthly sales  
- Average order value  
- Highest order value  
- Sales quantity chart

### **Expense Management**
- Add expenses  
- Store in `expenses.csv`  
- Calculate total monthly expenses

### **Customer Feedback**
- Save name, rating, and comments  
- Stored in `feedback.csv` for future improvement
