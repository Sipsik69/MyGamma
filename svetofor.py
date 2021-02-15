# # светофор на 4 стороны   1 *
#       6
#       5
#       4
# 3 2 1  7 8 9
#       10
#       11
#       12

def svet_plus(tek_svet):
    tek_svet += 1
    if tek_svet>3:
        tek_svet = 1
    return tek_svet

def svet_minus(tek_svet):
    tek_svet -= 1
    if tek_svet<1:
        tek_svet = 3
    return tek_svet

def color_v(color_num):
    clr = ['\033[1;32;40mG','\033[1;33;40mY','\033[1;31;40mR']
    blank = ['','','']
    color_name = '    '+clr[color_num-1]
    return color_name

def color_g(color_num):
    clr = ['\033[1;32;40mG','\033[1;33;40mY','\033[1;31;40m R']
    blank = ['       ','     ','   ']
    color_name = clr[color_num-1].rjust(color_num,' ')+blank[color_num-1]+ clr[color_num-1]
    return color_name


vert = 1
gor  = 3
condition = True
while condition:
    print(color_v(vert))
    print(color_g(gor))
    print(color_v(vert))

    klav = input('1 - Next  0- Exit :')
    if klav=='0':
        condition = False

    vert = svet_plus(vert)
    gor = svet_minus(gor)
