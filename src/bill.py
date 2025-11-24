def generate_bill(orderdata): #a function that is used to generate a bill
    print("\n========== BILL ==========") #\n is used to move to a new line
    print(f"Order ID : {orderdata['order_id']}") #prints the order id
    print("---------------------------")

    for item in orderdata["items"]: #creates a loop to print all the order data
        print(f"{item['name']}  x{item['qty']}  -  ₹{item['item_total']}")

    print("---------------------------")
    print(f"TOTAL AMOUNT : ₹{orderdata['total_price']}") #prints the total amount of a particular customer's order
    print("===========================\n")
