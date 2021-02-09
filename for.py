# courses = ['History','Programing','Math','Literature','Physics']
#
# counter = 0
# for item in courses:
#      print(item)
#      counter +=1
#
#
# print('This is last Element:',item)
# print(counter)

numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a','b','c','d']

# for num in numbers:
#     for num2 in numbers:
#         for num3 in numbers:
#             for num4 in numbers:
#                 print(num,num2,num3,num4)
#
# for num in numbers:
#     for let in letters:
#         print(num,let)

if len(numbers)>5:
    for num in numbers:
        if num % 2 ==0:
            if num>5:
                print('Even and >5')
            elif num<= 5:
                   print('Even and Small 5',num)
            else:
                print(num,'Even')
        else:
            if num>5:
                print('Odd and >5')
            else:
                print(num, 'Odd')