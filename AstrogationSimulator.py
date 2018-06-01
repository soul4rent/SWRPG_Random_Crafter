import DiceResults as dice

#testing if DiceResults works
blue = int(input("blue: "))
green = int(input("green: "))
yellow = int(input("yellow: "))
black = int(input("black: "))
purple = int(input("purple: "))
red = int(input("red: "))



#0 dice is a "simple" check, 5 dice is a "formidable" check.
checkDifficulty = max(0, min(purple+red, 5))

#assuming each round is 1 minute
astroTime = [1.0, 2.0, 5.0, 10.0, 60.0, 2400.0]


AT = astroTime[checkDifficulty]

result = dice.roll(blue, green, yellow, black, purple, red)



print (result)

print ("Base Time:", AT)
print ("New Time:", AT - .10*result['a']*AT) 
