lst = [3, 1, 4, 1, 5]

lst.append(9)         # [3, 1, 4, 1, 5, 9]
lst.extend([2, 6])    # [3, 1, 4, 1, 5, 9, 2, 6]
lst.insert(2, 10)     # [3, 1, 10, 4, 1, 5, 9, 2, 6]

lst.remove(1)         # Removes first '1'
val = lst.pop(3)      # Removes and returns element at index 3
count = lst.count(1)  # Count of 1s
index = lst.index(5)  # Index of first 5

lst.sort()            # Sorts list
lst.reverse()         # Reverses list

copy_lst = lst.copy() # Copy of list
lst.clear()           # Now lst is []
