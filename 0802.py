# empty_list = []
# empty_tuple = ()
# empty_dict = {}
# empty_set = set()
#
# print(type(empty_dict))
# print(type(empty_set))

# empty_list= [1233,12.313,'Some string',True, None,['One','Two',3]]
# print(empty_list)
# print(empty_list[2])
# print(empty_list[1:4])
# print(empty_list[5][1])
# empty_list[2]='New String'
# print(empty_list)
# empty_list[2]=[1233,True,'another String']
# print(empty_list)
# list_element=[1233,True, 'Another String']
# empty_list= [1233,12.313,'Some string',True, list_element,['One','Two',3]]
# print(empty_list)
# print(empty_list[::-1])

courses = ['History','Math','Literature','Physics','Programming',['Economics','Marketing','Math']]
# print(courses)
# courses[0]='Art'

# courses.append('Art')
# new_c = 'Art'
# courses.insert(-1,new_c)
# print(courses)

courses2 = ['Economic','Marketing','Math']
numbers = [1,5,6,7,3,76,23,34]
# courses.extend(courses2)

# courses.remove('Math')
# courses[6].remove('Math')
# pop_item = courses.pop()
# pop_item = courses[5].pop()
# print(pop_item)
# courses.reverse()

courses2=['Economics','Marketing','Math','Art','art']
# courses2.sort()
# print(courses2)
# setting=True
# courses2.sort(reverse=setting)
# print(courses2)

# courses= sorted(courses2)
# print(courses)
# print(courses2)

# print(min(numbers))
# print(max(numbers))
# print(min(courses2))
# max_value = max(courses2)
# print(max_value)
# art_index = courses2.index('Art')
# print(art_index)
# # print(courses2[art_index])
# print('art' in courses2)

new_str = """When Python 2.7 was still supported, a lot of functionality in Python 3 was kept for backward compatibility with Python 2.7"""
#
# courses_str = ', '.join(courses2)
# print(courses2)
# print(courses_str)
# print(type(courses_str))
# new_list= courses_str.split(', ')
# print(new_list)
# print(type(new_list))
# nl = new_str.split('\n')
# print(nl)
# print(len(nl))

# list_1 =['Math','History','Programming','Phisics']
# list_2 = list_1.copy()
# print(list_1)
# print(list_2)
#
# list_1[2]='Sports'
# list_2[0]='Art'
# print(list_1)
# print(list_2)

# courses = ('History','Math','Literature','Physics','Programming')
# # print(courses[4])
# courses2 = ('Biology','Programming')
# print(courses+courses2)
# new_c = courses+courses2
# print(new_c)
#
# new_list =list(courses)
# print(new_list)
# print(type(new_list))
# new_list[0]='Biology'
# new_tuple = tuple(new_list)
# print(new_tuple)
# print(type(new_tuple))

# SET
# courses = {'Economics','Marketing','Math','Art','art','Math'}
# courses2 = ['Economics','Marketing','Math','Art','art','Math']
# # print(courses2)
# # print(list(set(courses)))
# courses.remove('Economics')
# print(courses)

set1 = {'Math','History','Programing','Physics'}
set2 = {'Art','Physics','Design','History'}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

print(set1.union(set2))