#!/usr/bin/python3.9

import sys
import re
import array as arr

if (len(sys.argv) != 2 or sys.argv[1].find('=') == -1):
    print('Please write down a valid and only one polynomial argument.')
    sys.exit()

def rmv_space(string): 
    return string.replace(" ", "")

def my_min(a,b):
    if (a>=b):
        return a
    return b

def my_max(a,b):
    if (a>=b):
        return a
    return b

def my_sqrt(n):
    sgn = 0
    if n < 0:
        sgn = -1
        n = -n
    val = n
    while True:
        last = val
        val = (val + n / val) * 0.5
        if my_abs(val - last) < 1e-9:
            break
    if sgn < 0:
        return -val
    return val

def my_comp(disc):
    return complex(my_sqrt(-disc),1)

def my_abs(nbr):
    if (nbr == 0):
        return (0)
    elif (nbr > 0):
        return (nbr)
    return (-nbr)

def my_pow2(nbr):
    return (nbr*nbr)
      
def get_max_deg(coeff):
    if (coeff[0] == 0 and coeff[1] == 0 and coeff[2] == 0):
        return (-1)
    elif (coeff[2] != 0):
        return (2)
    elif (coeff[1] != 0):
        return (1)
    else:
        return (0)

def is_float(term):
    if (term.find('.') == -1):
        return False
    return True

def to_number(term):
    if(is_float(term)):
        return float(term)
    return int(term)

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

def get_coeff_list(exp):
    coeff_list = [0, 0, 0]
    arr = re.split('(\+|-)',exp)
    flag = 0
    for term in arr:
        if (term == ''):
            continue
        elif (term == '+'):
            flag = 0
        elif (term == '-'):
            flag = 1
        else:
            if (term.find('x^2') != -1):
                coeff_list[2] += get_coeff(term,flag)
            elif (term.find('x^1') != -1):
                coeff_list[1] += get_coeff(term,flag)
            elif (term.find('x^0') != -1):
                coeff_list[0] += get_coeff(term,flag)
            elif (term.find('x') != -1):
                coeff_list[1] += get_coeff(term,flag)
            else:
                coeff_list[0] += get_coeff(term,flag)
    return coeff_list

def is_null(coeffs):
    for elem in coeffs:
        if (elem != 0):
            return 0
    return 1

def coeff_sub(coeff1,coeff2):
    if (is_null(coeff1) and is_null(coeff2)):
        return ([0,0,0])
    elif (is_null(coeff2)):
        return (coeff1)
    elif (is_null(coeff1)):
        return (coeff2)
    final_coeff = [0,0,0]
    final_coeff[0] = coeff1[0] - coeff2[0]
    final_coeff[1] = coeff1[1] - coeff2[1]
    final_coeff[2] = coeff1[2] - coeff2[2]
    return (final_coeff)

def print_reduced(coeff):
    if (is_null(coeff)):
        sys.stdout.write('\u001b[36mll the real numbers are solution\n')
        return

    if (coeff[2] != 0):
        if (coeff[2] < 0):
            sys.stdout.write('\u001b[32;1m- ')
        if (abs(coeff[2]) != 1):
            sys.stdout.write('\u001b[32;1m' + str(abs(coeff[2])) + '\u001b[37;1m * \u001b[0m')
        sys.stdout.write('\u001b[32;1mX^2 \u001b[0m')
    if (coeff[1] != 0):
        if (coeff[1] < 0):
            sys.stdout.write('\u001b[35;1m- ')
        else:
            if (coeff[2] != 0):
                sys.stdout.write('\u001b[35;1m+ ')
    if (coeff[1] != 0):
        if (abs(coeff[1]) != 1):
            sys.stdout.write('\u001b[35;1m' + str(abs(coeff[1])) + '\u001b[37;1m * \u001b[0m')
        sys.stdout.write('\u001b[35;1mX \u001b[0m')
    if (coeff[0] != 0):
        if (coeff[0] < 0):
            sys.stdout.write('- ')
        else:
            sys.stdout.write('+ ')
    if (coeff[0] != 0):
        sys.stdout.write('\u001b[34;1m' + str(abs(coeff[0])) + ' \u001b[0m')
    sys.stdout.write('\u001b[37;1m= 0\u001b[0m')
    sys.stdout.write('\n')
    return

def disc(coeff):
    print('\u001b[36mDiscriminant Δ = \033[0m' + str(my_pow2(coeff[1])-4*coeff[2]*coeff[0]))
    return (my_pow2(coeff[1])-4*coeff[2]*coeff[0])

