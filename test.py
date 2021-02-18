# print('  jjj  j   '.strip())
# print("\033[1;32;40m  Green  \n")
# print("\033[1;31;40m Red  \n")
# print("\033[1;33;40m Yellow  \n"
s1 = [2,3,1]
s2 = ['aaa','vvvv','ddd']

s3 = list(zip(s1,s2))
print(s3)
s3.sort()
print(s3)
for i in s3[::-1]:
    print(i[1])

