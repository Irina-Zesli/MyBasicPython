# Печать элементов списка, делящихся на 5
def function_list_5(numbers):
    for number in numbers:
        if number%5 != 0:
            continue
        print(number, end = ' ')
    print("")
    
numbers1 = [2, 4, 78, 3, 110, 98, 45]
numbers2 = [5, 12, 3, 220, 13, 101, 870, 6]

function_list_5(numbers1)
function_list_5(numbers2)
print("")

# Простой поиск и возвращение минимального элемента в списке
def get_min_simple(numbers):
    m = numbers[0]
    for number in numbers:
        if number < m:
            m = number
    return m

numbers1 = [2, 4, 78, 3, 1, 98, 76, 6]
numbers2 = [12, 43, 22, 13, 101, 87, 6, 45, 5]

my_min = get_min_simple(numbers1)
print(my_min)
my_min = get_min_simple(numbers2)
print(my_min)
print("")

# Поиск в списке первого элемента, меньшего my_value.
def get_first_less(numbers, my_value):
    for number in numbers:
        if number < my_value:
            print(number)
            break
    else:
        print("Элемент не найден")

numbers1 = [42, 4, 78, 3, 11, 98, 76, 6, 2, 67]
numbers2 = [12, 13, 22, 13, 101, 87, 16, 45, 5]

MIN_VALUE = 30

get_first_less(numbers1, MIN_VALUE)
get_first_less(numbers2, 1)
