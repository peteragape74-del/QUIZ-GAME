#PYTHON CODE FOR THE QUIZ GAME

import random
round_score = 0
question1 = ['Question 1: Which planet is known as the Red Planet?', 'A. Venus', 'B. Mars', 'C. Jupiter', 'D. Mercury']        
question2 = ['Question 2: How many sides does a hexagon have?', 'A. Five', 'B. Six', 'C. Seven', 'D. Eight']
question3 = ['Question 3: Which language is primarily used to style web pages?', 'A. HTML', 'B. Python', 'C. CSS', 'D. SQL']
question4 = ['Question 4: What is 9 multiplied by 7?', 'A. 56', 'B. 63', 'C. 72', 'D. 79']
question5 = ['Question 5: Which gas do plants absorb from the atmosphere?', 'A. Oxygen', 'B. Nitrogen', 'C. Carbon dioxide', 'D. Hydrogen']
question6 = ['Question 6: What is the capital of Japan?', 'A. Seoul', 'B. Tokyo', 'C. Beijing', 'D. Bangkok']

print(' __________________________')
print('===GENERAL KNOWLEDGE QUIZ===')
print('============================')
while True:
    print("1. Play quiz")
    print("2. View instructions")
    print("3. View score")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        print('choose your answer from options(A-D)')
        print(' ')
        for question in question1:
            print(question)
        question1ans = input('Your answer(A-D): ')
        if question1ans == 'B':
            round_score += 1
        else:
            round_score += 0
        for question in question2:
            print(question)
        question2ans = input('Your answer(A-D): ')
        if question2ans == 'B':
            round_score += 1
        else:
            round_score += 0 
        for question in question3:
            print(question)
        question3ans = input('Your answer(A-D): ')
        if question3ans == 'C':
            round_score += 1
        else:
            round_score += 0
        for question in question4:
            print(question)
        question4ans = input('Your answer(A-D): ')
        if question4ans == 'B':
            round_score += 1
        else:
            round_score += 0
        for question in question5:
            print(question)
        question5ans = input('Your answer(A-D): ')
        if question5ans == 'C':
            round_score += 1
        else:
            round_score += 0
        for question in question6:
            print(question)
        question6ans = input('Your answer(A-D): ')
        if question6ans == 'B':
            round_score += 1
        else:
            round_score += 0
        print('Quiz complete. You scored', round_score, 'out of 6 questions')
        print('===========')
        print('Corrections')
        print('===========')
        if question1ans != 'B':
            print('Question 1: B')
        if question2ans != 'B':
            print('Question 2: B')
        if question3ans != 'C':
            print('Question 3: C')
        if question4ans != 'B':
            print('Question 4: B')
        if question5ans != 'C':
            print('Question 4: C')
        if question6ans != 'B':
            print('Question 5: B')
    
        
    elif choice == '2':
        print('============')
        print("Instructions")
        print('============')
        print("Choose Play from the menu to start a six-question quiz.")
        print("Enter A, B, C, or D for each answer. Each correct answer is worth one point.")
        print("Your score is saved for this session and can be viewed from the menu.")
    elif choice == '3':
        print('Your score is', round_score)
    elif choice == '4':
        print('Goodbye')
        break
