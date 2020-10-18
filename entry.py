import sys
import re
import math
import array as arr

#exit if number of inline arguments is different than 1, or the polynomial expression does not contain a "="
if (len(sys.argv) != 2 or sys.argv[1].find('=') == -1):
    sys.exit()

#printing arguments infos
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('Argument 1:', str(sys.argv[1]))

#remove space and return the string
def rmv_space(string): 
    return string.replace(" ", "")

def my_abs(nbr):
    if (nbr == 0):
        return (0)
    elif (nbr > 0):
        return (nbr)
    return (-nbr)

def my_pow2(nbr):
    return (nbr*nbr)

#get the polynomial degree      
def get_max_deg(coeff):
    if (coeff[0] == 0 and coeff[1] == 0 and coeff[2] == 0):
        return (0)
    elif (coeff[2] != 0):
        return (2)
    elif (coeff[1] != 0):
        return (1)
    else:
        return (0)

#check if string contain float
def is_float(term):
    if (term.find('.') == -1):
        return False
    return True

#convert string to number
def to_number(term):
    if(is_float(term)):
        return float(term)
    return int(term)

#return coeff from term
def get_coeff(term,flag):
    if (term[0] == 'x'):
        if(flag == 1):
            return(-1)
        return(1)
    elif (is_float(term)):
        temp = to_number(re.findall("\d+\.\d+", term)[0])
        if (flag == 1):
            my_abs(temp)
            return(-temp)
    else:
        temp = to_number(re.findall(r"^[^\d]*(\d+)", term)[0])
        if (flag == 1):
            my_abs(temp)
            return(-temp)
    return temp

#expression to list of coefficients
def get_coeff_list(exp):
    coeff_list = [0, 0, 0]
    arr = re.split('(\+|-)',exp)
    #print('list of terms : ')
    #print(arr)
    flag = 0
    for term in arr:
        if (term == ''):
            continue
        elif (term == '+'):
            flag = 0
        elif (term == '-'):
            flag = 1
        else:
            if (term.find('x^1') != -1):
                coeff_list[1] += get_coeff(term,flag)
            elif (term.find('x^2') != -1):
                coeff_list[2] += get_coeff(term,flag)
            else:
                coeff_list[0] += get_coeff(term,flag)
    return coeff_list

#check if list is null
def is_null(coeffs):
    for elem in coeffs:
        if (elem != 0):
            return 0
    return 1

#coeff lists substraction
def coeff_sub(coeff1,coeff2):
    if (is_null(coeff1) and is_null(coeff2)):
        return (0)
    elif (is_null(coeff2)):
        return (coeff1)
    elif (is_null(coeff1)):
        return (coeff2)
    coeff1[0]-=coeff2[0]
    coeff1[1]-=coeff2[1]
    coeff1[2]-=coeff2[2]
    return (coeff1)

#print reduced form
def print_reduced(coeff):
    if (is_null(coeff)):
        sys.stdout.write('ll the real numbers are solution\n')
        return

    if (coeff[2] != 0):
        if (coeff[2] < 0):
            sys.stdout.write('- ')
        if (coeff[2] != 1):
            sys.stdout.write(str(abs(coeff[2])) + ' * ')
        sys.stdout.write('X^2 ')
    if (coeff[1] != 0):
        if (coeff[1] < 0):
            sys.stdout.write('- ')
        else:
            if (coeff[2] != 0):
                sys.stdout.write('+ ')
    if (coeff[1] != 0):
        if (coeff[1] != 1):
            sys.stdout.write(str(abs(coeff[1])) + ' * ')
        sys.stdout.write('X ')
    if (coeff[0] != 0):
        if (coeff[0] < 0):
            sys.stdout.write('- ')
        else:
            sys.stdout.write('+ ')
    if (coeff[0] != 0):
        sys.stdout.write(str(abs(coeff[0])) + ' ')
    sys.stdout.write('= 0')
    sys.stdout.write('\n')
    return

#solve 0
def solve0(coeff):
    return

#solve 1st degree
def solve1(coeff):
    res = -coeff[0]/coeff[1]
    if (res == 0):
        return (0)
    print('X = ' + str(res))
    return

#calculate discriminant
def disc(coeff):
    print('disc d = ' + str(my_pow2(coeff[1])-4*coeff[2]*coeff[0]))
    return (my_pow2(coeff[1])-4*coeff[2]*coeff[0])

#solve 2nd degree
def solve2(coeff):
    d = disc(coeff)
    if (d < 0):
        print('The equation has no solution in R')
    elif (d == 0):
        print('One solution -b/2a :')
        print(-coeff[1]/2*coeff[2])
    else:
        a = coeff[2]
        b = coeff[1]
        c = coeff[0]
        print('a = ' + str(a) + ' b = ' + str(b) + ' c = ' + str(c))
        discr = my_pow2(b)-4*a*c
        print('Two solutions :')
        print('solution 1 : ')
        temp1=-b+math.sqrt(discr)
        temp2=2*a
        sol=temp1/temp2
        print(sol)
        print('solution 2 : ')
        temp1=-b-math.sqrt(discr)
        sol=temp1/temp2
        print(sol)
    return

#main entry
def entry(arg):
    p1 = rmv_space(arg.split('=')[0]).lower()
    p2 = rmv_space(arg.split('=')[1]).lower()
    coeff1 = get_coeff_list(p1)
    coeff2 = get_coeff_list(p2)
    final_coeff = coeff_sub(get_coeff_list(p1),get_coeff_list(p2))
    deg = get_max_deg(final_coeff)
    if (deg != 1 and deg != 2):
        print('Please input a valid linear or quadratic polynomial equation')
        return
    print('poly max deg')
    print(deg)
    print(p1)
    print(p2)
    print('coeff list 1st poly :')
    print(coeff1)
    print('coeff list 2nd poly :')
    print(coeff2)
    print('coeff reduced form :')
    print(final_coeff)
    print_reduced(final_coeff)
    #print('discriminant')
    #print(disc(final_coeff))
    if (deg == 1):
        solve1(final_coeff)
    elif (deg == 2):
        solve2(final_coeff)
    # if (deg == '0'):
    #     print('\033[31m' + 'X\033[0m = 0')
    #     return
    # else:
    #     print('\033[31m' + 'X\033[0m' + ' = \u001b[33m' + res)
    #     return
    return

entry(sys.argv[1])
