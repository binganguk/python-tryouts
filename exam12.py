"""
There are two wizards:

    YellowWizard (Yellow wizard)
    BlackWizard (Black wizard)

Both wizards can say "boo!".

Both wizards can say something about their beards. Like:

    Hello, I'm the ... (the name of the wizard). Colour of my beard is ... (colour of the beard).

Both wizards can make potions.

You should tell your wizard what kind of potion shall it be.

There are two sorts of potions:

    HealingPotion (Healing potion)
    PoisoningPotion (Poisoning potion)

Both wizards have beards. The colour of the beard of the Yellow wizard is red. The colour of the beard of the
Black wizard is blue.

Make two wizard classes and let both wizards prepare potions. Each of the wizards shall also say "boo".
Make two potions classes.
"""


class Potion(object):
    sort_of_potion = None


class PoisoningPotion(Potion):
        sort_of_potion = "poisoning potion"


class HealingPotion(Potion):
    sort_of_potion = "healing potion"


class Wizard(object):
    name = None
    beard_color = None

    def say_boo(self):
        print "boo"

    def make_potion(self, sort_of_potion):
        if sort_of_potion == "poisoning potion":
            return PoisoningPotion()
        elif sort_of_potion == "healing potion":
            return HealingPotion()

    def talk_about_beard(self):
        print "Hello, I'm the {0}. Colour of my beard is {1}.".format(self.name, self.beard_color)


class YellowWizard(Wizard):
    name = "Yellow Wizard"
    beard_color = "red"


class BlackWizard(Wizard):
    name = "Black Wizard"
    beard_color = "blue"



y = YellowWizard()
print y.make_potion("poisoning potion")
print y.make_potion("healing potion")
y.say_boo()
y.talk_about_beard()

b = BlackWizard()
print b.make_potion("poisoning potion")
print b.make_potion("healing potion")
b.say_boo()
b.talk_about_beard()