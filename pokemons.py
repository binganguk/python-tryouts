# -*- coding: utf-8 -*-

import random
from time import sleep


RIP = """
            ___________
            |         |
            |  R.I.P. |
            |         |
            |         |
            |         |
            |         |
            |         |
            |_________|
"""


TROPHY = """
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`

"""

class Pokemon(object):
    """Base class for pokemon's classification."""

    name = None
    fast_attack = None
    fast_attack_frequency = None  # Per second
    fast_attack_accuracy = 0.8
    charged_attack = None
    charged_attack_frequency = None  # Per second
    has_tail = False
    life = None

    def got_hit(self, damage):
        if self.life > 0:
            self.life -= damage
            print "{} got {} damage (life left {})".format(self.name, damage, self.life)
            self.status()

    def is_alive(self):
        if self.life <= 0:
            return False
        return True

    def heal(self, life):
        self.life += life

    def __repr__(self):
        return str(self.__dict__)

    def status(self):
        if not self.is_alive():
            print "\n † {} fainted\n".format(self.name)


class Articuno(Pokemon):
    """Articuno."""

    name = "Articuno"
    fast_attack = 101
    fast_attack_frequency = 0.5
    fast_attack_accuracy = 0.8
    charged_attack = 200
    charged_attack_frequency = 0.1
    has_tail = True
    life = 900


class Bulbasaur(Pokemon):
    """Bulbasaur."""

    name = "Bulbasaur"
    fast_attack = 45
    fast_attack_frequency = 0.5
    charged_attack = 70
    charged_attack_frequency = 0.1
    has_tail = False
    life = 1250


class Cyndaquil(Pokemon):
    """Cyndaquil."""

    name = "Cyndaquil"
    fast_attack = 200
    fast_attack_frequency = 0.5
    fast_attack_accuracy = 0.5
    charged_attack = 70
    charged_attack_frequency = 0.1
    has_tail = False
    life = 655


def get_attack_damage(fast_attack, fast_attack_accuracy):
    minimal_damage = int(fast_attack * fast_attack_accuracy)
    return random.randint(minimal_damage, fast_attack)


def auto_gym_battle():
    a = Articuno()
    b = Bulbasaur()
    c = Cyndaquil()

    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBattle starts\n\n\n"

    counter = 1

    while (
        (a.is_alive() == True and b.is_alive() == True)
        or (a.is_alive() == True and c.is_alive() == True)
        or (b.is_alive() == True and c.is_alive() == True)
    ):
        print "\nRound {}\n".format(counter)

        a_damage = get_attack_damage(a.fast_attack, a.fast_attack_accuracy)
        b_damage = get_attack_damage(b.fast_attack, b.fast_attack_accuracy)
        c_damage = get_attack_damage(c.fast_attack, c.fast_attack_accuracy)

        a.got_hit(b_damage + c_damage)
        b.got_hit(a_damage + c_damage)
        c.got_hit(a_damage + b_damage)

        counter += 1

        sleep(1)

    if a.is_alive() == True or b.is_alive() == True or c.is_alive() == True:
        print "===============================================\n"

        if a.is_alive() == True:
            print "The winner is {}".format(a.name)

        if b.is_alive() == True:
            print "The winner is {}".format(b.name)

        if c.is_alive() == True:
            print "The winner is {}".format(c.name)

        print TROPHY

    else:
        print "===============================================\n"
        print "Everyone died"
        print RIP


auto_gym_battle()
