import random
def roll_dice():
    dice = random.randint(1, 6)
    print("Вы бросили кубик и выпало:", dice)

    if dice >= 5:
        print("Вы победили :)")
    elif dice >= 3:
        roll_dice()
    else:
        print("Вы проиграли :(")

roll_dice()
