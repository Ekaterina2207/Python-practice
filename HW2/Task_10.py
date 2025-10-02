def is_palindrome(lst):
    return lst == lst[::-1]
n = int(input("Количество чисел: "))
numbers = []
for i in range(n):
    d = int(input("Число: "))
    numbers.append(d)
print("Последовательность:", numbers)
for i in range(n):
    if is_palindrome(numbers[i:]):
        print("Нужно приписать чисел: ", i)
        print("Сами числа: ", numbers[:i][::-1])
        break