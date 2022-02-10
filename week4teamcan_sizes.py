'''Computes and prints the storage efficiency for different can sizes'''

import math

def main():
    '''Calls the cylinder_volume, the cylinder_surface_area, and storage_efficiency functions \
    compute the can volume and surface area and storage efficiency.'''

    can_name = []
    storage_effiencies = []
    cost_effiencies = [] 
    storage_efficiency = 0
    cost_efficiency = 999999999999
    
    index = None
    # index1 = None

 # Create the text file for the 12 cans
    add_cans = ''
    while add_cans.lower() != 'done':
        name = input('Please enter can name: ')
        radius = float(input('Please enter can radius in centimeters: '))
        height = float(input('Please enter can height in centimeters: '))
        cost = float(input('Please enter the cost of the can: '))

        can_volume = compute_volume(radius, height)
        can_surface_area = compute_surface_area(radius, height)
        can_storage_efficiency = compute_storage_efficiency(can_volume, can_surface_area)
        can_cost_efficiency = compute_cost_efficiency(can_volume, cost)
        
        # index1 = cost_effiencies.index(cost_efficiency)


        print(f'The volume of the can is: {can_volume:.2f}. \n The surface area is: {can_surface_area:.2f}. \n The Storage efficiency is {can_storage_efficiency:.2f}. \n The Cost efficiency is {can_cost_efficiency:.2f}.')
        
        # print(f'The most storage effiecient can is {can_name[index]}.')
        # print(f'Most cost efficient can is {name[cost_efficiency]}.')
        

        with open('can_details.txt', 'at') as can_details:
            print(f'{name}, {radius}, {height}, {cost}, {can_storage_efficiency}, {can_cost_efficiency}', file=can_details)

        add_cans = input('Do you want to add more cans (Enter DONE when finished or YES to continue)? ')
        print(name)
        print(index)
    # print(f'The most storage efficient can is {can_name[index]}.')

    with open('can_details.txt') as can_details:
        for line in can_details:
            parts = line.strip().split(',')
            name = parts[0]
            radius = float(parts[1])
            height = float(parts[2])
            cost = float(parts[3])
            storage_efficiencies = parts[4]
            cost_efficiency  = float(parts[5])
            
            if storage_efficiency != 0:
                storage_effiencies.append(storage_efficiency)
                can_name.append(name)

                for i in storage_efficiency:
                    if i > storage_efficiency:
                        storage_efficiency = i
                        index = storage_efficiencies.index(storage_efficiency)
            
            # if cost_efficiency != 0:
            #     cost_effiencies.append(cost_efficiency)
            #     can_name.append(name)

            #     if i < cost_efficiency:
            #         cost_efficiency = i
            
    # index = storage_effiencies.index(storage_efficiency)
    # index1 = cost_effiencies.index(cost_efficiency)

# best_storage_efficient = max(storage_effiencies)
# best_cost_efficient = min(cost_effiencies)
# index = [i for i, v in enumerate(storage_effiencies) if v == storage_efficiency]
    
# efficient_storage_can = name[index]
# index1 = [j for j, v in enumerate(cost_effiencies) if v == cost_efficiency]
# efficient_cost_can = name[index1]
# print(index)

def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

# def append_storage_efficiencies(i):
#     for i in range(can_storage_efficiency):
#             storage_effiencies.append(i)
#             best_storage_efficient = max(storage_effiencies)

main()
