import sys
import re
import array as arr

if (len(sys.argv) != 2 or sys.argv[1].find('=') < 2): #exit if number of inline arguments is different than 1, or the polynomial expression does not contain a "="
    sys.exit()

#printing arguments infos
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('Argument 1:', str(sys.argv[1]))

#spliting expressions by '=' into two different variables
p1 = (sys.argv[1]).split('=')[0]
p2 = (sys.argv[1]).split('=')[1]

#printing both expressions
print('left expression=' + p1)
print('right expression=' + p2)

#get the polynomial degree
if ( sys.argv[1].find('x^2') >= 1 or sys.argv[1].find('X^2') >= 1):
    pol_deg = 2
    print('Polynomial degree: 2')
else:
    pol_deg = 1
    print('Polynomial degree: 1')

#expression to array of coefficients
def expr_to_array(exp,pol_deg):
    coef_arr = [0]*(pol_deg+1)
    print(coef_arr)
    arr = re.split('\+|-',exp)
    print('list of terms : ')
    print(arr)
    for i in arr:
        term_to_deg(coef_arr,i)
    return coef_arr

#return degree of term given as argument
def term_to_deg(coef_arr,term):
    if (term.find('X^1') != -1 or term.find('x^1') != -1):
        print(term.strip() + ' is 1st degree')
        return 1
    elif (term.find('X^2') != -1 or term.find('x^2') != -1):
        print(term.strip() + ' is 2nd degree')
        return 2
    print(term.strip() + ' is null degree')
    return 0

#left expression infos
expr_to_array(p1,pol_deg)