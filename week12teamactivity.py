print('Week 12 team activity- Files')
# CORE REQUIREMENTS
# number_of_chapters = 0
# book = None
# with open('books_and_chapters.txt') as books:
    
#     for lines in books:
#         parts = lines.split(':')
#         names = parts[0]
#         chapters = int(parts[1])
#         category = parts[2]
#         # print(names)
#         if chapters > number_of_chapters:
#             number_of_chapters = chapters
#             book = names
#     print(f'The largest number of chapters is {number_of_chapters} in {book}.')

# STRETCH REQUIREMENTS
chosen_catergory = input('Please enter a volume catergory to work with: ')
number_of_chapters = -1
book = None
chapters_total = 0
number_of_chapters_list = []

with open('books_and_chapters.txt') as books:
    for lines in books:
        parts = lines.split(':')
        names = parts[0].strip()
        chapters = int(parts[1])
        category = parts[2].strip()
        # print(names)
        if category.lower() == chosen_catergory.lower():
            print(f'Books: {names}, Chapters: {chapters}, Catergory: {category}')
            number_of_chapters_list.append(chapters)

            
            if chapters > number_of_chapters:
                number_of_chapters = chapters
                book = names
    for i in number_of_chapters_list:
        chapters_total += i
# sum_of_chapters = sum(chapters)
    print(number_of_chapters_list)
    print(chapters_total)
    print(f'In the {chosen_catergory.title()}, the largest number of chapters is {number_of_chapters} in {book}.')



    
