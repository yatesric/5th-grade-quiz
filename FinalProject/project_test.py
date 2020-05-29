import random

# the name of the file to read in!



def main():
    questions = load_questions()
    current_score = 0
    while current_score < 5:
        input('Press enter for next question: ')
        print('')
        next_question = random.sample(questions, 1)
        print(next_question)
        answer = input(str(' '))
        if next_question.startswith('Which homonym'):
            if answer.lower() == 'mousse':
                print("Correct! You wouldn't want to eat a moose.")
                current_score += 1
            else: print('Incorrect. The answer is mousse.')
        elif next_question.startswith('Who was the first'):
            if answer.lower() == 'george washington':
                print('Correct! George Washington was inaugurated in April 1789.')
                current_score += 1
            else: print('Incorrect. The answer is George Washington.')
        elif next_question.startswith("If your tea"):
            if answer.lower() == 'false':
                print('Correct! Have a cup on me.')
                current_score += 1
            else: print('Incorrect. The answer is False.')
        elif next_question.startswith("Yellow"):
            if answer.lower() == 'false':
                print('Correct! Yellow is made by mixing the primary colors red and green.')
                current_score += 1
            else: print('Incorrect. The answer is False.')
        elif next_question.startswith("What is 6"):
            if answer == '54':
                print('Correct! You are a multiplication whizz.')
                current_score += 1
            else: print('Incorrect. The answer is 54.')
        elif next_question.startswith("What continent"):
            if answer.lower() == 'asia':
                print('Correct! Did you know Russia and Turkey are in both Europe and Asia?')
                current_score += 1
            else: print('Incorrect. The answer is Asia.')
        elif next_question.startswith("Add a suffix"):
            if answer.lower() == 'helpful':
                print('Correct! That was helpful to your score!')
                current_score += 1
            else: print('Incorrect. The answer is "helpful".')
        elif next_question.startswith("Which of these US"):
            if answer.lower() == 'texas':
                print('Correct! Everything is big down in Texas, apparently.')
                current_score += 1
            else: print('Incorrect. The answer is Texas.')
        elif next_question.startswith("Which plant"):
            if 'cactus'.lower() in answer:
                print("Correct! Just don't touch any.")
                current_score += 1
            elif answer.lower() == 'a cactus':
                print("Correct! Just don't touch any.")
                current_score += 1
            else: print('Incorrect. The answer is a cactus.')
        elif next_question.startswith("To send"):
            if answer == '@':
                print('Correct! Every email address should have an @ symbol.')
                current_score += 1
            else: print('Incorrect. The answer is @')
        elif next_question.startswith("['11."):
            if answer == '1976':
                print('Correct! It was 200 years since the Declaration of Independence in 1776.')
                current_score += 1
            else: print('Incorrect. The answer is 1976.')
        elif next_question.startswith("['12."):
            if answer.lower() == 'india':
                print('Correct! There are over 1 billion Hindus in India.')
                current_score += 1
            else: print('Incorrect. The answer is India')
        elif next_question.startswith("['13."):
            if answer.lower() == 'mammal':
                print('Correct! Dolphins are one of the smartest animals on the planet.')
                current_score += 1
            elif answer.lower() == 'a mammal':
                print('Correct! Dolphins are one of the smartest animals on the planet.')
                current_score += 1
            else: print('Incorrect. The answer is a mammal.')
        elif next_question.startswith("['14."):
            if answer == '100':
                print('Correct! By the way, 100°C is 212°F.')
                current_score += 1
            else: print('Incorrect. The answer is 100.')
        elif next_question.startswith("['15."):
            if answer == '17':
                print('Correct! Congratulations, you are rich.')
                current_score += 1
            else: print('Incorrect. The answer is 17.')
        elif next_question.startswith("['16."):
            if answer.lower() == 'winter':
                print('Correct! In the southern hemisphere, the seasons are opposite.')
                current_score += 1
            else: print('Incorrect. The answer is winter.')
        elif next_question.startswith("['17."):
            if answer == 'minute':
                print("Correct! I hope you didn't check your dictionary...")
                current_score += 1
            else: print('Incorrect. The answer is minute.')
        elif next_question.startswith("['18."):
            if answer.lower() == 'ice age':
                print('Correct! Life was pretty cold back then.')
                current_score += 1
            elif answer.lower() == 'the ice age':
                print('Correct! Life was pretty cold back then.')
                current_score += 1
            else: print('Incorrect. The answer is The Ice Age.')
        elif next_question.startswith("['19."):
            if answer.lower() == 'ozone':
                print('Correct! There are big holes in the ozone layer above Australia, for example.')
                current_score += 1
            elif answer.lower() == 'ozone layer':
                print('Correct! There are big holes in the ozone layer above Australia, for example.')
                current_score += 1
            elif answer.lower() == 'the ozone layer':
                print('Correct! There are big holes in the ozone layer above Australia, for example.')
                current_score += 1
            else: print('Incorrect. The answer is the Ozone layer.')
        elif next_question.startswith("['20."):
            if answer.lower() == '2':
                print('Correct! "Bi" is the Latin word for two of something.')
                current_score += 1
            elif answer.lower() == 'two':
                print('Correct! "Bi" is the Latin word for two of something.')
                current_score += 1
            else: print('Incorrect. The answer is 2.')
        elif next_question.startswith("['21."):
            if answer.lower() == 'jefferson davis':
                print('Correct! After the Civil War he was jailed for two years.')
                current_score += 1
            else: print('Incorrect. The answer is Jefferson Davis.')
        elif next_question.startswith("['22."):
            if answer.lower() == 'hebrew':
                print('Correct! Hebrew is the official language of Israel.')
                current_score += 1
            else: print('Incorrect. The answer is Hebrew.')
        elif next_question.startswith("['23."):
            if answer.lower() == 'euro':
                print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                current_score += 1
            elif answer.lower() == 'euros':
                print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                current_score += 1
            elif answer.lower() == 'the euro':
                print('Correct! There are 19 countries in the "Eurozone"; each uses the same currency.')
                current_score += 1
            else: print('Incorrect. The answer is the Euro.')
        elif next_question.startswith("['24."):
            if answer.lower() == 'condensation':
                print('Correct! On a cold day, you can see condensation on a glass window.')
                current_score += 1
            else: print('Incorrect. The answer is condensation.')
        elif next_question.startswith("['25."):
            if answer.lower() == '58.5':
                print('Correct! You are a multiplication genius.')
                current_score += 1
            else: print('Incorrect. The answer is 58.5.')
        elif next_question.startswith("['26."):
            if answer.lower() == 'the panama canal':
                print('Correct! The Panama canal was completed in 1881.')
                current_score += 1
            elif answer.lower() == 'panama canal':
                print('Correct! The Panama canal was completed in 1881.')
                current_score += 1
            else: print('Incorrect. The answer is the Panama Canal.')
        elif next_question.startswith("['27."):
            if answer.lower() == 'Is the well dry?':
                print('Correct! Good interrogation.')
                current_score += 1
            else: print('Incorrect. The answer is Julius Caesar.')
        elif next_question.startswith("['28."):
            if answer.lower() == 'julius caesar':
                print('Correct! He was quite good at conquering.')
                current_score += 1
            else: print('Incorrect. The answer is Julius Caesar.')
        elif next_question.startswith("['29."):
            if answer.lower() == 'nitrogen':
                print('Correct! Nitrogen forms 78% of our atmosphere.')
                current_score += 1
            else: print('Incorrect. The answer is nitrogen.')
        elif next_question.startswith("['30."):
            if answer.lower() == 'south america':
                print('Correct! Potatoes were first domesticated in Peru over 7,000 years ago.')
                current_score += 1
            else: print('Incorrect. The answer is South America.')
    print('CONGRATS! You have answered 5 questions correctly. ')

def load_questions():
    questions = []
    for line in open('sample_qs.txt'):
        question = line.strip()
        questions.append(question)
    return questions

if __name__ == '__main__':
    main()

