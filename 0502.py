# some_string1 = ''
# some_string2 = ""
# some_string3 = '''that's'''
# some_string4 = """"""
#
# wrong_string = "that's"
# wrong_string = 'that\'s'
# print(wrong_string)
#
empty_string=''
string_sample = 'Hello world world'
string_sample2 = 'first letteR is lowErcase'
string_sample3 = '  extra whitespace string'
german_string = 'der Flub'

# print(string_sample[0])
# print(string_sample[0:5])
# print(string_sample[-1])
# print(string_sample[-5:-1])
# print(string_sample[:6])
# print(string_sample[0::3])
# print(string_sample[::-1])
# print(test[0:12])
# print(test[-4:-1])
# print(test[0:5], test[19:29])
test = 'Hello world. It is beatiful day.'
# print(len(test))
# print(test.find('beatiful'))
# print(test[19:28])
# print(test.upper())
# print(test.split('.'))
# print(test.lower())
# print(test.casefold())
#
# username= 'rOman'
# # print(username.lower().capitalize())
# username= username.lower().capitalize()
# print(username)

# search = 'world'
# print(string_sample.find('world'))
# print(string_sample.count(search))

# print("world" in string_sample)
# print(string_sample+'. '+string_sample2)
#
# worker = 'John'
# worker2 = 'Mary'
# salary = 1000
# salary2 = 2000
# worker_string = "{}'s salary is {}"
# worker_string = "{1}'s salary is {0}"
# # print(worker+worker_string,salary)
# # print(worker2+worker_string,salary2)
# print(worker_string.format(worker,salary))
#
# apples = 3
# banans = 5
# pears = 2
# fs = "Jonn has {} bananas, {} apples and {} pears"
# print(fs.format(banans,apples,pears))
# fs = "Jonn has {1} bananas, {0} apples and {2} pears"
# print(fs.format(banans,apples,pears))
#
# price = "This {product:} costs {price:.2f} eros"
# print(price.format(price=350,product="computer"))
# print("{space:c}".format(space=32))

# id_code=input('Please enter your id:')
# # if len(id_code)==11:
# #     print('id ', id_code)
# # elif len(id_code)>11:
# #     print('Code longer than 11')
# # else:
# #     print('Code shoter than 11')
# if len(id_code)==11:
#     print('id ', id_code)
#     print('Molodec')
#
# else:
#     print('WONG !!')

somestring = 'Hello world. It is a beautiful day'
if 'beautiful' in somestring:
    print('OK')
else:
    print('Not ')
print(len(somestring))
if len(somestring[0:5])>10:
    print('>>10')
elif len(somestring)>20:
    print('>>20')
