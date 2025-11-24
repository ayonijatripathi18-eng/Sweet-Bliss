import csv
import numpy as np

# this function is used when customer orders more than one item at the same time
def placeorder(items_list):
    """
    first we load the menu into a dictionary
    so we can check prices and names quickly using item_id
    """
    menu = {}
    with open("data/menu.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            menu[int(row["item_id"])] = {
                "name": row["item_name"],
                "price": int(row["price"])
            }

    order_details = [] # this will store all items that the customer ordered
    total_price = 0 # this will add all item totals together for final bill

    
    order_id = sum(1 for _ in open("data/orders.csv"))

    
    for item_id, qty in items_list:
        if item_id not in menu: # checking if item exists in the menu
            return None, f"Item ID {item_id} does not exist!"

        name = menu[item_id]["name"] #name of item
        price = menu[item_id]["price"] #price of item
        item_total = price * qty #to calculatee how much this item costs in total
        total_price += item_total #adding this amount to the final total of the order

        #to save the order to the orders.csv file
        with open("data/orders.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([order_id, item_id, qty, item_total])

        #to store the order details in a list to print bill
        order_details.append({
            "item_id": item_id,
            "name": name,
            "price": price,
            "qty": qty,
            "item_total": item_total
        })

    return { #returns order details
        "order_id": order_id,
        "items": order_details,
        "total_price": total_price
    }, "Order placed successfully!"
