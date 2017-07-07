import datetime

print """
Hi, I am a chatbot.
Wanna talk?
Type hello to start conversation and bye to end conversation.
"""

chatbot_birth_date = datetime.date(year=2017, month=7, day=7)


user_input = None


while user_input != "bye":
    user_input = raw_input(": ")
    user_input = user_input.lower()

    if "name" in user_input:
        print "My name is Billbot Chattins."

    elif "old" in user_input or "age" in user_input:
        print "I'm {} days old".format((datetime.date.today() - chatbot_birth_date).days)

    elif "marry" in user_input:
        print "Sorry I'm already married with a hot HP computer."

    elif "hello" in user_input:
        print "Hi, what a nice day for a talk."

    
    else:
        print "This isn't in my vocabulary yet."




# print "name" in 'What is your name'
#
# sss = "What is your name"
#
# print "name" in sss
