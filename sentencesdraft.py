import random

grammatical_number = None

tense = ''
word = ''
word1 = ''
word2 = ''
def main():
    # List of the all the words that the functions will randomly select
    # if grammatical_number == 1:
    #     word_singular = ["the", "a", "one", "every", "adult", "bird", "boy", "car", "cat", "child", "dog", "girl", \
    #     "man", "woman"]
    #     word = random.choice(word_singular)
    # else:
    #     word_plural = ["two", "some", "many", "adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    #     word1 = random.choice(word_plural)
    
    # if tense:
    #     word_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    #     word2 = random.choice(word_past)
    # elif tense and grammatical_number:
    #     word_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    #     word2 = random.choice(word_present)
    # elif tense and grammatical_number !=1:
    #     word_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    #     word2 = random.choice(word_present)
    # else:
    #     word_future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    #     word2 =random.choice(word_future)
    
    # Call the random word picked by the functions get_determiner, get_noun, and get_verb and have that assigned from the list above.

    # Call the the get_determiner, get_noun, and get_verb functions and select the different word cohices as needed.
    sentence = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=True)}'
    sentence1 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=True)}'
    sentence2 = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=True, tense=False)}'
    sentence3 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=False, tense=False)}'
    sentence4 = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=False)}'
    sentence5 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=False)}'
    
    # Print the sentences for the user to see
    print(sentence)
    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ['the', 'a', 'one', 'every']

        # word = random.choice(words)
    else:
        words = ["some", "many"]

        # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        words1 = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    else:
        words1 = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    word1 = random.choice(words1)
    return word1

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if grammatical_number == None and tense == True:
        words2 = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif grammatical_number == True and tense == False:
        words2 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif grammatical_number == False and tense == False:
        words2 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]       
    else: #grammatical_number == None and tense == False:
        words2 = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word2 = random.choice(words2)
    return word2

# Call the function main() so the program starts executing.    
main()
