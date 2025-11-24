import csv
import numpy as np

def addexp(name, amt): #addexp is a function that is used to add expenses
    expid = sum(1 for _ in open("data/expenses.csv")) #expid basically counts all the expenses entered by the user

    with open("data/expenses.csv", "a", newline="") as f: #in simple words with dunction is used to open and close a file without memory leaks orfile corruption
        writer = csv.writer(f) #gets a new column
        writer.writerow([expid, name, amt]) #adds three rows to that columns named expid, name and amt

    return "Expense added."

def totalexp():
    amt = []
    with open("data/expenses.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt.append(int(row["amount"])) #convert amount to int and adds to the list

    if len(amt) == 0:
        return 0

    return np.sum(amt)
