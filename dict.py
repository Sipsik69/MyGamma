# list = [] = list()
# tuple = () = tuple()
# set = set()
# dict = {}
#
# dict_var = {'Name':'Roman', 'Age': 32}
# print(type(dict_var))
# print(dict_var['Name'])

x=5
dict = {x:'variable','name':'John','age':32}
# print(dict[x])
# print(dict[5])
# print(dict)
# print(dict.get('job'))

# dict['name'] = 'Jack'
# dict['job'] = 'Programmer'
# print(dict['job'])
# print(dict)
dict.update(({'name':'Mick','age':27,'phone':'555-5566'}))
# print(dict)
# del dict['name']
# print(dict)

# pop_item = dict.pop('name')
print(dict)
# # print(pop_item)
# print(len(dict))
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for x in dict.items():
#     print(x)

for key,value in dict.items():
     print(key,value)

# somelist = [[1,2,3],[4,5,6],[7,8,9]]
# print(somelist)
# for i in somelist:
#     print(i)
# for x,y,z in somelist:
#     print(x,y,z)
#