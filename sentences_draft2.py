import random

words = ["the", "a", "one", "two", "some", "many", "adult", "bird", "boy", "car", "cat", "child", "dog", "girl", \
    "man", "woman", "adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women",  "drank",\
    "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "drinks", "eats", "grows", \
    "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "drink", "eat", "grow", "laugh", "think", "run",\
    "sleep", "talk", "walk", "write", "will drink", "will eat", "will grow", "will laugh", "will think", "will run", \
    "will sleep", "will talk", "will walk", "will write"]
def main():
    # List of the all the words that the functions will randomly select
    words = ["the", "a", "one", "two", "some", "many", "adult", "bird", "boy", "car", "cat", "child", "dog", "girl", \
    "man", "woman", "adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women",  "drank",\
    "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "drinks", "eats", "grows", \
    "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "drink", "eat", "grow", "laugh", "think", "run",\
    "sleep", "talk", "walk", "write", "will drink", "will eat", "will grow", "will laugh", "will think", "will run", \
    "will sleep", "will talk", "will walk", "will write"]
    
    # Call the random word picked by the functions get_determiner, get_noun, and get_verb and have that assigned from the list above.
    word = random.choice(words)
    word1 = random.choice(words)
    word2 = random.choice(words)
    
    # Call the the get_determiner, get_noun, and get_verb functions and select the different word cohices as needed.
    sentence = f'{get_determiner(word, grammatical_number=True)} {get_noun(word1, grammatical_number=True)} {get_verb(word2, grammatical_number=True, grammatical_number1=True, tense=True)}'
    sentence1 = f'{get_determiner(word, grammatical_number=False)} {get_noun(word1, grammatical_number=False)} {get_verb(word2, grammatical_number=True, tense=True)}'
    sentence2 = f'{get_determiner(word, grammatical_number=True)} {get_noun(word1, grammatical_number=True)} {get_verb(word2, grammatical_number=True, tense=False)}'
    sentence3 = f'{get_determiner(word, grammatical_number=False)} {get_noun(word1, grammatical_number=False)} {get_verb(word2, grammatical_number=False, grammatical_number1=True, tense=False)}'
    sentence4 = f'{get_determiner(word, grammatical_number=True)} {get_noun(word1, grammatical_number=True)} {get_verb(word2, grammatical_number=False, tense=False)}'
    sentence5 = f'{get_determiner(word, grammatical_number=False)} {get_noun(word1, grammatical_number=False)} {get_verb(word2, grammatical_number=False, tense=False)}'
    
    # Print the sentences for the user to see
    print(sentence)
    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)

def get_determiner(word, grammatical_number = 1):
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
        words = ['the', 'every','one']

        # word = random.choice(words)
    else:
        words = ["some", "many"]

        # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(word1, grammatical_number = 1):
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

def get_verb(word2, grammatical_number=1, grammatical_number1=1, tense=True):
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
    # if grammatical_number == 1 or grammatical_number != 1:
    #     if tense:
    #         words2 = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    if tense and grammatical_number == 1 and grammatical_number1 == 1:
        words2 = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif grammatical_number1 and tense:
        words2 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif grammatical_number1 != 1 and tense !=True:
            words2 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words2 = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word2 = random.choice(words2)
    return word2

# Call the function main() so the program starts executing.    
main()
