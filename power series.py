
base = int(input("Enter the base number: "))
terms = int(input("Enter the number of terms in the power series: "))

print(f"Power series of {base}:")
for i in range(terms):
    print(f"{base}^{i} = {base**i}")