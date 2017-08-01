def minus(initial_value, decrease, minimal_value):
    while initial_value >= minimal_value:
        initial_value -= decrease

    return initial_value

print minus(1000, 3, 4)

print minus(667, 3.5, 4.5)
