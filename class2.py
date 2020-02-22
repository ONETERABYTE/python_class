mylist = ["tecno", "itel", "infinix", "nokia"]
x = ""
while x != "quit":
    x = input("enter phones,or enter 'quit': ")
    if x in mylist:
        print("phones exist")
    else:
        mylist.append(x)
        print(mylist)

input("enter")

