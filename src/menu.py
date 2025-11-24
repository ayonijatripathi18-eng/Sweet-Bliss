import csv
import matplotlib.pyplot as plt

def loadmenu(): #this funtion derives menu items from the menu.csv
    menulist = [] #it is an empty list to store menu items
    with open("data/menu.csv", "r") as f:
        reader = csv.DictReader(f) #it reads each row as a dictionary
        for row in reader:
            menulist.append(row)
    return menulist

def menuchart(): #this function shows the menu in the form of a bar chart
    menulist = loadmenu()  # FIXED: calling loadmenu()
    items = [m["item_name"] for m in menulist] #to make list for item names and thir amount
    prices = [int(m["price"]) for m in menulist]

    plt.figure(figsize=(9, 6)) #for chart to look bigger
    plt.barh(items, prices) #to create bar chart
    plt.title("Café + Bakery Menu") #to add title to the chatt
    plt.xlabel("Price (₹)") #to name x axis
    plt.tight_layout()
    plt.show() #to show the cahrt

def menuprint(): #it prints the menu
    menulist = loadmenu()  # FIXED: calling loadmenu()
    print("\n------- MENU --------")
    for m in menulist:
        print(f"{m['item_id']}. {m['item_name']} - ₹{m['price']}")
