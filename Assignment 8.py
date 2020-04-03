# Alex Bello
# 3/26/2020
# The driver for keeping track of stock totals and the total profit or loss from those stocks.

from Stack_class import Qty_Stack
from Stack_class import Price_Stack
from Stack_class import Qty_Queue
from Stack_class import Price_Queue


choice = int(input("""Please chose how you would like to work with your stocks
hit 1 for Stack, or hit 2 for Queue."""))


if choice == 1:
    qty = Qty_Stack()
    price = Price_Stack()
else:
    qty = Qty_Queue()
    price = Price_Queue

total_stock_qty = 0
total_profit = 0.0
total_value_of_sold_stocks = 0.0
menu = 0

while menu != 5:
    print("Welcome to the menu! Select one of the five options below to start managing your stocks!")
    print("1. Add stocks to your portfolio.")
    print("2. Sell stock from your portfolio.")
    print("3. See how many stocks you own.")
    print("4. Look at your profit/loss.")
    print("5. Exit the menu.")
    menu = int(input(">"))

    if menu == 1:
        qty = int(input("How many stocks are you buying today?"))
        price = float(input("How much are they?"))
        Qty_Stack.push(qty)
        Qty_Queue.push(qty)
        Price_Stack.push(price)
        Price_Queue.push(price)
        print("Alright, everything's in.")

        total_stock_qty += qty

    elif menu == 2:
        qty_needed = int(input("How many stocks would you like to sell?"))
        if qty_needed > total_stock_qty:
            print("You don't seem to have enough stocks to do that.")
        else:
            total_popped = 0
            total_sale = 0.0

            qty_popped = inventory_system_qty.pop()
            total_stock_qty -= qty_popped
            price = inventory_system_price.pop()
            total_sale += (qty_popped * price)
            total_popped += qty_popped
            while total_popped < qty_needed:
                qty_popped = Qty_Stack.pop()
                qty_popped = Qty_Queue.pop()
                total_stock_qty -= qty_popped
                price = Price_Stack.pop()
                price = Price_Queue.pop()
                total_sale += (qty_popped * price)
                total_popped += qty_popped
            while total_popped < qty_needed:
                qty_popped = Qty_Stack.pop()
                qty_popped = Qty_Queue.pop()
                total_stock_qty -= qty_popped
                price = inventory_system_price.pop()
                total_sale += (qty_popped * price)
                total_popped += qty_popped

            if total_popped > qty_needed:
                overage = total_popped - qty_needed
                inventory_system_qty.push(overage)
                inventory_system_price.push(price)
                total_stock_qty += overage
                total_sale -=(overage * price)

            total_value_of_sold_stocks += total_sale
            total_profit += (total_sale * .1)
        print(f"You have successfully filled the order for {qty_needed}\n")
