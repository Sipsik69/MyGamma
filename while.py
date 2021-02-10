# counter = 0
# while counter<1000:
#     counter +=1
#     if counter%100 ==0:
#         print("I can't stop ",counter,' times')

condition = True
while condition:
    user_input = input('Enter id:')
    try:
        user_input= str(int(user_input))
        if len(user_input) !=11:
            raise UserWarning
        else:
            condition=False

    except :
        print('Raised error')
    else:
        print('Your Id ',user_input)

# except UserWarning:
#     print('Id code long or shot')
    finally:
         print('Program finish working !')

# while True:
#     try:
#       user_input = input('Enter id:')
#       user_input = str(int(user_input))
#        if len(user_input)!=11:
#            print('Please try again')
#            continue
#        else:
#          break
#
