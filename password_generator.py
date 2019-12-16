import random as r

#chars to be used to generate random password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$%&*'

#alphabets to be used as 4 initials in e_id
alph = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#number and special characters to be used after alphabets in e_id
num_spc='0123456789@$%&*'

#input the length of password you want
length = int(input('password length?'))

#number of students for whom id and password to be generated
for l in range(1,31):
    e_id = ''
    alp = ''
    ns = ''
    password = ''
    
    #first 4 random initials of e_id is alphabets
    for i in range(4):
        alp += r.choice(alph)
    #next 3 can be number of special character
    for x in range(3):
        ns += r.choice(num_spc)
    #email_id
    e_id = alp+ns+'@gmail.com'
    print('email_id of roll no',l, e_id)

    #to generate password according to given length
    for c in range(length):
       password += r.choice(chars)
    print('Password of roll no',l, password)
