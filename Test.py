# Made by Jordan Leich on 6/3/2020

import random
import time

score = 0


def results():
    global score
    print('Your final score is: ' + str(score))
    print()
    time.sleep(2)
    again = input('Would you like to take the math test again (yes or no): ')
    print()
    time.sleep(2)
    if again == 'yes':
        print('Your final score will be kept... Restarting test...')
        print()
        time.sleep(2)
        test()

    elif again == 'no':
        print('Quiting test...')
        print()
        time.sleep(2)
        quit()

    else:
        print('Invalid input...')
        print()
        time.sleep(2)
        print('Quiting test...')
        print()
        time.sleep(2)
        quit()


def test():
    global score
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    addition_user = input('What is ' + str(first_number) + ' + ' + str(second_number) + ': ')
    print()
    time.sleep(2)
    addition_user = eval(addition_user)
    addition_correct = int(first_number + second_number)

    if addition_user == addition_correct:
        print('Correct!')
        print()
        score += 1
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    else:
        print('Incorrect!')
        print()
        time.sleep(2)
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    subtract_user = input('What is ' + str(first_number) + ' - ' + str(second_number) + ': ')
    print()
    time.sleep(2)
    subtract_user = eval(subtract_user)
    subtract_correct = int(first_number - second_number)

    if subtract_user == subtract_correct:
        print('Correct!')
        print()
        score += 1
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    else:
        print('Incorrect!')
        print()
        time.sleep(2)
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    multiply_user = input('What is ' + str(first_number) + ' * ' + str(second_number) + ': ')
    print()
    time.sleep(2)
    multiply_user = eval(multiply_user)
    multiply_correct = int(first_number * second_number)

    if multiply_user == multiply_correct:
        print('Correct!')
        print()
        score += 1
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    else:
        print('Incorrect!')
        print()
        time.sleep(2)
        print('Your score is: ' + str(score))
        print()
        time.sleep(2)

    divide_user = input('What is ' + str(first_number) + ' / ' + str(second_number) + ': ')
    print()
    time.sleep(2)
    divide_user = eval(divide_user)
    divide_correct = int(first_number / second_number)

    if divide_user == divide_correct:
        print('Correct!')
        print()
        score += 1
        time.sleep(2)
        results()

    else:
        print('Incorrect!')
        print()
        time.sleep(2)
        results()


def main():
    test()


main()
