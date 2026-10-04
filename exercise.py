from dataclasses import dataclass, field
from functools import wraps
from random import random

# 1. Write a function sum_ints(xs: list[int]) -> int that returns the sum. Add proper type hints.
def sum_ints(xs: list[int]) -> int:
    res = 0
    for num in xs:
        res += num
    return res

xs = [1, 2, 3]
res = sum_ints(xs)
print(res)

# 2. Write parse_values(raw: list[str]) -> list[int | str] that converts numeric strings to int and leaves others as str.
def parse_values(raw: list[str]) -> list[int | str]:
    res = []
    for raw_str in raw:
        res.append(int(raw_str) if raw_str.isdigit() else raw_str)
    return res
raw = ['1', '2', '3', 'abc']
print('parse_values<<', parse_values(raw))

# 3. Define a function get_item(d: dict[str, int], key: str) -> int | None returning None if key is missing.
def get_item(d: dict[str, int], key: str) -> int | None:
    return d.get(key)
d = {'1': 3, '2': 2, '3': 1, 'abc': 12}
print('get_item<<<<', get_item(d, 'abc'), get_item(d, 'none_key'))

# 4. Create a Student dataclass: name: str, grades: list[int], id: int. Compute average() as a method.
@dataclass
class Student:
    name: str
    grades: list[int]
    id: int

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) 

student1 = Student('Alice', [100, 90, 80], 123)
print(student1.name, 'has average grades of', student1.average())

# 5. Make a Point dataclass that's frozen and ordered by (x, y).
@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

print(Point(2, 3), Point(0, 1))

# 6. Create a Config dataclass where settings: dict uses default_factory — then verify two instances don't share the dict.
@dataclass
class Config:
    name: str
    settings: dict = field(default_factory=dict) 

a = Config('a')
b = Config('b')
b.settings['a'] = 1
print(a.settings)
print(b.settings)

# 7. From nums = [1, 2, 3, 4, 5, 6], produce [x**3 for x in nums if x % 2 == 0].
nums = [1, 2, 3, 4, 5, 6]
res = [x**3 for x in nums if x % 2 == 0]
print(res)

# 8. Flatten [[1, 2], [3, 4], [5, 6]] into a single list.
list_a = [[1, 2], [3, 4], [5, 6]]
flattened_list_a = [x for xs in list_a for x in xs]
print(flattened_list_a)

# 9. From words = ["apple", "banana", "cherry"], build a dict {word: len(word)}.
words = ["apple", "banana", "cherry"]
dict_from_words = {w:len(w) for w in words}
print(dict_from_words)

# 10. Build a dict of {letter: count} for the letters in a string using a comprehension and str.count.
test_str = 'aabbabcddabe'
letter_count = {c:test_str.count(c) for c in dict.fromkeys(test_str)}
print(letter_count)

# 11. Write a @logged decorator that prints the function name and its args each call.
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'function name: {func.__name__}, args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@logged
def sum_nums(nums: list[int]) -> int:
    return sum(nums)
sum_nums([1, 2, 3])

# 12. Write a @memoize decorator that caches results by arguments (use a dict).
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        if (key not in cache):
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if (n < 2):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))

# 13. Write a @retry(times) decorator that retries a function up to times on exception.
def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'attempted at {attempt} times, error: {e}')
                    if (attempt == times - 1):
                        raise
        return wrapper
    return decorator

@retry(3)
def flacky_test():
    if random() < 0.5:
        raise ValueError('value error')
    else:
        print('success')

flacky_test()

# TODO
# 14. Write a @enforce_types decorator that checks each arg against the function's type hints and raises TypeError on mismatch.
