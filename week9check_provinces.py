file_list = []
with open('provinces.txt', 'rt') as file:

    for i in file:
        clean = i.strip()
        file_list.append(clean)
        
    print(file_list)
    file_list.pop(0)
    file_list.pop()
    print()
    print(file_list)

    for j in range(len(file_list)):
        if file_list[j] == 'AB':
            file_list[j] = 'Alberta'
    
    alberta_count = file_list.count('Alberta')
    print()
    print(file_list)
    print()
    print(alberta_count)