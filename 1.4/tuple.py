tup1 = ( 1, 2, 4, 8, 16 )
print(tup1)

tpl = ( "Macos", "Linux", "Win" )
print(tpl[1])

(work, home, friend) = tpl
print(work)

lst = list(tpl)
lst.append("Unix")
tpl = tuple(lst)
print(tpl)