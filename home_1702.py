with open('blad.txt','r') as file:

    data = file.read().replace('\xa0','').replace('\n','').replace(',','').replace('—','').replace('.','').replace('?','').replace('!','').replace(':','').replace('…','').replace('«','').replace('»','')
    data_list = data.split(' ')
    data_set = set(data_list)

    print(len(data_list), len(data_set))

# print(data_list)
