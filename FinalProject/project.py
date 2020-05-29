import random


def main():
    print('Welcome to the 5th Grade quiz! This will test your general knowledge. To pass the test you must get 3 correct answers.')
    ask_for_level()
    play_again()


def ask_for_level():
    chosen_level = input(str('Enter your difficulty level: Easier, Harder or Fiendish: '))
    if chosen_level.lower() == 'easier':
        questions = load_easier()
        current_score = 0
        attempt = 0
        print('Okay, lets do some easier questions.')
        while current_score < 3:
            input('Press enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0,len(questions)-1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)
            questions.pop(question_choice)
            answer = input(str(' '))
            if list_length > 2:
                if next_question.startswith('Which homonym'):
                    if answer.lower() == 'mousse':
                        print("Correct! You wouldn't want to eat a moose.")
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is mousse.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Who was the'):
                    if answer.lower() == 'george washington':
                        print('Correct! George Washington was inaugurated in April 1789.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is George Washington.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('If your tea'):
                    if answer.lower() == 'false':
                        print('Correct! Have a cup on me.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is False.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Yellow is a'):
                    if answer.lower() == 'false':
                        print('Correct! Yellow is made by mixing the primary colors red and green.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is False.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What is 6'):
                    if answer == '54':
                        print('Correct! You are a multiplication whizz.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 54.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What continent'):
                    if answer.lower() == 'asia':
                        print('Correct! Did you know Russia and Turkey are in both Europe and Asia?')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is Asia.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Add a suffix'):
                    if answer.lower() == 'helpful':
                        print('Correct! That was helpful to your score!')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is "helpful".')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Which of these'):
                    if answer.lower() == 'texas':
                        print('Correct! Everything is big down in Texas, apparently.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is Texas.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Which plant'):
                    if answer.lower() == 'cactus':
                        print("Correct! Just don't touch any.")
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'a cactus':
                        print("Correct! Just don't touch any.")
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is a cactus.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('To send an'):
                    if answer == '@':
                        print('Correct! Every email address should have an @ symbol.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is @')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
            else:
                print("Sorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            print('CONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() == 'harder':
        questions = load_harder()
        current_score = 0
        attempt = 0
        print('Okay, these questions are a little trickier.')
        while current_score < 3:
            input('Press enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0, len(questions) - 1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)
            questions.pop(question_choice)
            answer = input(str(' '))
            if list_length > 2:
                if next_question.startswith('In what year'):
                    if answer == '1976':
                        print('Correct! It was 200 years since the Declaration of Independence in 1776.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 1976.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What country'):
                    if answer.lower() == 'india':
                        print('Correct! There are over 1 billion Hindus in India.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is India.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Is a dolphin'):
                    if answer.lower() == 'mammal':
                        print('Correct! Dolphins are one of the smartest animals on the planet.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'a mammal':
                        print('Correct! Dolphins are one of the smartest animals on the planet.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is a mammal.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Above what'):
                    if answer == '100':
                        print('Correct! By the way, 100°C is 212°F.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 100.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('How many quarters'):
                    if answer == '17':
                        print('Correct! Congratulations, you are rich.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == '17 quarters':
                        print('Correct! Congratulations, you are rich.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 17.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith("When it's summer"):
                    if answer.lower() == 'winter':
                        print('Correct! In the southern hemisphere, the seasons are opposite.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is winter.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Which dictionary'):
                    if answer == 'minute':
                        print("Correct! I hope you didn't check your dictionary...")
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is minute.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Name the time'):
                    if answer.lower() == 'ice age':
                        print('Correct! Life was pretty cold back then.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'the ice age':
                        print('Correct! Life was pretty cold back then.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is The Ice Age.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What layer of'):
                    if answer.lower() == 'ozone':
                        print('Correct! There are big holes in the ozone layer above Australia, for example.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'ozone layer':
                        print('Correct! There are big holes in the ozone layer above Australia, for example.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'the ozone layer':
                        print('Correct! There are big holes in the ozone layer above Australia, for example.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is the Ozone layer.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith("If you're a"):
                    if answer.lower() == '2':
                        print('Correct! "Bi" is the Latin word for two of something.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'two':
                        print('Correct! "Bi" is the Latin word for two of something.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 2.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
            else:
                print("Sorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            print('CONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() == 'fiendish':
        questions = load_fiendish()
        current_score = 0
        attempt = 0
        print('Wow, this will be a real test of your knowledge!')
        while current_score < 3:
            input('Press enter for next question: ')
            print('')
            list_length = len(questions)
            question_choice = random.randint(0, len(questions) - 1)
            next_question = (questions[question_choice])
            print(str(attempt + 1) + '. ' + next_question)
            questions.pop(question_choice)
            answer = input(str(' '))
            if list_length > 2:
                if next_question.startswith('Who was the'):
                    if answer.lower() == 'jefferson davis':
                        print('Correct! After the Civil War he was jailed for two years.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is Jefferson Davis.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('In what language'):
                    if answer.lower() == 'hebrew':
                        print('Correct! Hebrew is the official language of Israel.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is Hebrew.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What money is'):
                    if answer.lower() == 'euro':
                        print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'euros':
                        print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'the euro':
                        print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is the Euro.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Name the process'):
                    if answer.lower() == 'condensation':
                        print('Correct! On a cold day, you can see condensation on a glass window.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is condensation.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('A rectangular room'):
                    if answer.lower() == '58.5':
                        print('Correct! You are a multiplication genius.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is 58.5.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What man-made'):
                    if answer.lower() == 'the panama canal':
                        print('Correct! The Panama canal was completed in 1881.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    elif answer.lower() == 'panama canal':
                        print('Correct! The Panama canal was completed in 1881.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is the Panama Canal.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('Make this an'):
                    if answer.lower() == 'is the well dry?':
                        print('Correct! Good interrogation.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is: Is the well dry?')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What Roman leader'):
                    if answer.lower() == 'julius caesar':
                        print('Correct! He was quite good at conquering.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is Julius Caesar.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('What gas makes'):
                    if answer.lower() == 'nitrogen':
                        print('Correct! Nitrogen forms 78% of our atmosphere.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is nitrogen.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                elif next_question.startswith('On what continent'):
                    if answer.lower() == 'south america':
                        print('Correct! Potatoes were first domesticated in Peru over 7,000 years ago.')
                        current_score += 1
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
                    else:
                        print('Incorrect. The answer is South America.')
                        attempt += 1
                        print('Your score is ' + str(current_score) + ' out of ' + str(attempt) + '.')
            else:
                print("Sorry, you have run out of attempts. Let's play again...")
                input(' ')
                break
        if current_score == 3:
            print('CONGRATS! You have reached 3 correct answers.')
            percentage = (float(current_score) / float(attempt)) * 100
            print('Your official score is ' + str(percentage) + '%')
        else:
            print('')
    elif chosen_level.lower() != 'easier' or 'harder' or 'fiendish':
        print('Sorry, try entering that again.')
        ask_for_level()


def play_again():
    play_again = input(str('Do you want to play again - Yes or No? '))
    if play_again.lower() == 'yes':
        main()
    else:
        print('Thanks for playing. See you in 6th grade!')




def load_easier():
    easier_questions = []
    for line in open('easy_qs.txt'):
        question = line.strip()
        easier_questions.append(question)
    return easier_questions

def load_harder():
    harder_questions = []
    for line in open('medium_qs.txt'):
        question = line.strip()
        harder_questions.append(question)
    return harder_questions

def load_fiendish():
    fiendish_questions = []
    for line in open('hard_qs.txt'):
        question = line.strip()
        fiendish_questions.append(question)
    return fiendish_questions


if __name__ == '__main__':
    main()

