def is_int(num):
    """ This function get a string and return that is it an integer or not """
    if num[0] == '-':
        for i in num[1:]:
            if not ((ord(i) >= 48) and (ord(i) <= 57)):
                return False
        return True
    else:
        for i in num:
            if not ((ord(i) >= 48) and (ord(i) <= 57)):
                return False
        return True


def isint(num):
    """ This function get a string and return that is it an integer or not """
    if num == '' or num == ' ':
        return False
    if num[0] == '-':
        if not str.isdigit(num[1:]):
            return False
        return True
    if not str.isdigit(num):
        return False
    return True


def is_float(num):
    """ This function get a string and return that is it a float or not """
    if num == '' or num == ' ':
        return False
    f = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = 0
    if num[0] == '-':
        for i in num[1:]:
            if i == '.':
                c += 1
            if i not in f and c != 1:
                return False
        if c == 1 or c == 0:
            return True
        return False
    else:
        for i in num:
            if i == '.':
                c += 1
            if i not in f and c != 1:
                return False
        if c == 1 or c == 0:
            return True
        return False


def for_error():
    msg = ['Please enter correctly !! ', 'Please enter a valuable number !! ', 'This is an error enter correctly !! ',
           'You must enter correctly !! ', 'Please reenter a valuable number !! ']
    import random
    rng = random.Random()
    print(msg[rng.randrange(0, 5)])


def reverse(n):
    s = 0
    c = 0
    if n < 0:
        n = n * (-1)
        c = 1
    while n / 10 != 0:
        s = s * 10 + n % 10
        n = n // 10

    if c == 1:
        return -1 * s
    else:
        return s


def is_alpha(name):
    """ This function get a string and return that are the all indexes are char  """
    if name == '' or name == ' ':
        return False
    names = name.split()
    for name in names:
        for i in name:
            if not (((ord(i) >= 97) and (ord(i) <= 122)) or ((ord(i) >= 57) and (ord(i) <= 90))):
                return False
    return True

def get_int_number():
    while True:
        number = input('Please enter an integer number : ')
        if not isint(number):
            for_error()
            continue
        break
    return int(number)

def get_float_number():
    while True:
        number = input('Please enter a float number : ')
        if not is_float(number):
            for_error()
            continue
        break
    return float(number)

def get_alpha_str():
    while True:
        name = input('Please enter a name : ')
        if not is_alpha(name):
            for_error()
            continue
        break
    return name


