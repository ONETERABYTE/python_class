def sort_number(*args):
    numbers_list = args
    result_list =  []  

    for number in numbers_list:
        string = str(number)
        replaced = string.replace("+234", "0")    
        result_list.append(replaced)
    return result_list

    
    


start = sort_number("+2348033788529","+234908676774","+234807645789")

print(start)

