# formula for dice expressed as tuples, where (x, y) expresses xdy

# coin, d4, d6, d8, d10, d12, d20, d100 (two d10s)
DICE = [2, 4, 6, 8, 10, 12, 20, 100]
DEFAULT_LENIENCY = 1

# get leniency
try:
    leniency = int(input("What leniency? (default " + str(DEFAULT_LENIENCY) + ") "))
except ValueError:
    leniency = DEFAULT_LENIENCY

# get user input and make calculations
ideal_average = float(input("Ideal average? "))
ideal_min_max = float(input("Ideal min-max? "))
minimum_average = ideal_average - leniency
maximum_average = ideal_average + leniency

# init values
quanity_of_dice = 1
current_die = 0
best_formulas = []

# loop through quantities until too large
while quanity_of_dice <= ideal_average + leniency:
    for die in DICE:
        # sexy formula for finding mean
        mean_value = ((die / 2) + 0.5) * quanity_of_dice
        # is it good enough?
        if mean_value <= maximum_average and mean_value >= minimum_average:
            best_formulas.append(((quanity_of_dice, die), mean_value))
    quanity_of_dice += 1

# now see which formula maintains the range best
winner = None
for formula in best_formulas:
    # calculate crit score, and difference from mean (this will be same for miss so it's fine to skip it)
    # actually, it would be easier to calculate miss (just quantity_of_dice) but crits are more fun
    crit = formula[0][0] * formula[0][1]
    difference = crit - formula[1]
    # how close on target?
    distance_from_target = abs(ideal_min_max - difference)
    if winner == None or distance_from_target < winner[1]: # pylint: disable=E1136
        winner = (formula[0], distance_from_target)
winner = winner[0]

# print winner!
if winner != None:
    print(str(winner[0]) + "d" + str(winner[1]))
else:
    print("Can't find any, sorry!")
