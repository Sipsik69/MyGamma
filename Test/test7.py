
str =input('enter Stroka palindrom: ')
str1  = ''
for i in str:
    if i!=' ':
        str1=str1+i
mylist = list(str1)
print(mylist)

mylist.reverse()
newstr = ''
for i in mylist:
    newstr = newstr+i

if str1==newstr:
    print('URA !!!', str+' = '+newstr)
else:
    print('Fig Vam....')
