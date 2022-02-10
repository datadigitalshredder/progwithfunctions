print('Number of boxes')

print()
import math
total_items = int(input('How many items have been manufactured? '))
carton_size = int(input('How many items are to be packed per carton? '))

number_of_boxes = math.ceil(total_items / carton_size)

print(f'The number of boxes required is {number_of_boxes}.')
print()

# Sample solution
# import math

# num_items = int(input("Enter the number of items: "))
# items_per_box = int(input("Enter the number of items per box: "))

# # Compute the number of boxes.
# num_boxes = math.ceil(num_items / items_per_box)

# # Display the results for the user to see.
# print(f"For {num_items} items, packing {items_per_box}"
# f" items in each box, you will need {num_boxes} boxes.")