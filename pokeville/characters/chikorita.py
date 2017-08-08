from base import Pokemon

class Meganium(Pokemon):
    name = "Meganium"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180

class Bayleef(Pokemon):
    name = "Bayleef"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180
    number_of_candies_required_for_upgrade = 600
    upgrade_class = Meganium

class Chikorita(Pokemon):
    name = "Chikorita"
    initial_combat_power = 1000
    combat_power_value = 10
    fast_attack = 20
    charged_attack = 180
    number_of_candies_required_for_upgrade = 150
    upgrade_class = Bayleef