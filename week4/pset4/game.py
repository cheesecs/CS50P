# Guess game

import random

while True:
    try:
        level = int(input('Level: '))

        if level <= 0:
            continue

        if level < 2:
            rn = random.randint(1, level)
            break
        else:
            rn = random.choice(range(1, level))
            break
    except ValueError:
            continue

while True:
    guess = int(input('Guess: '))

    if guess > rn:
        print('Too large!')
    
    elif guess < rn:
        print('Too small!')
    
    else:
        print('Just right!')
        break
