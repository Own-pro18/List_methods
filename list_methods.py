# lst1 = [8,1,1,4,4,12]
# values = 4
# lst1.remove(values)
# print(lst1)
# x = lambda a,b:a*b
# print(x(5,5))# x = lambda a,b:a/b
# print(int(x(6,2)))
lst = [3,4,2,7,25]
lst1 = str(lst)
print(type(lst))
print(type(lst))
nw = [x for x in lst if isinstance(x, int)]
print(nw)
nw = [x for x in lst if isinstance(x, str)]
print(f'lst of string instances{nw}')
nw = [x for x in lst1 if "thre" in x]
print(f'yes exsist {nw} in {lst1}')
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst.insert(1,23)
print(lst)
print(lst[-5:])
lst.reverse()
print(lst)
print(lst[0])
lst[0:1]="apple","car"
print(lst)
tup1 = (1,2,3,"apple","orange")
tup2 = (2,34)
add = tup1+tup2
print(add)
lst.extend(tup1)
print(lst)
lst.remove
lst.remove("apple")
print(lst)
del lst[2]
print(f'this is del function',lst)
st = [x for x in lst if isinstance(x, str)]
ls = [x for x in st if "e" in x]
print(ls)
print(lst.pop(3))
print(lst)
cnt = lst.count("e")
print(cnt)
print(lst)
x = lst.copy()
[print(x) for x in lst]
print(len(lst))
x = list(dict.fromkeys(lst))
print(f'Removed Duplicate Entries {x}')