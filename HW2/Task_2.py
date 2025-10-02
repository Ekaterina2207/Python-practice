class_1 = [x for x in range(160, 177, 2)]
class_2 = [x for x in range(162, 181, 3)]
class_1.extend(class_2)
class_1.sort()
print(f'Отсортированный список учеников:', class_1)