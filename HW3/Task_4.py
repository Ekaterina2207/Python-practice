s = input().lower()
result = {}
for i in s:
    result[i] = result.get(i, 0) + 1
print(result)
