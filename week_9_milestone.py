print("Welcome to the Shopping Cart Program.")

products = []
item_price = []

action = -1

while action != 0:
  print()
  print(f'Please select one of the following actions: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit')
  print()
  action = int(input('Please enter an action number: '))
    

    
  if action == 1:
      new_item = input("What item would you like to add? ")
      products.append(new_item)
  print(products)

# print()
# for new_item in products: 
#   print(f'{new_item} has been added to the cart and it cost ${item_price[0]}.')