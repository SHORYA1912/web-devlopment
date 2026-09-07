import random

def picking_random_BALL():
    balls = ['red','green','blue']
    results = random.choice(balls)

    pro = balls.count('red')/len(balls)
    print(f"Probability of picking a red ball: {pro}")

    if results == 'red':
        print("You picked a red ball!")
    else:
        print("You did not pick a red ball.")

res = picking_random_BALL()
print(res)
