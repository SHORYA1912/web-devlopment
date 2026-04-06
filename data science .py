import numpy as np
data_type=[('name', 'S15'), ('age', int), ('height', float)]
student_deatail = [('james', 5, 48.5), ('nail', 6, 52.5), ('pual', 5, 42.10), ('pit', 5, 40.11)]
students= np.array(student_deatail, dtype=data_type)
print("ORIGINAL ARRAY:")
print(students)
print("SORT BY HEIGHT:")
print(np.sort(students, order='height'))
