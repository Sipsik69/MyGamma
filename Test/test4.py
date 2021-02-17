# mylist = []
#
# cond = True
# while cond:
#     zz=input('enter Element, 0 - exit: ')
#     if zz=='0':
#         cond = False
#     else:
#         mylist.append(zz)
#
# print(mylist)
# mylist.reverse()
# print(mylist)

some_list = input('Enter ,: ').split(', ')
# print(some_list[::-1])
for num in some_list[::-1]:
    print(num)
