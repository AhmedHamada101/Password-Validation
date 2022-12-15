# edit
def is_valid(password):
    capital_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabets = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_char = "@#$"

    capital_alphabets_check = False
    small_alphabets_check = False
    digits_cheak = False
    special_char_check = False

    if len(password) < 6:
        print('The password must be at least 6 characters')
    elif len(password) > 12:
        print('The password must be maxed at 12 characters')
    else:
        for i in password:
            if i in capital_alphabets:
                capital_alphabets_check = True
            elif i in small_alphabets:
                small_alphabets_check = True
            elif i in digits:
                digits_check = True
            elif i in special_char:
                special_char_check = True

        if capital_alphabets_check is False:
            print('The password must be include capital letters')
        if small_alphabets_check is False:
            print('The password must be include small letters')
        if digits_check is False:
            print('The password must be include numbers')
        if special_char_check is False:
            print('The password must include symbols from(@,#,$)')

        if capital_alphabets_check and small_alphabets_check and digits_check and special_char_check:
            print('The password is acceptable')
        else:
            print('The password is not acceptable')


while True:
    password = input('Enter the password to check it  ==>  ')
    is_valid(password)

    while True:
        try:
            check_again = int(input("To check again enter [1] and to not check again enter [0]  ===>  "))
        except:
            print('Please, enter [0] or [1]')
        else:
            break

    if check_again == 1:
        continue
    else:
        print('Done')
        break
