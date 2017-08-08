from .base import Pokemon


class Charizard(Pokemon):
    name = "Charizard"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180


class Charmeleon(Pokemon):
    name = "Charmeleon"
    initial_combat_power = 100
    combat_power_value = 10
    fast_attack = 15
    charged_attack = 70
    number_of_candies_required_for_upgrade = 600
    upgrade_class = Charizard


class Charmander(Pokemon):
    name = "Charmander"
    initial_combat_power = 10
    combat_power_value = 10
    fast_attack = 12
    charged_attack = 55
    number_of_candies_required_for_upgrade = 150
    upgrade_class = Charmeleon
