
import random

words = [
    "walk",
    "butterfly",
    "car",
    "weather",
    "lightning",
]

words[0]


int('0') == 0
int('1') == 1
int('12') == 12

random_word = words[random.randint(0, 4)]

good_guess = False
max_number_of_attempts = 3
number_of_attempts = 0

while not good_guess and (max_number_of_attempts - number_of_attempts) > 0:
    guess = raw_input("Please say {}: ".format(", ".join(words)))

    if guess == random_word:
        good_guess = True
        print "Hurray! good guess"

    else:
        number_of_attempts += 1
        print "{} guesses left".format(max_number_of_attempts - number_of_attempts)

if not good_guess:
    print "Game over!"
