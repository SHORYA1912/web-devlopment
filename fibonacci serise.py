def fib_serise(nterms):
    n1, n2= 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
nterms = int(input("how many terms")) 
if nterms <= 0:
        print("Please enter a positive integer")
elif nterms == 1:
        print("Fibonacci sequence upto", nterms,":")
        fib_serise(nterms)
else:
        print("Fibonacci sequence:")
        fib_serise(nterms)
            