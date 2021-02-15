# id_code = input('Please enter your:')
#
# isik_list = list(id_code)
# kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
# idx = 0
# ves1 = 0
# ves2 = 0
# for num in isik_list[0:10]:
#     ves1 = ves1 + int(num) * kaal1[idx]
#     ves2 = ves2 + int(num) * kaal2[idx]
#     idx += 1
#
# check_num = ves1%11
# if check_num==int(id_code[-1]):
#     print('Id Cde is Valid 1')
# elif check_num ==10:
#     check_num = ves2 % 11
#     if check_num == int(id_code[-1]):
#        print('Id Code is Valid 2')
#     else:
#         print('Code is not valid')
# else:
#     print('Code is note valid !!!!!!!!!')


def squares():
    print('Hello World')

squares()

def print_mes(a,b):
    return print(a,b)

print_mes(33,44)
