# isik = '36906200277'
# isik = '46305200276'

age = ['18','19','20']

def isik11(isik_test):
    isik_list = list(isik_test)
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    idx  = 0
    ves1 = 0
    ves2 = 0
    for num in isik_list[0:10]:
        ves1 = ves1 + int(num) * kaal1[idx]
        ves2 = ves2 + int(num) * kaal2[idx]
        idx += 1
    if ves1%11<10:
        return(str(ves1%11))
    else:
        return(str(ves2%11))


def haigla(ha_num):
    ha_name = ''

    if ha_num>=1 and ha_num<=10:
        ha_name = 'Kuressaare haigla'
    elif ha_num>=11 and ha_num<=19:
       ha_name = 'Tartu Ülikooli Naistekliinik'
    elif ha_num>=21 and ha_num<=150:
       ha_name = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif ha_num>=151 and ha_num<=160:
       ha_name = 'Keila haigla'
    elif ha_num>=161 and ha_num<=220:
       ha_name = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif ha_num>=221 and ha_num<=270:
       ha_name = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif ha_num>=271 and ha_num<=370:
       ha_name = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif ha_num>=371 and ha_num<=420:
       ha_name = ' Narva haigla'
    elif ha_num>=421 and ha_num<=470:
       ha_name = 'Pärnu haigla'
    elif ha_num>=471 and ha_num<=490:
       ha_name = 'Haapsalu haigla'
    elif ha_num>=491 and ha_num<=520:
       ha_name = 'Järvamaa haigla (Paide)'
    elif ha_num>=521 and ha_num<=570:
       ha_name = 'RRakvere haigla, Tapa haigla'
    elif ha_num>=571 and ha_num<=600:
       ha_name = 'Valga haigla'
    elif ha_num>601 and ha_num<=650:
       ha_name = 'Viljandi haigla'
    elif ha_num>=651 and ha_num<=700:
       ha_name = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        ha_name = 'Not born......'

    return ha_name

while True:
    isik_ok=input('0 - Exit, 1 Pristupim pomoljas:')
    if isik_ok=='0':
        exit()

    isik=input('Enter your Isikukood:')

    if len(isik) == 11:
        if isik.isdigit():
            pol_y = isik[0]
            if  pol_y in '135':
                pol = 'Man'
                age_n = age['135'.find(pol_y)]
            elif isik[0] in '246':
                pol ='Woman'
                age_n = age['246'.find(pol_y)]
            else:
                Pol = 'Ups...'

            vozrast = isik[5:7]+'.'+isik[3:5]+'.'+age_n+isik[1:3]

            print(pol)
            print(vozrast)
            haigla_name = haigla(int(isik[6:10]))
            print(haigla_name)
            if isik[10] != isik11(isik):
                print('11 digits is invalid !!!')
        else:
            print('Bukovki')
    else:
        if len(isik)<11:
            print('Korotkovato...')
        else:
            print('Dlinnovato')

