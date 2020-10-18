import sys
import re
import array as arr

if (len(sys.argv) != 2 or sys.argv[1].find('=') == -1): #exit if number of inline arguments is different than 1, or the polynomial expression does not contain a "="
    sys.exit()

#printing arguments infos
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('Argument 1:', str(sys.argv[1]))

#remove space and return the string
def rmv_space(string): 
    return string.replace(" ", "")

#get the polynomial degree      
def get_max_deg(poly):
    if (poly.find('x^2') != -1):
        return 2
    elif (poly.find('x^1') != -1):
        return 1
    else:
        return 0

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
            abs(temp)
            return(-temp)
    else:
        temp = to_number(re.findall(r"^[^\d]*(\d+)", term)[0])
        if (flag == 1):
            abs(temp)
            return(-temp)
    return temp

#expression to list of coefficients
def get_coeff_list(exp):
    coeff_list = [0, 0, 0]
    arr = re.split('(\+|-)',exp)
    # print('list of terms : ')
    # print(arr)
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
        sys.stdout.write('0 = 0\n')
        return
    if (coeff[2] != 0):
        if (coeff[2] < 0):
            sys.stdout.write('- ')
        if (coeff[2] != 1):
            sys.stdout.write(str(abs(coeff[2])) + ' * ')
        sys.stdout.write('X^2')
        if (coeff[1] != 0 or coeff[0] != 0):
            if (coeff[1] < 0):
                sys.stdout.write(' - ')
            else:
                sys.stdout.write(' + ')
    if (coeff[1] != 0):
        if (coeff[1] != 1):
            sys.stdout.write(str(abs(coeff[1])) + ' * ')
        sys.stdout.write('X^1')
        if (coeff[0] != 0):
            if (coeff[0] < 0):
                sys.stdout.write(' - ')
            else:
                sys.stdout.write(' + ')
    if (coeff[0] != 0):
        sys.stdout.write(str(abs(coeff[2])))
    sys.stdout.write(' = 0')
    sys.stdout.write('\n')
    return

#main entry
def entry(arg):
    p1 = rmv_space(arg.split('=')[0]).lower()
    p2 = rmv_space(arg.split('=')[1]).lower()
    print('poly max deg')
    print(get_max_deg(arg))
    print(p1)
    print(p2)
    print('coeff list 1st poly :')
    print(get_coeff_list(p1))
    print('coeff list 2nd poly :')
    print(get_coeff_list(p2))
    print('coeff reduced form :')
    print_reduced(coeff_sub(get_coeff_list(p1),get_coeff_list(p2)))
    return

entry(sys.argv[1])
