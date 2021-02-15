mylist = []

cond = True
while cond:
    zz=input('enter Element, 0 - exit: ')
    if zz=='0':
        cond = False
    else:
        mylist.append(zz)

print(mylist)
mylist.reverse()
print(mylist)

