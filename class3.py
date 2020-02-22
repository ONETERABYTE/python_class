import random
y = random.randrange(0,50,5)
print(y)


def stickers(x):  
      result = int(x) * 10
      print(result)
stickers(7)  

def my_function(country = "nigeria"):
    print("i am from"  + country)
my_function("nigeria")    
my_function ("sweden")
my_function ("ghana")
my_function ("togo")

def tel(x):
    if "+234" in x:
        result = x.replace("+234","0")
        print(result)

tel("+2348033788529","+234809976543")

def my_function(a = 5+2):
    print (result)

