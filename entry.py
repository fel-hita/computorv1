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

#spliting expressions by '=' into two different variables
p1 = rmv_space((sys.argv[1]).split('=')[0]).lower()
p2 = rmv_space((sys.argv[1]).split('=')[1]).lower()

#printing both expressions
print('left expression=' + p1)
print('right expression=' + p2)

#get the polynomial degree      
if ( sys.argv[1].find('x^2') == -1):
    pol_deg = 2
    print('Polynomial degree: 1')
else:
    pol_deg = 1
    print('Polynomial degree: 2')

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
    print('list of terms : ')
    print(arr)
    flag = 0
    for term in arr:
        if (term == '+'):
            flag = 0
        elif (term == '-'):
            flag = 1
        else:
            print(get_coeff(term,flag))
            if (term.find('x^1') != -1):
                coeff_list[1] += get_coeff(term,flag)
            elif (term.find('x^2') != -1):
                coeff_list[2] += get_coeff(term,flag)
            else:
                coeff_list[0] += get_coeff(term,flag)
    return coeff_list


#left expression infos
print(p1)
print('coeff list :')
print(get_coeff_list(p1))