d = {'a': 1, 'b': 2}
d.clear()
print(d)  # Output: {}

d = {'a': 1, 'b': 2}
d_copy = d.copy()
print(d_copy)  # Output: {'a': 1, 'b': 2}

d = {'a': 1}
print(d.get('a'))       # Output: 1
print(d.get('b', 0))    # Output: 0

d = {'a': 1}
print(d.get('a'))       # Output: 1
print(d.get('b', 0))    # Output: 0

d = {'a': 1}
print(d.setdefault('b', 2))  # Output: 2
print(d)                     # Output: {'a': 1, 'b': 2}

d = {'a': 1}
d.update({'b': 2})
print(d)  # Output: {'a': 1, 'b': 2}

d = {'a': 1, 'b': 2}
print(d.pop('a'))  # Output: 1
print(d)           # Output: {'b': 2}

d = {'a': 1, 'b': 2}
print(d.popitem())  # Output: ('b', 2)
print(d)            # Output: {'a': 1}

d = {'a': 1, 'b': 2}
print(d.keys())  # Output: dict_keys(['a', 'b'])

d = {'a': 1, 'b': 2}
print(d.values())  # Output: dict_values([1, 2])

keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}
