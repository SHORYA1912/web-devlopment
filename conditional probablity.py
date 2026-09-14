def a_and_b(a, b):

    if a == 1 :
        prob_student = 0.3
        if b ==1:
            prob_dining = 0.75
        else:
            prob_dining = 0.25
        print("THE PROBABILITY OF GIVEN A AND B : ", prob_dining)

    if a ==2:
        prob_student = 0.7
        if b==2:
            prob_dining = 0.6
        else:
            prob_dining = 0.4

        print("THE PROBABILITY OF GIVEN A AND B : ", prob_dining)

    print("THE PROBABILITY OF GIVEN A AND B IS: ", prob_student * prob_dining)
    prod_a_b = prob_student * prob_dining
    return(prod_a_b)

print("CHECK THE PROBABILITY OF THE GIVEN A AND B, CHECK YOUR ANSWER")

print("IS THE STUDENTS FRESHMEN? (1/2) : ")
a =int(input("Enter the value of A:1/2 "))
print("ARE THEY EATING IN THE DINING HALL? (1/2) : ")
b =int(input("Enter the value of B:1/2 "))
print("THE PROBABILITY OF BOTH THE EVENTS A AND B IS: ", a_and_b(a, b))
