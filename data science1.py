import numpy as np
Data_type = [('name','S15'),('age',int),('mobile_number',float)]
employee_deatail =[('RAVIKUMAR',25, 9016859590),('DAKSH',24, 9825263585),('PRAJAPATI',26, 9876545321)]
employee = np.array(employee_deatail, dtype=Data_type)

print("ORIGINAL ARRAY:")
print(employee)
print("SORT BY AGE:")
print(np.sort(employee, order='age'))
print("SORT BY NAME:")
print(np.sort(employee, order='name'))
print("SORT BY MOBILE NUMBER:")
print(np.sort(employee, order='mobile_number'))