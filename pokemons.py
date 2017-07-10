class Pokemon(object):
    """Base class for pokemon's classification."""

    name = None
    fast_attack = None
    fast_attack_frequency = None  # Per second
    charged_attack = None
    charged_attack_frequecy = None  # Per second
    has_tail = False
    life = None

    def got_hit(self, damage):
        self.life -= damage
        self.is_alive()

    def is_alive(self):
        if self.life < 0:
            print "Your {} pokemon fainted".format(self.name)


class Bulbasaur(Pokemon):
    """Bulbasaur."""

    name = "Bulbasaur"
    fast_attack = 15
    fast_attack_frequency = 0.5
    charged_attack = 70
    charged_attack_frequecy = 0.1
    has_tail = False
    life = 70


class Articuno(Pokemon):
    """Articuno."""

    name = "Articuno"
    fast_attack = 70
    fast_attack_frequency = 0.5
    charged_attack = 200
    charged_attack_frequecy = 0.1
    has_tail = True
    life = 500


b = Bulbasaur()
a = Articuno()


