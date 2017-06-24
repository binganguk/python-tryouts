import random

random_number = random.randint(1, 5)

bad_guess = True

while bad_guess:
    guess = raw_input("Please, type a number between 1 and 5: ")

    if int(guess) == random_number:
        bad_guess = False
        print "Hurray! Good guess!"
    else:
        print "Try again, looser!"
