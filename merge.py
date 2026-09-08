import random

set1 ={'v','d','a','b','c','z','x','y'}
set2 ={'a','b','c','d','e','f','g','h'}

print("UNION")
union = set1.union(set2)
total_guest = list(union)
print("TOTAL GUESTS INVITED TO THE PARTY:", len(total_guest))
print("GUEST LIST:", total_guest)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("INTERSECTION")
intersection= set1.intersection(set2)
total_guest = list(intersection)
print("TOTAL GUESTS INVITED TO THE PARTY", len(total_guest))
print("GUEST LIST:", total_guest)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("PROBABILITY")
def prob_a_or_b(a,b,all_possible_outcomes):
    prob_a=len(a)/len(all_possible_outcomes)

    prob_b = len(b)/len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_a_b = len(inter)/len(all_possible_outcomes)
    return prob_a + prob_b - prob_a_b

prob = prob_a_or_b(set1, set2, union)
print("PROBABILITY OF INVITING A GUEST FROM EITHER SET:", prob)
print("PROBABILITY OF INVITING A GUEST FROM SET1:", len(set1)/len(union))