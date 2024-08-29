def second_smallest(numbers):
    if len(numbers)<2:
        return
    if len(numbers)==2 and numbers[0]==numbers[1]:
        return
    dup_items=set()
    uniq_items=[]
    for i in numbers:
        if i not in dup_items:
            uniq_items.append(i)
            dup_items.add(i)
    uniq_items.sort()
    return uniq_items[1]
print(second_smallest([1,2,-8,-2,0,-2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2, 2]))  # Edge case with two identical elements, returns None
print(second_smallest([2])) j