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