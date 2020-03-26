# Alex Bello
# 3/25/2020
# The driver for keeping track of stock totals and the total profit or loss from those stocks.

from Stack_class import Stack
from Stack_class import Queue


choice = 0

while choice != 2:
    print("Please choose who you would like to work with your stocks.")
    print("1. Using a stack.")
    print("2. Using a queue.")
    choice = int(input(">"))


total_inventory_qty = 0
total_profit = 0.0
total_value_sold = 0.0
inventory_system_qty= Stack()
inventory_system_price = Stack()
choice = 0

while choice != 5:
    print("Please select an option from the menu below:")
    print("1. Add stock to your portfolio")
    print("2. Sell stock from your portfolio")
    print("3. See the total number of stocks you own")
    print("4. See total profit")
    print("5. Exit Program")
    choice = int(input(">"))

    if choice == 1:
        qty = int(input("How many are you adding?"))
        price = float(input("How much does each cost?"))
        inventory_system_qty.push(qty)
        inventory_system_price.push(price)
        print("Added to inventory. \n\n")

        total_inventory_qty += qty

    elif choice == 2:
        qty_needed = int(input("How many are you looking to sell?"))
        if qty_needed > total_inventory_qty:
            print("You do not have that many available for sale.\n\n")
            # This statement makes the loop start back at the menu
            continue
        else:
            total_popped = 0
            total_sale = 0.0

            # These next 5 lines are the key to keeping track of where you are
            qty_popped = inventory_system_qty.pop()
            total_inventory_qty -= qty_popped
            price = inventory_system_price.pop()
            total_sale += (qty_popped * price)
            total_popped += qty_popped
            # Keep popping until we have enough
            while total_popped < qty_needed:
                qty_popped = inventory_system_qty.pop()
                total_inventory_qty -= qty_popped
                price = inventory_system_price.pop()
                total_sale += (qty_popped * price)
                total_popped += qty_popped

            # We should have popped enough, but did we pop too many?  Push the extra back on.
            if total_popped > qty_needed:
                overage = total_popped - qty_needed
                inventory_system_qty.push(overage)
                inventory_system_price.push(price)
                total_inventory_qty += overage
                total_sale -=(overage * price)

            # Let's calculate the profit on what we are selling and keep track of it
            total_value_sold += total_sale
            total_profit += (total_sale * .1)
        print(f"You have successfully filled the order for {qty_needed}\n")

    elif choice == 3:
        print(f"The total current inventory quantity is {total_inventory_qty}\n")

    elif choice == 4:
        print(f"The total profit from sales is currently ${total_profit}\n")
