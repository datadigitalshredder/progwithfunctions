print()
print('WELCOME TO THE SHOPPING CART PROGRAM')

items = []
prices = []

action = -1
while action != 5:
    print()
    print(f'Please select one of the following actions: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit')
    print()
    action = int(input('Please enter an action number: '))

    # Action 1: Adding items
    if action == 1:
        add = input('What item would you like to add to the cart? ').capitalize()
        price = float(input('What is the price of the item? '))
        items.append(add)
        prices.append(price)
        print()
        print(f'{add.upper()} worth ${price:,.2f} has been added to the cart.')

    # Action 2: Viewing items
    elif action == 2:
        print()  
        print(f'These are the items on the cart:')      
        for i in range(len(items)):
            item = items[i]
            price1 = prices[i]
            print(f'{i + 1:4}. {item:20} --- ${price1:15,.2f}')
        print(f'The total number of items on the cart is: {len(items)}')
   
    # Action 3: Removing items
    elif action == 3:
        print()
        print(f'These are the items on the cart:')
        for i in range(len(items)):
            item = items[i]
            price1 = prices[i]
            print(f'{i + 1:4}. {item:20} --- ${price1:15,.2f}')
        print(f'The total number of items on your the is: {len(items)}')

        remove = int(input('What item number would you like to remove from the cart, enter the correct item number (OTHERWISE NOTE: Entering zero removes the last item, -1 removes second last item, and -2 removes third last item and so on)? ')) - 1
        if  -1 < remove <= len(items) - 1:
            items.pop(remove)
            prices.pop(remove)
            print()
            print(f'Item number {remove + 1} has been removed from the cart.')
            print(f'These are now the item(s) on the cart:')
            for i in range(len(items)):
                item = items[i]
                price1 = prices[i]
                print(f'{i + 1:4}. {item:20} --- ${price1:15,.2f}')
            print(f'The total number of items on the cart is now: {len(items)}')

        elif remove == -1:
            items.pop()
            prices.pop()
            print()
            print(f'The last item (Item {len(items) + 1}) has been removed from the cart.')
            print(f'These are now the item(s) on the cart:')
            for i in range(len(items)):
                item = items[i]
                price1 = prices[i]
                print(f'{i + 1:4}. {item:20} --- ${price1:15,.2f}')
            print(f'The total number of items on the cart is now: {len(items)}')

        # Use the below conditions to stop the program from attempting to remove an item index that is out of range, 
        # i.e. avoiding the Python error message "items.pop(remove) IndexError: pop index out of range". 
        else:
            try:
                items.pop(remove)
                prices.pop(remove)
            except IndexError:
                pass
                print(f"Sorry, that's an invalid index. Please enter a valid index. \nA valid index on your cart is from 1 to {len(items)}.")

    # Action 4: Computing the total
    elif action == 4:
        print()
        print(f'These are the items on the cart:')
        for i in range(len(items)):
            item = items[i]
            price1 = prices[i]
            print(f'{i + 1:4}. {item:20} --- ${price1:15,.2f}')
        print(f'The total number of items on your cart is: {len(items)}')

        running_total = 0
        for j in prices:
            running_total += j
        print(f'The total price for items on your cart is: ${running_total:,.2f}')

# Action 5: Exiting the cart
else:
    print()
    print('Thank you for using my shopping cart program. Hope you loved your shopping!')
