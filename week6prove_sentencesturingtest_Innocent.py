print('Printing random sentences from lists of determiners, nouns, verbs, and prepositions. \
    \nBy Innocent Hove.\n')
import random

def main():

    # Call the the get_determiner, get_noun, and get_verb functions and select the different word choices in the following order:
    
    # Grammatical Number	Verb Tense
    # a.	single	        past
    # b.	plural          past
    # c.	single	        present
    # d.	plural	        present
    # e.	single	        future
    # f.	plural	        future.

    # Simple sentences
    sentence = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=True)}.'.capitalize()
    sentence1 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=True)}.'.capitalize()
    sentence2 = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=True, tense=False)}.'.capitalize()
    sentence3 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=False, tense=False)}.'.capitalize()
    sentence4 = f'{get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=False)}.'.capitalize()
    sentence5 = f'{get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=False)}.'.capitalize()
    
    # Complex sentences
    sentence6 = f'{get_time_noun(tense=0)} {get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=True)} {get_prepositional_phrase(quantity=True)}.'.capitalize()
    sentence7 = f'{get_time_noun(tense=0)} {get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=True)} {get_prepositional_phrase(quantity=False)}.'.capitalize()
    sentence8 = f'{get_time_noun(tense=1)} {get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=True, tense=False)} {get_prepositional_phrase(quantity=True)}.'.capitalize()
    sentence9 = f'{get_time_noun(tense=1)} {get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=False, tense=False)} {get_prepositional_phrase(quantity=False)}.'.capitalize()
    sentence10 = f'{get_time_noun(tense=2)} {get_determiner(grammatical_number=True)} {get_noun(grammatical_number=True)} {get_verb(grammatical_number=None, tense=False)} {get_prepositional_phrase(quantity=True)}.'.capitalize()
    sentence11 = f'{get_time_noun(tense=2)} {get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=False)} {get_prepositional_phrase(quantity=False)}.'.capitalize()
    sentence12 = f'{get_time_noun(tense=2)} {get_determiner(grammatical_number=False)} {get_noun(grammatical_number=False)} {get_verb(grammatical_number=None, tense=False)} {get_prepositional_phrase(quantity=True)}.'.capitalize()
    
    # Print the sentences for the user to see. Use different sentence formats from differrent places in the file.
    print(sentence)
    print(sentence1)
    print(sentence2)
    print(sentence3)
    print(sentence4)
    print(sentence5)
    print()
    print(sentence6)
    print(sentence7)
    print(sentence8)
    print(sentence9)
    print(sentence10)
    print(sentence11)
    print(sentence12)

def get_time_noun(tense):
    """Return a randomly chosen date. If tense is "past", this
    function will return one of these nouns:
    'Yesterday,', 'Last year,'
        
    If tense is "present" , this
    function will return one of these nouns:
        'Today,', 'This hour,'

    If tense is "future", this function will return one of
    these nouns:
    'Today,', Tomorrow,', 'Next week,', 'Next year,'
        
    """ 
    if tense == 0:
        words = ['Yesterday,', 'Last year,']
    elif tense == 1:
        words = ['Today,', 'This hour,']   
    else: 
        words = ['Today,', 'Tomorrow,', 'Next week,', 'Next year,']
    
    word = random.choice(words)
    return word
     
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
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    word = random.choice(words)
    return word

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
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif grammatical_number == True and tense == False:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif grammatical_number == False and tense == False:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]       
    else: 
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        # Call the deteminer and noun functions if the determiner and noun is singular 
        get_determiner(grammatical_number=True)
        get_noun(grammatical_number=True)

    else:
        # Call the deteminer and noun functions if the determiner and noun is plural 
        get_determiner(grammatical_number=False)
        get_noun(grammatical_number=False)

    # Create a phrase depending on the quantity of the determiner/ noun (singular or plural)
    phrase = get_preposition()+ ' ' +get_determiner(quantity)+ ' ' +get_noun(quantity)  
    return phrase
    
# Call the function main() so the program starts executing.    
main()
