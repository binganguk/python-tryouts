"""
Sample chat bot.
"""

import datetime

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

    if not found:
        print "This isn't in my vocabulary yet."
