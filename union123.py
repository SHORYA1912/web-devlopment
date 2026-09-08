import random

set1 ={'v','d','a','b','c'}
set2 ={'a','b','c','d','e'}

intersection = set1.intersection(set2)

total_guest = list(intersection)

print("total guests invited to the party:", len(total_guest))
print("Guest list:", total_guest)