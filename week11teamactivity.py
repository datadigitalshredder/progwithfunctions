print('Week 11 Team Activity')

# # Core requirement 1
# with open('hr_system.txt') as hr_file:
#     for data in hr_file:
#         # Core requirement 2 & 3
#         parts = data.split()
#         name = parts[0]
#         title = parts[2]
#         print(f'Name: {name}, Job title: {title}.')

# Stretch challenge
# Stretch challenge 1 & 2
expectancy_list = []
with open('hr_system.txt') as hr_file:
    for data in hr_file:
        parts = data.strip()
        parts1 = parts.split(' ')
        name = parts1[0]
        title = parts1[2]
        id = parts1[1]
        salary = float(parts1[3])
        paycheck = salary / 24
        
        if salary != 0:
            expectancy_list.append(salary)
print(expectancy_list)
big = max(expectancy_list)
print(big)

        # max_salary = max(salary)
        # print(f'{max_salary}')
        # print(f'Name: {name} (ID: {id}), Job title: {title} -- Paycheck: ${paycheck:.2f}.')

        # Stretch challenge 3
        # if parts1[2].lower() == 'engineer':
            # OR USE
        # if title.lower() == 'engineer':
            # paycheck += 1000
        # print(f'Name: {name} (ID: {id}), Job title: {title} -- Paycheck: ${paycheck:.2f}.')
        # number = -1
    
            # total = 0.0
            # for i in salary:
            #     total += i
            # print(total)

