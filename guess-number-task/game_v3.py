"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def game_core_v3(number: int = 1) -> int:
    """Для начала выбираем число 50, как середину диапазона от 1 до 100. В зависимости от того, больше или меньше загаданное число - 
    выбираем число в середине диапазонов от 50 до 100 или от 1 до 50. Переназначаем границы диапазона, что бы выбирать числа только из отгаданного диапазона. 
    Когда остается меньше 5 возможных вариантов - увеличиваем или уменьшаем последний вариант загаданного числа на 1. 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    end_int = 100 # Устанавливаем конец диапазона
    count = 0
    guess_num = 50 # Устанавливаем число с которого начинается отгадывание
    
    while number != guess_num:
      count += 1
      if guess_num > number and guess_num > 5: # Если загаданного число меньше нашего варианта
      # переназначаем вернюю границу диапазона и проверяем со следующим числом, кторое вдвое меньше предыдущего  
        end_int = guess_num
        guess_num //= 2
      elif guess_num > number and guess_num < 5: # Когда диапазон возможных вариантов сокращается до 5 - начинаем перебор, уменьшая предыдущую догадку на 1 
        guess_num -= 1
      
      elif guess_num < number and guess_num < 95: # Если загаданное число больше нашего варианта - 
      # выбираем следующее число из середины диапазона между предыдущим вариантом и концом диапазона
        guess_num = (end_int + guess_num) // 2
      # Когда число возможных вариантов сокращается до 5 - дальнешие попытки угадывания производим путем перебора, увеличивая предыдущую догадку на 1
      elif guess_num < number and guess_num > 95:
        guess_num += 1

    # Ваш код заканчивается здесь
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(game_core_v3)
