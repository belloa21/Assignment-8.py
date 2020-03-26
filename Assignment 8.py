# Alex Bello
# 3/26/2020
# The driver for keeping track of stock totals and the total profit or loss from those stocks.

from Stack_class import Stack
from Stack_class import Queue


choice = int(input("""Please chose how you would like to work with your stocks
hit 1 for Stack, or hit 2 for Queue."""))


if choice == 1:
    myList = Stack()
else:
    myList = Queue()

total_stock_qty = 0
total_profit = 0.0
total_value_of_sold_stocks = 0.0
inventory_system_qty = choice
inventory_system_price = choice
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
        inventory_system_qty.push(qty)
        inventory_system_price.push(price)
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
                qty_popped = inventory_system_qty.pop()
                total_stock_qty -= qty_popped
                price = inventory_system_price.pop()
                total_sale += (qty_popped * price)
                total_popped += qty_popped
