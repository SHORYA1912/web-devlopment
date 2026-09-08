import random

set1 ={'v','d','a','b','c'}
set2 ={'a','b','c','d','e'}

union = set1.union(set2)

total_guest = list(union)

print("Total guests invited to the party:", len(total_guest))
print("Guest list:", total_guest)
