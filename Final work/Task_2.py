from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    @property
    def cache(self):
        if len(self._cache) == 0:
            return None
        return list(self._cache)[0]

    @cache.setter
    def cache(self, new_elem): # этот метод должен добавлять новый элемент
        key, value = new_elem
        self.put(key, value)

    def get(self, key):
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key, value):
        if key in self._cache:
            self._cache[key] = value
            self._cache.move_to_end(key)
        else:
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
            self._cache[key] = value

    def print_cache(self):
        print("LRU Cache:")
        if not self._cache:
            print('Кэш пуст')
        else:
            for key, value in self._cache.items():
                print(f"{key} : {value}")
        print()


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2")) # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
