lst = [ 1, 4.4, "hello", False, 0, -33 ]
print(lst)
print(lst[2])
print(lst[-1])
print(lst[2:4])
print(lst[2:])

lst[0] = 100
lst[3:4] = [1, 2, 3, 4, 5]
print(lst)

lst.insert(3, "world")
lst.append(True)
print(lst)

lst1 = [1,2,3,4,5]
lst1.extend(lst)
print(lst1)

lst.remove("hello")
print(lst)

lst.pop(1)
print(lst)

for item in lst:
    print(item)

print(len(lst))

lst.clear()
print(lst)

lst2 = [120, 8, 1, -5, 9, 3, 22, 132]
lst2.sort()
print(lst2)

lst3 = lst2.copy()
print(lst3)
lst3[0] = 0
print(lst2 + lst3)