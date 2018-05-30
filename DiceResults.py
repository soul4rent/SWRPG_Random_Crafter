import random


#The following functions simulate a FFG star wars dice roll.
#There are six die, with their results represented as a dictionary
def getGreenDice():
    die = [{'succ': 0, 'adv': 0}, \
           {'succ': 1, 'adv': 0}, \
           {'succ': 1, 'adv': 0}, \
           {'succ': 2, 'adv': 0}, \
           {'succ': 0, 'adv': 1}, \
           {'succ': 0, 'adv': 1}, \
           {'succ': 1, 'adv': 1}, \
           {'succ': 0, 'adv': 2}]
    return random.choice(die)

def getYellowDice():
    die = [{'succ': 0, 'adv': 0}, \
           {'succ': 1, 'adv': 0}, \
           {'succ': 1, 'adv': 0}, \
           {'succ': 2, 'adv': 0}, \
           {'succ': 2, 'adv': 0}, \
           {'succ': 0, 'adv': 1}, \
           {'succ': 1, 'adv': 1}, \
           {'succ': 1, 'adv': 1}, \
           {'succ': 1, 'adv': 1}, \
           {'succ': 1, 'adv': 2}, \
           {'succ': 1, 'adv': 2}, \
           {'succ': 1, 'adv': -1}] #used to represent triumph
    return random.choice(die)

def getBlueDice():
    die = [{'succ': 0, 'adv': 0}, \
           {'succ': 0, 'adv': 0}, \
           {'succ': 0, 'adv': 2}, \
           {'succ': 0, 'adv': 1}, \
           {'succ': 1, 'adv': 1}, \
           {'succ': 1, 'adv': 0}]
    return random.choice(die)

def getPurpleDice():
    die = [{'fail': 0, 'dis': 0}, \
           {'fail': 1, 'dis': 0}, \
           {'fail': 2, 'dis': 0}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 0, 'dis': 2}, \
           {'fail': 1, 'dis': 1}]
    return random.choice(die)

def getRedDice():
    die = [{'fail': 0, 'dis': 0}, \
           {'fail': 1, 'dis': 0}, \
           {'fail': 1, 'dis': 0}, \
           {'fail': 2, 'dis': 0}, \
           {'fail': 2, 'dis': 0}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 1, 'dis': 1}, \
           {'fail': 1, 'dis': 1}, \
           {'fail': 0, 'dis': 2}, \
           {'fail': 0, 'dis': 2}, \
           {'fail': 1, 'dis': -1}] #used to represent dispair
    return random.choice(die)

def getBlackDice():
    die = [{'fail': 0, 'dis': 0}, \
           {'fail': 0, 'dis': 0}, \
           {'fail': 1, 'dis': 0}, \
           {'fail': 1, 'dis': 0}, \
           {'fail': 0, 'dis': 1}, \
           {'fail': 0, 'dis': 1}]
    return random.choice(die)



def roll(blue, green, yellow, black, purple, red):

    #success, advantage, triumph, fail, disadvantage, dispair
    total_roll = {'s': 0, 'a': 0, 't': 0, 'f': 0, 'd': 0, 'x': 0}
    die = None #placeholder to hold die results


    #add results of positive die
    for x in range(blue):
        die = getBlueDice()
        #print(die)
        total_roll['s'] += die['succ']
        total_roll['a'] += die['adv']

    for x in range(green):
        die = getGreenDice()
        #print(die)
        total_roll['s'] += die['succ']
        total_roll['a'] += die['adv']

    for x in range(yellow):
        die = getYellowDice()
        #print(die)
        total_roll['s'] += die['succ']
        if die['adv'] != -1:    #checking for a triumph
            total_roll['a'] += die['adv']
        else:
            total_roll['t'] += 1

    #subtract results of negative die
    for x in range(black):
        die = getBlackDice()
        #print(die)
        total_roll['s'] -= die['fail']
        total_roll['a'] -= die['dis']

    for x in range(purple):
        die = getPurpleDice()
        #print(die)
        total_roll['s'] -= die['fail']
        total_roll['a'] -= die['dis']

    for x in range(red):
        die = getRedDice()
        #print(die)
        total_roll['s'] -= die['fail']
        if die['dis'] != -1:    #checking for a dispair
            total_roll['a'] -= die['dis']
        else:
            total_roll['x'] += 1

    #correct the total (no negatives)
    #NOTE: according to the official rules, triumphs and dispairs DO NOT cancel out
    if (total_roll['s'] < 0):
        total_roll['f'] = abs(total_roll['s'])
        total_roll['s'] = 0
    if (total_roll['a'] < 0):
        total_roll['d'] = abs(total_roll['a'])
        total_roll['a'] = 0

    return total_roll



print(roll(0, 0, 0, 0, 1, 0)) #testing functions. at first glance, they work.
