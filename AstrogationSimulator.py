import DiceResults as dice

#testing if DiceResults works
blue = int(input("blue: "))
green = int(input("green: "))
yellow = int(input("yellow: "))
black = int(input("black: "))
purple = int(input("purple: "))
red = int(input("red: "))

result = dice.roll(blue, green, yellow, black, purple, red)

print result
