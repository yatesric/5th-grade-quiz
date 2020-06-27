import random

"""
This program sets the user quiz questions based on the 5th grade curriculum.
You can select from difficulty levels: Easier, Harder and Fiendish. To win 
you must get 3 answers correct, and you can play again multiple times.
"""

# This dictionary contains messages of encouragement based on the difficulty level selected.
encouragement = {'easier': '\nOkay, lets do some easier questions.',
                 'harder': '\nOkay, these questions are a little trickier.',
                 'fiendish': '\nWow, this will be a real test of your knowledge!' }


def main():
    print('\nWelcome to the 5th Grade quiz! This will test your general knowledge. '
          'To pass the test you must get 3 correct answers.')
    level = ask_for_level()         # Stores chosen level into the variable "level"
    introduce_level(level)
    pose_questions(level)
    play_again()


def ask_for_level():
    # Asks user to enter difficulty level, then returns the level to main.
    chosen_level = input(str('\nEnter your difficulty level: Easier, Harder or Fiendish: '))
    if chosen_level.lower() == 'easier' or 'harder' or 'fiendish':
        return chosen_level
    else:
        print('\nSorry, try entering that again.')
        ask_for_level()


def introduce_level(level):        # Prints message of encouragement from dictionary
    print(encouragement[level])


def pose_questions(level):
    # Poses the questions (based on chosen level) and keeps track of both the score and number of attempts.
    questions = load_questions(level)       # Retrieves list of questions
    answers = load_answers(level)           # Retrieves list of answers
    messages = load_messages(level)         # Retrieves list of messages
    current_score = 0
    attempt = 0
    while current_score < 3:
        # The loop returns questions until the score reaches 3.
        input('\nPress enter for next question: ')
        print('')
        list_length = len(questions)        # Calculates length of questions list
        question_choice = random.randint(0, len(questions) - 1)        # Selects a line at random
        next_question = (questions[question_choice])        # Loads question from chosen line into next_question
        print(str(attempt + 1) + '. ' + next_question)      # Prints attempt (i.e. "1.") followed by question
        answer = input(str(' '))        # User inputs their answer here
        if list_length > 2:        # Runs through the question list until only 1 is left.
            if check_answers(answers, question_choice, answer.lower()):       # Passes 3 parameters to the function
                print('')
                print(messages[question_choice])        # Prints congratulatory message for the relevant question
                current_score += 1        # Adds 1 to running score
                attempt += 1        # Adds 1 to number of attempts
                print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
            else:
                print('\nIncorrect. The answer is ' + str(answers[question_choice]) + '.')
                attempt += 1        # Adds 1 to attempts even if incorrect
                print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
            questions.pop(question_choice)      # Removes question from list once it has been asked.
            answers.pop(question_choice)        # Removes answer from list once it has been asked.
            answers.pop(question_choice + int(len(answers) / 2))    # Removes alternatively spelled answer.
            messages.pop(question_choice)                           # Removes message from list.
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


def play_again():
    # Invites user to play again. If Yes not selected, the program ends.
    play_again = input(str('\nDo you want to play again - Yes or No? '))
    if play_again.lower() == 'yes':
        main()
    else:
        print('\nThanks for playing. See you in 6th grade!')


def check_answers(answers, question_index, user_answer):
    # Checks that answer from list (answers & question_index) is same as user's inputted answer (user_answer)
    if answers[question_index].lower() == user_answer:
        return True
    elif answers[int(question_index + int(len(answers)/2))].lower() == user_answer:     # Checks alternative spelling
        return True
    else:
        return False


def load_questions(chosen_level):
    if chosen_level == 'easier':
        # Loads questions from .txt file into an empty list.
        easier_questions = []
        for line in open('easy_qs.txt'):
            question = line.strip()
            easier_questions.append(question)
        return easier_questions
    elif chosen_level == 'harder':
        # Loads questions from .txt file into an empty list.
        harder_questions = []
        for line in open('harder_qs.txt'):
            question = line.strip()
            harder_questions.append(question)
        return harder_questions
    elif chosen_level == 'fiendish':
        # Loads questions from .txt file into an empty list.
        fiendish_questions = []
        for line in open('fiendish_qs.txt'):
            question = line.strip()
            fiendish_questions.append(question)
        return fiendish_questions


def load_answers(chosen_level):
    if chosen_level == 'easier':
        # Loads easier answers from .txt file into an empty list
        easier_answers = []
        for line in open('easy_as.txt'):
            answer = line.strip()
            easier_answers.append(answer)
        return easier_answers
    elif chosen_level == 'harder':
        # Loads harder answers from .txt file into an empty list
        harder_answers = []
        for line in open('harder_as.txt'):
            answer = line.strip()
            harder_answers.append(answer)
        return harder_answers
    elif chosen_level == 'fiendish':
        # Loads answers from .txt file into an empty list.
        fiendish_answers = []
        for line in open('fiendish_as.txt'):
            answer = line.strip()
            fiendish_answers.append(answer)
        return fiendish_answers


def load_messages(chosen_level):
    if chosen_level == 'easier':
        # Loads messages from .txt file into an empty list.
        easier_message = []
        for line in open('easy_message.txt'):
            message = line.strip()
            easier_message.append(message)
        return easier_message
    elif chosen_level == 'harder':
        # Loads messages from .txt file into an empty list.
        harder_message = []
        for line in open('harder_message.txt'):
            message = line.strip()
            harder_message.append(message)
        return harder_message
    elif chosen_level == 'fiendish':
        # Loads messages from .txt file into an empty list.
        fiendish_message = []
        for line in open('fiendish_message.txt'):
            message = line.strip()
            fiendish_message.append(message)
        return fiendish_message


if __name__ == '__main__':
    main()