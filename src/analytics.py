import csv
import numpy as np
import matplotlib.pyplot as plt

def sales_summary():
    total = [] #Create an empty python list which will store each order's total price
    with open("data/orders.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total.append(int(row["total_price"])) #.append fuction is used when you want to add something in an empty list i.e. total

    if len(total) == 0: #It returns order of rows and if the list is empty then it returns 0 0 0
        return 0, 0, 0

    total = np.array(total) #Converts python list to numpy array.

    return np.sum(total), np.mean(total), np.max(total)
    """
    np.sum(total) returns total revenue
    np.mean(total) returns average i.e. mean
    np.max(total) returns the largest single total_price in orders i.e. maximum sale
    """
    #The above written is called a docstring

def sales_chart(): #It is a function that creats a bar chart of item sales and their quantity
    item_id = [] #An empty list to store item ids
    quantities = [] #An empty list to store quantity of that item

    with open("data/orders.csv", "r") as f: #This will open orders.csv and repeat rows as dictionaries
        r = csv.DictReader(f)
        for row in r:
            item_id.append(row["item_id"]) #Add items to the item_id list using .append
            quantities.append(int(row["quantity"])) #Add quantity to the quantities list using .append

    if len(quantities) == 0: #If this functions finds the list it prints "No sales yet."
        print("No sales yet.")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(item_id, quantities)
    plt.title("Item Sales Quantity") #Gives title to the bar chart
    plt.xlabel("Item ID") #Name the x axis
    plt.ylabel("Quantity Sold") #Name the y axis
    plt.tight_layout() 
    plt.show() #show the final graph
