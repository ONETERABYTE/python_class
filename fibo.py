nterms = int(input("how many terms?"))
# first two terms
n1, n2 = 0, 1
count = 1

# check if the number of terms is valid
if nterms <= 1:
    print("enter an integer")
elif nterms == 2:
    print("fibonacci sequence upto",nterms ,":")
    print(n1)
else:
    print("fibonacci sequence:") 
    clone = []  
    while count < nterms:
        clone.append(n1)
        print(clone)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
