num = str(input())
num = num.replace(',', '.')
def find_min_max(num):
    minimum = min(num)
    print(minimum)
    maximum = max(num)
    print(maximum)
    result = print(f'Minimum: {minimum}', 'Maximum: {maximum}', end='\n')
    return result
find_min_max(num)