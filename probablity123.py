import random

def prob_a_or_b(a,b,all_possible_outcomes):
    prob_a=len(a)/len(all_possible_outcomes)

    prob_b = len(b)/len(all_possible_outcomes)

    inter = a.intersection(b)
    prob_a_and_b = len(inter)/len(all_possible_outcomes)

    return prob_a + prob_b - prob_a_and_b

evens = {2,4,6}
odds = {1, 3, 5}
greater_than_two = {3, 4, 5, 6}
all_possible_outcomes = {1, 2, 3, 4, 5, 6}

print("Probability of evens or odds:", prob_a_or_b(evens, odds, all_possible_outcomes))
print("Probability of evens or greater than two:", prob_a_or_b(evens, greater_than_two, all_possible_outcomes))
