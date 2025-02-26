"""
Algorithm that receives a list of integers of size N and returns another list with the ranking of the original values, respecting the indexes.

For example, the list [7, 10, 5, 6, 7] would return [2, 1, 4, 3, 2].

Lists with repeated values ​​should also work. In this case, the same values ​​receive the same ranking.
"""

from random import randint
arr = [randint(1, 10) for i in range(5)]
print(arr)

rank_list = [0 for num in range(len(arr))]
past_numbers = list()

count = 1
while True:
    if arr.count(-1) == len(arr):
        break

    max_value = max(arr)
    max_index = arr.index(max_value)
    rank_list.pop(max_index)

    if count == 1:
        rank_list.insert(max_index, count)
        arr.remove(max_value)
        arr.insert(max_index, -1)
    
    else:
        other_count = 1
        for list in past_numbers:
            if max_value == list[0]:
                rank_list.insert(max_index, list[1])
                arr.remove(max_value)
                arr.insert(max_index, -1)
                count -= 1
                break
            elif other_count == len(past_numbers):
                rank_list.insert(max_index, count)
                arr.remove(max_value)
                arr.insert(max_index, -1)
            else:
                other_count += 1
                continue

    past_numbers.append([max_value, count])

    count += 1
    
print(rank_list)