def solve1(coeff):
    sol = -coeff[0]/coeff[1]
    if (coeff[1] != 0):
        b = coeff[1]
        c = coeff[0]
        print('\u001b[35;1mb = \033[0m' + str(b) + '\u001b[34;1m c = \033[0m' + str(c))
        print('\u001b[36m One solution : \033[0m')
        if (sol == 0):
            sol = 0.0
        print('\u001b[31m X = ' + str(sol) +'\033[0m')
    return

def solve2(coeff):
    d = disc(coeff)
    if (d < 0):
        a = coeff[2]
        b = coeff[1]
        c = coeff[0]
        print('\u001b[32;1ma = \033[0m' + str(a) + '\u001b[35;1m b = \033[0m' + str(b) + '\u001b[34;1m c = \033[0m' + str(c))
        discr = my_pow2(b)-4*a*c
        print('\u001b[36m Two complex solutions \u001b[33mX1\033[0m,\u001b[31mX2 \033[0m: ')
        temp1 = complex(0,my_sqrt(my_abs(d)))
        temp2 = 2 * a
        sol=(-b+temp1)/temp2
        print('\u001b[33m X1 = (' + str(-b) + ' / ' + str(temp2) + ') + (√' + str(my_abs(d)) + ' / ' + str(temp2) + ') * j''\033[0m')
        print('\u001b[33m X1 = ' + str(sol))
        temp1 = complex(0,my_sqrt(my_abs(d)))
        sol=(-b-temp1)/temp2
        print('\u001b[31m X2 = (' + str(-b) + ' / ' + str(temp2) + ') - (√' + str(my_abs(d)) + ' / ' + str(temp2) + ') * j''\033[0m')
        print('\u001b[31m X2 = ' + str(sol))
    elif (d == 0):
        a = coeff[2]
        b = coeff[1]
        print('\u001b[32;1ma = \033[0m' + str(a) + '\u001b[35;1m b = \033[0m' + str(b))
        print('\u001b[36m One solution \u001b[33m-b/2a \033[0m:')
        sol = -coeff[1]/2*coeff[2]
        if(sol == 0):
            sol = 0.0
        print('\u001b[33m X = ' + str(sol) +'\033[0m')
    else:
        a = coeff[2]
        b = coeff[1]
        c = coeff[0]
        print('\u001b[32;1ma = \033[0m' + str(a) + '\u001b[35;1m b = \033[0m' + str(b) + '\u001b[34;1m c = \033[0m' + str(c))
        discr = my_pow2(b)-4*a*c
        print('\u001b[36m Two solutions \u001b[33mX1\033[0m,\u001b[31mX2 \033[0m: ')
        temp1=-b+my_sqrt(discr)
        temp2=2*a
        sol=temp1/temp2
        print('\u001b[33m X1 = ' + str(sol) +'\033[0m')
        temp1=-b-my_sqrt(discr)
        sol=temp1/temp2
        print('\u001b[31m X2 = ' + str(sol) +'\033[0m')
    return

