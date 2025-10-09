n = int(input())
digit = '1234567890'
total = 0
for i in range(n):
    text = input()
    for j in text:
        if j in digit:
            total += 1
            break
print(total)
