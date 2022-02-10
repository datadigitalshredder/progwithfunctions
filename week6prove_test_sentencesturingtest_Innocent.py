print('This function tests the accurateness of the different word combinations in sentences.py.\nBy Innocent Hove.')
print()
from week6prove_sentencesturingtest_Innocent import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ['the', 'a', 'one', 'every']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.

    single_noun = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_noun(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_noun

def test_get_verb():
    # 1. Test the past verb tense.
    verb_past = ['The', 'A', 'One', 'Every', "Some", "Many", "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_verb(1, 2)
        word1 = get_verb(1, 2)
        # Verify that two words (the determiner and verb) returned from get_verb are
        # words in the verb_past list.
       
        assert word, word1 in verb_past

    # 2. Test the present verb tense. 
    verb_present = ['The', 'A', 'One', 'Every', "Some", "Many", "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes",\
        "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_verb(2, 1)
        word1 = get_verb(2, 2)

        # Verify that two words (the determiner and verb) returned from get_verb
        # are words in the verb_present list.
        
        assert word, word1 in verb_present
    
    # 3. Test the future verb tense.
    verb_future = ['The', 'A', 'One', 'Every', "Some", "Many", "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", \
        "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_verb(3, 1)
        word1 = get_verb(3, 2)

        # Verify that two words (the determiner and verb) returned from get_verb
        # is one of the words in the verb_future list
    
        assert word, word1 in verb_future

def test_get_preposition():
    # Tests the prepositons.

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_preposition()

        # Verify that the word returned from get_prepositon is
        # one of the words in the prepositions list.
        assert word in prepositions

def test_get_prepositional_phrase():
    # Tests the prepositional phrases.

    # Create the three lists of the words that make up the prepositional phrase, prepostions, determiners
    # nouns.
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    determiners = ['the', 'a', 'one', 
        'every', "some", "many"]
    nouns = ["adult", "bird", "boy", "car", "cat", 
        "child", "dog", "girl", "man", "woman", "adults", "birds", 
        "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    # Call the functions to generate the prepostional phrases for singular and plural determiners and nouns
    # and assign them a variable.
    phrase = get_prepositional_phrase(quantity=True)
    phrase1 = get_prepositional_phrase(quantity=False)

    # Split the prepositional phrase on white spaces into three words
    phrase_parts = phrase.split(' ')
    phrase_parts1 = phrase1.split(' ')

    # Assign each component/ phrase part the appropriate variable for both singular and plural determiners and
    # and the nouns as well as the prepositions
    preposition = phrase_parts[0]
    determiner = phrase_parts[1]
    noun = phrase_parts[2]

    preposition1 = phrase_parts1[0]
    determiner1 = phrase_parts1[1]
    noun1 = phrase_parts1[2]

    # Verify that the singular/ plural determiner and noun, and preposition are in the list.
    assert preposition and preposition1 in prepositions
    assert determiner and determiner1 in determiners
    assert noun and noun1 in nouns

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "week6prove_test_sentencesturingtest_Innocent.py"])