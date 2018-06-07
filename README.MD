# RPG Damage Rollin'

You want to create a dice formula to average about x, and to have min-max values of y and z? Have I kinda got the tool for you!

Run roll.py. Fill in options so that you get a dice roll in which:

1. The mean average is within your ideal average plus or minus the leniency.
2. The furthest possible values from the average is the closest possible to your ideal min-max, given the possibilities from step 1.

For example, say I wanted a roll that averages 7 (give or take 1), where the maximum value is about 3 more than the average and the minimum value about 3 below it (so if one possible roll found in step 1 averages 7, that roll be between about 4 and 10). I would use leniency 1, ideal average 7 and ideal min-max 3.

I write dice formula in the traditional way (xdy, where x is quantity and y is number of die faces), and use 2, 4, 6, 8, 10, 12, 20, and 100 sided dice, since they're kinda the standard.

Hope this makes sense, if it doesn't I'd be happy to try to explain properly!

Oh, hey, don't want to clone this? That's cool, I put this [on repl.it](https://repl.it/@linky00/RPGDamageRollin)!
