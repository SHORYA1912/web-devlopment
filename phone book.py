import sys
def initial_phonebook():
    row,cols = int(input("enter initial no. of contacts:")),5

    phone_book = []
    print("phone_book")
    for i in range(row):
        print("\nEnter the contact %d details in the following order (ONLY):" % (i+1))
        print("note * indicates mandotary fileds")
print("**************************************************************************************************************")
temp = []
for j in range(cols):
    if j == 0:
        temp.append(str(input("enter name*: ")))
    if temp[j]==""or temp[j]==" ":
        sys.exit("Name is a mandotary field process exiting due to empty name")
    if j == 1:
        temp.append(str(input("enter number*: ")))
    if j == 2:
        temp.append(str(input("enter email: ")))
    if temp[j]==""or temp[j]==" ":
    if j == 3:
        temp.append(str(input("enter birthdate: ")))