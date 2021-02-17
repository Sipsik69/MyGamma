#
# str =input('enter Stroka palindrom: ')
# str1 = str.replace(' ','')
# print(str1)
#
# mylist = list(str1)
# print(mylist)
#
# mylist.reverse()
# newstr = ''
# for i in mylist:
#     newstr = newstr+i
#
# if str1==newstr:
#     print('URA !!!', str+' = '+newstr)
# else:
#     print('Fig Vam....')

entry = 'never odd or even'
# if entry.lower().replace(' ','') == entry.lower().replace(' ','')[::-1]:
entry = entry.lower().replace(' ','')

if entry == entry[::-1]:
    print('Ura')
else:
    print('Uvi')