def err_syn(arg):
    err_list = []
    err = 0
    last_char = ''
    flag_can_frac = 1
    flag_sign = 0
    flag_frac = 1
    flag_mp = 1
    flag_x = 0
    flag_exp = 0
    flag_nbr = 0
    flag_eq = 1

    sys.stdout.write('\nInput : ')
    for char in arg:
        if(char == '+' or char == '-'):
            if(flag_sign == 1 or flag_exp == 1):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(1))
                err += 1
            else:
                flag_can_frac = 1
                flag_eq = 1
                flag_x = 0
                flag_sign = 1
                flag_nbr = 0
                flag_frac = 1
                sys.stdout.write(char)
        elif(char == '*'):
            if (flag_mp == 1 or flag_frac == 1):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(2))
                err += 1
            else:
                flag_eq = 1
                flag_mp = 1
                flag_sign = 0
                sys.stdout.write(char)
        elif(char == 'x'):
            if(flag_x == 1):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(3))
                err += 1
            else:
                flag_eq = 0
                flag_x = 1
                flag_sign = 0
                flag_mp = 0
                flag_nbr = 1
                flag_frac = 1
                sys.stdout.write(char)
        elif(char == '^'):
            if(flag_exp == 1):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(4))
                err += 1
            elif(flag_x == 0):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(4))
                err += 1
            else:
                flag_eq = 0
                flag_frac = 1
                flag_exp = 1
                flag_nbr = 1
                flag_sign = 0
                sys.stdout.write(char)
        elif(char.isnumeric()):
            flag_eq = 0
            if(flag_exp == 1):
                if(char != '0' and char != '1' and char != '2'):
                    sys.stdout.write('\u001b[31m' + char + '\033[0m')
                    err_list.append(err_out(5))
                    err += 1
                else:
                    sys.stdout.write(char)
                flag_exp = 0
                flag_nbr = 1
                flag_sign = 0
            else:
                flag_mp = 0
                if(flag_sign == 1):
                    flag_sign = 0
                    flag_nbr = 0
                    flag_frac = 0
                    sys.stdout.write(char)
                elif(flag_nbr == 1):
                    sys.stdout.write('\u001b[31m' + char + '\033[0m')
                    err_list.append(err_out(6))
                    err += 1
                else:
                    flag_frac = 0
                    sys.stdout.write(char)
        elif(char == '='):
            if(flag_eq == 1 or flag_exp == 1):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(7))
                err += 1
            else:
                flag_can_frac = 1
                flag_frac = 1
                flag_x = 0
                flag_nbr = 0
                flag_eq = 1
                sys.stdout.write(char)
        elif(char == '.'):
            if(flag_frac == 1 or flag_mp == 1 or flag_can_frac == 0):
                sys.stdout.write('\u001b[31m' + char + '\033[0m')
                err_list.append(err_out(8))
                err += 1
            else:
                flag_can_frac = 0
                flag_frac = 1
                flag_sign = 0
                sys.stdout.write(char)
        elif(char == ' '):
            continue
        else:
            sys.stdout.write('\u001b[31m' + char + '\033[0m')
            err_list.append(err_out(9))
            err += 1
        last_char = char
        
    if (last_char == '=' or last_char == '+' or last_char == '-' or last_char == '^'):
        if (err == 0):
            err += 1
        sys.stdout.write('\nInvalid \u001b[31mend\033[0m of polynom.\n')
    if (err > 0):
        sys.stdout.write('\nPlease fix the highlighted \u001b[31m')
        if (err == 1):
            sys.stdout.write('\033[0merror.\u001b[31m\n')
        else:
            sys.stdout.write(str(err) + '\033[0m errors.\u001b[31m\n')
        print(*err_list, sep='\033[0m, \u001b[31m')
    else:
        sys.stdout.write('\nYour input syntax is\u001b[32m valid.\033[0m\n')
    return(err)

def err_out(err_nb):
    if (err_nb == 1):
        return ('Sign')
    elif (err_nb == 2):
        return ('Multiplication')
    elif (err_nb == 3):
        return ('Inderterminant')
    elif (err_nb == 4):
        return ('Exponent')
    elif (err_nb == 5):
        return ('Exponent power ([0,2])')
    elif (err_nb == 6):
        return ('Numerical')
    elif (err_nb == 7):
        return ('Equal sign')
    elif (err_nb == 8):
        return ('Fraction')
    return ('Error.')

def main(arg):
    err = err_syn(arg.lower())
    if (err != 0):
        return
    p1 = rmv_space(arg.split('=')[0]).lower()
    p2 = rmv_space(arg.split('=')[1]).lower()
    coeff1 = get_coeff_list(p1)
    coeff2 = get_coeff_list(p2)
    final_coeff = coeff_sub(coeff1,coeff2)
    deg = get_max_deg(final_coeff)
    if (coeff1 == coeff2):
        print('\u001b[36mAll the real numbers are solution\033[0m')
        return
    elif (deg == -1):
        print('\u001b[36mBut please input a none-null linear or quadratic polynomial equation\033[0m')
        return
    elif (deg != 1 and deg != 2):
        print('\u001b[36mBut please input a valid linear or quadratic polynomial equation\033[0m')
        return
    elif (deg == 1):
        print('\u001b[36mThe polynom is linear\033[0m')
    elif (deg == 2):
        print('\u001b[36mThe polynom is quadratic\033[0m')
    sys.stdout.write('\u001b[36mAcquiring coefficient list for 1st poly : \033[0m')
    print(coeff1)
    sys.stdout.write('\u001b[36mAcquiring coefficient list for 2nd poly : \033[0m')
    print(coeff2)
    sys.stdout.write('\u001b[36mFinal polynomial coefficient reduced list : \033[0m')
    print(final_coeff)
    sys.stdout.write('\u001b[36mPolynomial reduced form : \033[0m')
    print_reduced(final_coeff)
    if (deg == 1):
        solve1(final_coeff)
    elif (deg == 2):
        solve2(final_coeff)
    return

   
if __name__ == "__main__":
    main(sys.argv[1])