# Start by creating lists to use in the function
strongly_disagree = []
disagree = []
agree = []
strongly_agree = []

def main():
    '''This program is an implementation of the Rosenberg Self-Esteem Scale.\
    This program will show you ten statements that you could possibly\
    apply to yourself. Please rate how much you agree with each of the\
    statements by responding with one of these four letters:\
    D means you strongly disagree with the statement.\
    d means you disagree with the statement.\
    a means you agree with the statement.\
    A means you strongly agree with the statement.'''

    print('This program is an implementation of the Rosenberg Self-Esteem Scale.\
    This program will show you ten statements that you could possibly\
    apply to yourself. Please rate how much you agree with each of the\
    statements by responding with one of these four letters:\
    D means you strongly disagree with the statement.\
    d means you disagree with the statement.\
    a means you agree with the statement.\
    A means you strongly agree with the statement.')

    # Present the statements and assign the appropriate score depending on the statement type
    question_1 = input('1. I feel that I am a person of worth, at least on an equal plane with others. Enter D, d, a, or A: ')
    if question_1 == 'D':
        score = 0
        strongly_disagree.append(score)
    elif question_1 == 'd':
        score = 1
        disagree.append(score)
    elif question_1 == 'a':
        score = 2
        agree.append(score)
    elif question_1 == 'A':
        score = 3
        strongly_agree.append(score)
    
    question_2 = input('2. I feel that I have a number of good qualities. Enter D, d, a, or A: ')
    if question_2 == 'D':
        score = 0
        strongly_disagree.append(score)
    elif question_2 == 'd':
        score = 1
        disagree.append(score)
    elif question_2 == 'a':
        score = 2
        agree.append(score)
    elif question_2 == 'A':
        score = 3
        strongly_agree.append(score)
    
    question_3 = input('3. All in all, I am inclined to feel that I am a failure. Enter D, d, a, or A: ')
    if question_3 == 'D':
        score = 3
        strongly_disagree.append(score)
    elif question_3 == 'd':
        score = 2
        disagree.append(score)
    elif question_3 == 'a':
        score = 1
        agree.append(score)
    elif question_3 == 'A':
        score = 0
        strongly_agree.append(score)

    question_4 = input('4. I am able to do things as well as most other people. Enter D, d, a, or A: ')
    if question_4 == 'D':
        score = 0
        strongly_disagree.append(score)
    elif question_4 == 'd':
        score = 1
        disagree.append(score)
    elif question_4 == 'a':
        score = 2
        agree.append(score)
    elif question_4 == 'A':
        score = 3
        strongly_agree.append(score)
    
    question_5 = input('5. I feel I do not have much to be proud of. Enter D, d, a, or A: ')
    if question_5 == 'D':
        score = 3
        strongly_disagree.append(score)
    elif question_5 == 'd':
        score = 2
        disagree.append(score)
    elif question_5 == 'a':
        score = 1
        agree.append(score)
    elif question_5 == 'A':
        score = 0
        strongly_agree.append(score)
    
    question_6 = input('6. I take a positive attitude toward myself. Enter D, d, a, or A: ')
    if question_6 == 'D':
        score = 0
        strongly_disagree.append(score)
    elif question_6 == 'd':
        score = 1
        disagree.append(score)
    elif question_6 == 'a':
        score = 2
        agree.append(score)
    elif question_6 == 'A':
        score = 3
        strongly_agree.append(score)
    
    question_7 = input('7. On the whole, I am satisfied with myself. Enter D, d, a, or A: ')
    if question_7 == 'D':
        score = 0
        strongly_disagree.append(score)
    elif question_7 == 'd':
        score = 1
        disagree.append(score)
    elif question_7 == 'a':
        score = 2
        agree.append(score)
    elif question_7 == 'A':
        score = 3
        strongly_agree.append(score)
    
    question_8 = input('8. I wish I could have more respect for myself. Enter D, d, a, or A: ')
    if question_8 == 'D':
        score = 3
        strongly_disagree.append(score)
    elif question_8 == 'd':
        score = 2
        disagree.append(score)
    elif question_8 == 'a':
        score = 1
        agree.append(score)
    elif question_8 == 'A':
        score = 0
        strongly_agree.append(score)
    
    question_9 = input('9. I certainly feel useless at times. Enter D, d, a, or A: ')
    if question_9 == 'D':
        score = 3
        strongly_disagree.append(score)
    elif question_9 == 'd':
        score = 2
        disagree.append(score)
    elif question_9 == 'a':
        score = 1
        agree.append(score)
    elif question_9 == 'A':
        score = 0
        strongly_agree.append(score)
    
    question_10 = input('10. At times I think I am no good at all. Enter D, d, a, or A: ')
    if question_10 == 'D':
        score = 3
        strongly_disagree.append(score)
    elif question_10 == 'd':
        score = 2
        disagree.append(score)
    elif question_10 == 'a':
        score = 1
        agree.append(score)
    elif question_10 == 'A':
        score = 0
        strongly_agree.append(score)
    
    # Sum the total score from the four lists and print the result
    total_score = sum(strongly_disagree + disagree + agree + strongly_agree)
    print(f'Your self-esteem score is {total_score}.\nA score below 15 may indicate problematic low self-esteem.')
    
main()