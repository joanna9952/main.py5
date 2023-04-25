# exercise 1
def selection_sort(numbers: list):
    for fill_slot in range(len(numbers) - 1, 0, - 1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location

        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp


numbers = [-2, 0, 4, 9, 3, -6, 1]
print(numbers)
selection_sort(numbers)
print(numbers)
print()


# exercise 2
def binary_search(text: list, target: str):
    first = 0
    last = len(text) - 1

    while first <= last:
        mid = (first + last) // 2

        if text[mid] == target:
            return text[mid]

        elif text[mid] < target:
            first = mid + 1

        else:
            last = mid - 1

    return None


text = ['dog', 'cat', 'frog', 'mouse', 'tiger']
target = 'dog'
print(text)
binary_search(text, target)
print(binary_search(text, target))
print()


# exercise 3-6
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return len(key) % self.size
        else:
            raise TypeError

    def put(self, key, data):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None


hash_table = HashTable(6)

hash_table.put(1, "tiger")
hash_table.put(2, "lion")
hash_table.put(3, "elephant")
hash_table.put(4, "giraffe")
hash_table.put(5, "crocodile")

print(hash_table.get(1))
print(hash_table.get(2))
print(hash_table.get(3))
print(hash_table.get(4))
print(hash_table.get(5))
print(hash_table.get(6))
