# file = open('text.txt','r',encoding='UTF*')
#
# print(file)
# print(file.name)
# print(file.mode)
# print(file.closed)
#
# file.close()
# print(file.closed)

# with open('text.txt','r',encoding='UTF8') as file:

    # # data = file.read()
    # # data = file.readline()
    # print(file.readline())
    # print(file.readline())
    # print(file.read())
    # # data2 = file.read()
    # # print(data2)

    # for line in file:
    #     print(line,end='***')

    # size_to_read = 100
    # file_content = file.read(size_to_read)
    # while len(file_content) >0:
    #     print(file_content,'***********')
    #     file_content = file.read(size_to_read)
    # print(file_content)
    # file.seek(0)
    # file_content = file.read(size_to_read)
    # print(file_content)
    # file.write('TEST')

with open('test_text.txt','w',encoding='UTF*') as file:

    file.write('TEST')
    file.write('some test string')
    file.seek(0)
    file.write('***T')