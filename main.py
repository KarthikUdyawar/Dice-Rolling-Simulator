import random

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    Dice = Dice1 + Dice2
    print("Rolling the dices...")
    print("The values are....")
    print(str(Dice1), str(Dice2))
    print("Total value: " + str(Dice))
    roll_again = (input("Roll the dices again? (y/n)"))
