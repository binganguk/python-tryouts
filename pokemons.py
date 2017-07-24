import random


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
        self.life -= damage
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
            print "Your {} pokemon fainted".format(self.name)


class Bulbasaur(Pokemon):
    """Bulbasaur."""

    name = "Bulbasaur"
    fast_attack = 45
    fast_attack_frequency = 0.5
    charged_attack = 70
    charged_attack_frequency = 0.1
    has_tail = False
    life = 770


class Articuno(Pokemon):
    """Articuno."""

    name = "Articuno"
    fast_attack = 70
    fast_attack_frequency = 0.5
    charged_attack = 200
    charged_attack_frequency = 0.1
    has_tail = True
    life = 500


def get_attack_damage(fast_attack, fast_attack_accuracy):
    minimal_damage = fast_attack * fast_attack_accuracy
    return random.randint(minimal_damage, fast_attack)


def auto_gym_battle():
    a = Articuno()
    b = Bulbasaur()

    while a.is_alive() == True and b.is_alive() == True:
        a_damage = get_attack_damage(a.fast_attack, a.fast_attack_accuracy)
        b_damage = get_attack_damage(b.fast_attack, b.fast_attack_accuracy)

        a.got_hit(b_damage)
        b.got_hit(a_damage)


auto_gym_battle()
