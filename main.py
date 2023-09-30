# This is a sample Python script.

import random
import string
lngth = 0
password = ''




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('How long do you want the password to be?')
    passwordLength = int(input())
    while lngth < passwordLength:
        ranNum = random.randint(0,1)
        if (ranNum == 0):
            password += random.choice(string.ascii_letters)
        else:
            password += str(random.randint(0, 9))
        lngth += 1
    print(password)