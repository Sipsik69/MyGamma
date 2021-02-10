condition = True
while condition:
    user_choice = input('\nPlease choose:\n1. Check id code\n0. Exit\n-->')
    if user_choice == '1':
        condition2 = True
        while condition2:
            user_id = input('Please enter your Id: ')
            try:
                user_id = str(int(user_id))
                if len(user_id) != 11:
                    if len(user_id) > 11:
                        print('Id too Long')
                    elif len(user_id)<11:
                        print('Id too Shot')
                    raise UserWarning
                else:
                    condition2 = False
            except:
                print('Error')
            else:
                gender_id = user_id[0]
                birth_year  = user_id[1:3]
                birth_month = user_id[3:5]
                birth_day = user_id[5:7]
                birth_region = user_id[7:10]
                check_num = user_id[10]

                age = ['18', '19', '20','21']
                if gender_id in '1357':
                    gender = 'Man'
                    birth_cent = age['1358'.find(gender_id)]
                elif isik[0] in '2468':
                    gender = 'Woman'
                    birth_cent = age['246'.find(gender_id)]
                else :
                    ender = 'Ups..'
                    birth_cent = 'Ups...'

                ha_num = int(birth_region)
                if ha_num in range(1, 11):
                    ha_name = 'Kuressaare haigla'
                elif ha_num in range(11, 20):
                   ha_name = 'Tartu Ülikooli Naistekliinik'
                elif ha_num in range(21, 151):
                   ha_name = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                elif ha_num in range(151,161):
                   ha_name = 'Keila haigla'
                elif ha_num in range(161 ,221):
                   ha_name = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
                elif ha_num in range(221, 271):
                   ha_name = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
                elif ha_num in range(271,371):
                   ha_name = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif ha_num in range(371, 421):
                   ha_name = ' Narva haigla'
                elif ha_num in range(421, 471):
                   ha_name = 'Pärnu haigla'
                elif ha_num in range(471, 491):
                   ha_name = 'Haapsalu haigla'
                elif ha_num in range(491, 521):
                   ha_name = 'Järvamaa haigla (Paide)'
                elif ha_num in range(521, 571):
                   ha_name = 'Rakvere haigla, Tapa haigla'
                elif ha_num in range(571, 601):
                   ha_name = 'Valga haigla'
                elif ha_num in range(601, 651):
                   ha_name = 'Viljandi haigla'
                elif ha_num in range(651, 701):
                   ha_name = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
                else:
                    ha_name = 'Not born......'

                print('Your Id is: ', user_id)
                print('You are '+gender)
                print('Your date of Birth is : ', birth_day+'.'+birth_month+'.'+birth_cent+birth_year)
                print('You are born in ',ha_name)

    elif user_choice == '0':
        quit('Finally')
    else :
        print('Choice out of range')
