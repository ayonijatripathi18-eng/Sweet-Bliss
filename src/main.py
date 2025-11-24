from menu import menuprint, menuchart
from orders import placeorder
from analytics import sales_summary, sales_chart
from expenses import addexp, totalexp
from feedback import feedback
from bill import generate_bill

print("\n===== WELCOME TO SWEET BLISS CAFE! =====\n") #welcome message

while True: #this loops keeps the program running until user chooses the exit option
    print("\n1. Show Menu")
    print("2. Show Menu Chart (Graph)")
    print("3. Place Multiple-Item Order")
    print("4. Show Sales Analytics Summary")
    print("5. Add Expense")
    print("6. Show Total Expenses")
    print("7. Give Feedback")
    print("8. Show Sales Quantity Chart")
    print("9. Exit")

    try: #try and except is used when we dont want to crash the entire program just because user entered a different value than what was required
        ch = int(input("\nEnter your choice: "))
    except: #except keeps the rpgram running even when user enters any undesired value
        print("Invalid input! Please enter a number.")
        continue


    if ch == 1: #to print full menu
        menuprint()

   
    elif ch == 2: #shows a bar garph of menu items and their prices
        menuchart()

   
    elif ch == 3: #to take multiple items order from the customer
        print("\nEnter multiple items for this order.")
        print("Type 0 to finish adding items.")

        items_list = []
        while True:
            try:
                item_id = int(input("\nItem ID (0 to stop): "))
            except:
                print("Invalid item ID")
                continue

            if item_id == 0: #when user enters 0 it stops taking more items
                break

            qty = int(input("Quantity: ")) #to ask the quantity of the particular item
            items_list.append((item_id, qty))

        if len(items_list) == 0:
            print("No items selected! Order cancelled.")
        else:
            order_data, msg = placeorder(items_list)
            if order_data: #if order is successfull then it prints the bill
                print(msg)
                generate_bill(order_data)
            else:
                print(msg)

   
    elif ch == 4: #shows sales summary
        total, avg, max_sale = sales_summary()
        print("\n----- SALES SUMMARY -----")
        print(f"Total Sales Amount : ₹{total}")
        print(f"Average Order Value: ₹{avg:.2f}")
        print(f"Highest Single Sale: ₹{max_sale}")

   
    elif ch == 5: #to add a new expense like butter or milk etc.
        name = input("Expense name: ")
        try:
            amt = int(input("Amount: "))
        except:
            print("Invalid amount!")
            continue

        print(addexp(name, amt))

   
    elif ch == 6: #to show the total expenses of the cafe
        print("\nTotal expenses so far: ₹", totalexp())

   
    elif ch == 7: #to take feedback from the customer
        name = input("Customer name: ")
        try:
            rating = int(input("Rating (1–5): "))
        except:
            print("Invalid rating!")
            continue

        comment = input("Comments: ")
        print(feedback(name, rating, comment))

   
    elif ch == 8: #shows bar graph of items
        sales_chart()

   
    elif ch == 9: #shows a thank you message and exits the program
        print("THANK YOU FOR VISITING!")
        break

    else:
        print("Invalid choice! Please try again.")
