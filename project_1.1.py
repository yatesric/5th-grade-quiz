import random

"""
This program sets the user quiz questions based on the 5th grade curriculum.
You can select from difficulty levels: Easier, Harder and Fiendish. To win 
you must get 3 answers correct, and you can play again multiple times.
"""


def main():
    # Welcomes the user to the quiz and explains the concept.
    print('\nWelcome to the 5th Grade quiz! This will test your general knowledge. To pass the test you must get 3 correct answers.')
    ask_for_level()
    play_again()


def ask_for_level():
    # Asks user to enter difficulty level, then loads the relevent questions.
    chosen_level = input(str('\nEnter your difficulty level: Easier, Harder or Fiendish: '))
    if chosen_level.lower() == 'easier':
        questions = load_easier()
        answers = load_easier_answer()
        messages = load_easier_message()
        # The current score and number of attempts is saved throughout.
        current_score = 0
        attempt = 0
        print('\nOkay, lets do some easier questions.')
        while current_score < 3:
            # The loop returns questions until the score reaches 3.
            input('\nPress enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0,len(questions)-1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)  # Prints a randomly selected question.
            answer = input(str(' '))
            if list_length > 2:
                # Runs through the question list until only 1 is left.
                if check_answers(answers, question_choice, answer.lower()):
                    print('')
                    print(messages[question_choice])
                    current_score += 1
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                else:
                    print('\nIncorrect. The answer is ' + str(answers[question_choice]) + '.')
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                questions.pop(question_choice)  # Removes question from list once it has been asked.
                answers.pop(question_choice)  # Removes answer from list once it has been asked.
                answers.pop(question_choice + int(len(answers)/2))  # Removes alternatively spelled answer.
                messages.pop(question_choice)  # Removes message from list.
            else:
                print("\nSorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            # Prints summary of completed round.
            print('\nCONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() == 'harder':
        questions = load_harder()
        answers = load_harder_answer()
        messages = load_harder_message()
        # The current score and number of attempts is saved throughout.
        current_score = 0
        attempt = 0
        print('\nOkay, these questions are a little trickier.')
        while current_score < 3:
            # The loop returns questions until the score reaches 3.
            input('\nPress enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0,len(questions)-1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)  # Prints a randomly selected question.
            answer = input(str(' '))
            if list_length > 2:
                # Runs through the question list until only 1 is left.
                if check_answers(answers, question_choice, answer.lower()):
                    print('')
                    print(messages[question_choice])
                    current_score += 1
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                else:
                    print('\nIncorrect. The answer is ' + str(answers[question_choice]) + '.')
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                questions.pop(question_choice)  # Removes question from list once it has been asked.
                answers.pop(question_choice)  # Removes answer from list once it has been asked.
                answers.pop(question_choice + int(len(answers) / 2))  # Removes alternatively spelled answer.
                messages.pop(question_choice)  # Removes message from list.
            else:
                print("\nSorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            # Prints summary of completed round.
            print('\nCONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() == 'fiendish':
        questions = load_fiendish()
        answers = load_fiendish_answer()
        messages = load_fiendish_message()
        # The current score and number of attempts is saved throughout.
        current_score = 0
        attempt = 0
        print('\nWow, this will be a real test of your knowledge!')
        while current_score < 3:
            # The loop returns questions until the score reaches 3.
            input('\nPress enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0,len(questions)-1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)  # Prints a randomly selected question.
            answer = input(str(' '))
            if list_length > 2:
                # Runs through the question list until only 1 is left.
                if check_answers(answers, question_choice, answer.lower()):
                    print('')
                    print(messages[question_choice])
                    current_score += 1
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                else:
                    print('\nIncorrect. The answer is ' + str(answers[question_choice]) + '.')
                    attempt += 1
                    print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                questions.pop(question_choice)  # Removes question from list once it has been asked.
                answers.pop(question_choice)  # Removes answer from list once it has been asked.
                answers.pop(question_choice + int(len(answers) / 2))  # Removes alternatively spelled answer.
                messages.pop(question_choice)  # Removes message from list.
            else:
                print("\nSorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            # Prints summary of completed round.
            print('\nCONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() != 'easier' or 'harder' or 'fiendish':
        print('\nSorry, try entering that again.')
        ask_for_level()


def check_answers(answers, question_index, user_answer):
    # Checks that answer from list is same as user's inputted answer
    if answers[question_index].lower() == user_answer:
        return True
    elif answers[int(question_index + int(len(answers)/2))].lower() == user_answer:
        return True
    else:
        return False


def play_again():
    # Invites user to play again. If Yes not selected, the program ends.
    play_again = input(str('\nDo you want to play again - Yes or No? '))
    if play_again.lower() == 'yes':
        main()
    else:
        print('\nThanks for playing. See you in 6th grade!')


def load_easier():
    # Loads questions from .txt file into an empty list.
    easier_questions = []
    for line in open('easy_qs.txt'):
        question = line.strip()
        easier_questions.append(question)
    return easier_questions


def load_easier_answer():
    # Loads answers from .txt file into an empty list.
    easier_answers = []
    for line in open('easy_as.txt'):
        answer = line.strip()
        easier_answers.append(answer)
    return easier_answers


def load_easier_message():
    # Loads messages from .txt file into an empty list.
    easier_message = []
    for line in open('easy_message.txt'):
        message = line.strip()
        easier_message.append(message)
    return easier_message


def load_harder():
    # Loads questions from .txt file into an empty list.
    harder_questions = []
    for line in open('medium_qs.txt'):
        question = line.strip()
        harder_questions.append(question)
    return harder_questions


def load_harder_answer():
    # Loads answers from .txt file into an empty list.
    harder_answers = []
    for line in open('medium_as.txt'):
        answer = line.strip()
        harder_answers.append(answer)
    return harder_answers


def load_harder_message():
    # Loads messages from .txt file into an empty list.
    harder_message = []
    for line in open('medium_message.txt'):
        message = line.strip()
        harder_message.append(message)
    return harder_message


def load_fiendish():
    # Loads questions from .txt file into an empty list.
    fiendish_questions = []
    for line in open('hard_qs.txt'):
        question = line.strip()
        fiendish_questions.append(question)
    return fiendish_questions


def load_fiendish_answer():
    # Loads answers from .txt file into an empty list.
    fiendish_answers = []
    for line in open('hard_as.txt'):
        answer = line.strip()
        fiendish_answers.append(answer)
    return fiendish_answers


def load_fiendish_message():
    # Loads messages from .txt file into an empty list.
    fiendish_message = []
    for line in open('hard_message.txt'):
        message = line.strip()
        fiendish_message.append(message)
    return fiendish_message


if __name__ == '__main__':
    main()