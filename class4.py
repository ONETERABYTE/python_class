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

tel("+2348033788529")

def sort_number(*args):
    numbers_list = args
    result_list =  []  

    for number in numbers_list:
        string = str(number)
        replaced = string.replace("+234", "0")    
        result_list.append(replaced)
    print(result_list)
    


sort_number("+2348033788529","+234908676774","+234807645789")

