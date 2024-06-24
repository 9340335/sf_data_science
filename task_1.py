
input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')

# Удаляем ненужные символы для применения метода .isdigit()
# Для сокращения кода объединяем обе строки
test_str = input_string1 + input_string2
test_str = test_str.replace(',', '')
#test_str = test_str.replace("'", "")
test_str = test_str.replace(' ', '')
    
def pure_intersection(input_string1, input_string2):
    # с помощью метода .isdigit() проверяем, что строка содержит только цифры        
    if not test_str.isdigit():
        return 'Некорректный ввод' # если в строке есть иные элементы - выводим "Некорректный ввод"
    # преобразуем данные в множества и проверяем наличие совпадающих элементов методом .intersection()
    else:
        # для корректного преобразования введенных данных в множества, преобразуем строки в списки с разделением ', '
        input_string1, input_string2 = input_string1.split(', '), input_string2.split(', ')
        input_string1, input_string2 = set(input_string1), set(input_string2)
        intersection_lst = [] # создаем пустой лист
        intersection_lst = list(input_string1.intersection(input_string2)) # перезаписываем пустой лист при наличии пересечений
        return intersection_lst 
           
print(pure_intersection(input_string1, input_string2))