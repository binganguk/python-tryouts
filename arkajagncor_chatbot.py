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
    print user_input
    # UPPERCASE
    # lowercase
    # "Hello, my name is Artur".lower() == "hello, my name is artur"
    if "name" in user_input:
        print "My name is Billbot Chattins."

    if "old" in user_input or "age" in user_input:
        print "I'm {} days old".format((datetime.date.today() - chatbot_birth_date).days)

    if "marry" in user_input:
        print "Sorry I'm already married with a hot HP computer."

    if "hello" in user_input:
        print "Hi, what a nice day for a talk."

    if "bye" in user_input:
        print "Bye, have a nice day."
        break

    else:
        print "This isn't in my vocabulary yet."




# print "name" in 'What is your name'
#
# sss = "What is your name"
#
# print "name" in sss



