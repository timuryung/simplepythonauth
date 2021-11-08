login = 'admin'
password = '123'

logininput = input('You login: ')
if logininput == login:
    passwordinput = input('Your password: ')
    if passwordinput == password:
          print('Success!')
    else:
        print('Failed!')
else:
    print('Failed!')

    
