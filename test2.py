input_string = input('Введите последовательность чисел: ')
input_string = input_string.replace(',', '.')
print(input_string)
test_list = list(input_string.split(' '))
print(test_list)
#print(max(*test_list))


def find_min_max(*test_list):
    mn = min(test_list)
    mx = max(test_list)
    return mn, mx
    #test_list = list(input_string.split(' '))
    #minimum =
print(find_min_max(1,5, 5,5, 12))
    