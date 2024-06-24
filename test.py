input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')

#input_string1, input_string2 = input_string1.split(', '), input_string2.split(', ')
print(input_string1)
print(input_string2)

joint_str = input_string1 + input_string2
print(joint_str)

test_str = joint_str
test_str = test_str.replace('[', '')
test_str = test_str.replace(']', '')
test_str = test_str.replace(',', '')
test_str = test_str.replace("'", "")
test_str = test_str.replace(' ', '')
print(test_str)

input_string1 = input_string1.split(', ')

lst1 = list(input_string1)

print(lst1)
    
set1 = set(lst1)
print(set1)