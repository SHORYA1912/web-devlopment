def random_no():
    import random
    return random.randint(1,100)

print("PICK ANY RANDOM NUMBER BETWEEN 1 AND 100:")
INPUTNO = int(input("PICK ANY RANDOM NUMBER BETWEEN 1 AND 100:"))

if INPUTNO == random_no():
    print("CONGRATULATIONS! YOU HAVE WON THE GAME")
    print("THE PROBABILITY OF WINNING THE GAME IS 1/100 OR 0.01")
else:
    print("SORRY! YOU HAVE LOST THE GAME")
    print("THE PROBABILITY OF WINNING THE GAME IS 1/100 OR 0.01")