def prob_a_and_b(a,b):

    if a==1:
        prob_a = 0.2
        if b==1:
                prob_bga=0.85
        elif b==2:
                prob_bga=0.15
        else:
            print("invalid choice")
        prob_a_and_b = prob_a * prob_bga
        print("THE PROBABILITY OF B GIVEN A IS: ", prob_bga)
        print("THE PROBABILITY OF BOTH THE EVENTS OCCURRING A AND B IS: ", prob_a_and_b)

    elif a==2:
              
        prob_a = 0.8
        if b==1:
                prob_bga=0.75
        elif b==2:
                prob_bga=0.25
        else:
                print("invalid choice")
        prob_a_and_b = prob_a * prob_bga
        print("THE PROBABILITY OF A AND B IS: ", prob_a_and_b)
        print("THE PROBABILITY OF GIVEN A AND B IS: ", prob_bga)

    else:
        print("invalid choice")

print("LETS CALCULATE THE PROBABILITY OF A AND B")

print("HAS THE PERSON STEPED THROUGHT // 1. YES 2. NO")
a = int(input("ENTER YOUR CHOICE: "))

print("HAS THE PERSON HAS BEEN POSITVE // 1. YES 2. NO")
b = int(input("ENTER YOUR CHOICE:"))

print("THE PROBABILITY OF GIVEN A AND B IS: ", prob_a_and_b(a,b))