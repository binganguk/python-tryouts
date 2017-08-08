from .base import Pokemon


class Venusaur(Pokemon):
    name = "Venusaur"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180


class Ivysaur(Pokemon):
    name = "Ivysaur"
    initial_combat_power = 100
    combat_power_value = 10
    fast_attack = 15
    charged_attack = 70
    number_of_candies_required_for_upgrade = 600
    upgrade_class = Venusaur


class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    initial_combat_power = 10
    combat_power_value = 10
    fast_attack = 12
    charged_attack = 55
    number_of_candies_required_for_upgrade = 150
    upgrade_class = Ivysaur
