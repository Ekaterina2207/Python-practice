def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return abs(a+b)
def nok(a, b):
    return abs(a * b) // nod(a, b)
def nok_list(numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = nok(result, numbers[i])
    return result
def nod_list(numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = nod(result, numbers[i])
    return result
n = int(input("Введите количество чисел: "))
nums = []
for i in range(n):
    nums.append(int(input()))
print('НОД:', nod_list(nums))
print('НОК:', nok_list(nums))