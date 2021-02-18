# with open('blad.txt','r') as file:
with open('text.txt', 'r',encoding='UTF8') as file:
    data = file.read()\
        # .replace('\xa0','').replace('\n','').replace(',','').replace('—','').replace('.','').replace('?','').replace('!','').replace(':','').replace('…','').replace('«','').replace('»','')
    data_list = data.split(' ')
    data_set = set(data_list)

    print('Кол-во слов: ',len(data_list))
    print('Кол-во уникальных слов: ',len(data_set))
print(data_list)

ves_list =[]
for num in data_set:
    ves_list.append(data_list.count(num))
print(ves_list)

top_list = list(zip(ves_list,data_set))
top_list.sort()
top_list.reverse()
print(top_list)

# for i in s3[::-1]:
#     print(i[1])
