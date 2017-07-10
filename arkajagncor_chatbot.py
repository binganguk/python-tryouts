"""
Sample chat bot.
"""

import datetime


def arkajagncor_chatbot():
    """Calls the chatbot.

    :return:
    """
    print """
    Hi, I am a chatbot.
    Wanna talk?
    Type hello to start conversation and bye to end conversation.
    """

    chatbot_birth_date = datetime.date(year=2017, month=7, day=7)


    user_input = ""


    while "bye" not in user_input:

        user_input = raw_input(": ")  # Reading user input from terminal
        user_input = user_input.lower()  # Converting the user input to lowercase
        found = False

        if "name" in user_input:
            print "My name is Billbot Chattins."
            found = True

        if "old" in user_input or "age" in user_input:
            print "I'm {} days old".format((datetime.date.today() - chatbot_birth_date).days)
            found = True

        if "marry" in user_input:
            print "Sorry I'm already married with a hot HP computer."
            found = True

        if "hello" in user_input:
            print "Hi, what a nice day for a talk."
            found = True

        if "bye" in user_input:
            print "Bye, have a nice day."
            found = True

        if "chili" in user_input:
            print "O, I don't like that because it's too hot for me."
            found = True

        if "star wars" in user_input:
            print "I have seen all the movies and I like them."
            found = True

        if "ketchup" in user_input:
            print "Oh, yummy."
            found = True

        if "swim" in user_input:
            print "Swimming could be dangerous for me."
            found = True

        if "vacation" in user_input:
            print "I am going to Hawai this year."
            found = True

        if not found:
            print "This isn't in my vocabulary yet."


if __name__ == '__main__':
    arkajagncor_chatbot()
