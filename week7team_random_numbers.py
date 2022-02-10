import random
# numbers_list = []
def main():
    randnums = [16.2, 75.1, 52.3]
    print(f'The initail list is {randnums}')

    append_random_numbers(randnums)
    print(f'After appending the first number, the list is {randnums}')

    append_random_numbers(randnums, quantity=3)
    print(f'After appending three more numbers, the list is {randnums}')

    words = []
    # for i in range(words):
    print(f'The initial word list is {words}')

    append_random_words(words)
    print(f'After appending the first word, the list is {words}')

    append_random_words(words, quantity=9)
    print(f'After appending the first word, the list is {words}')
    
    
def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        number = random.uniform(0, 100)
        number1 = round(number, 1)
        numbers_list.append(number1)

def append_random_words(words_list, quantity=1):
    words = ['Arrange', 'a', 'one', 'hour', 'synchronous', 'meeting', 'with', 'your', 'team', 'for', 'this', 'activity']
    for _ in range(quantity):
        
        word = random.choice(words)
        words_list.append(word)

if __name__ == "__main__":
    main()



