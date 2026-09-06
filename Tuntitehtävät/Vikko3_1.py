number = [1.2, 5.6, 4.5, 6.7, 9.8]
number1 = [1.2, 9.3, 6.5, 5.5, 8]
number2 = [1.2, 7.9 , 5, 9.5, 7.8]
average_li =[]
def addtolist(new_number):
    average_li.append(new_number) 

def average(list):
    avg = sum(list) / len(list)
    addtolist(round(avg, 2))

average(number)
average(number1)
average(number2)

print(average_li)
