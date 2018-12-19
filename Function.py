# Give the user a list of available commands
print('commands: \n    1; square a number\n    2; print a string\n    3; optional parameters\n    4; double function\n    q: quit')

#Ask the user what command to use
command = None


while command != 'q':
    command = input('Choose the number of your command: ')

    if command == '1':
        number = int(input('Enter a number you want to square: ' ))

        def user_num(number):
            numbersq = number ** 2
            return numbersq

        print('You entered: ' , number)
        print(number , 'squared is', user_num(number))

    elif command == '2':
        def string_print(string = None):
            string = input('Type a word or phrase: ')
            return string
        print(string_print())


    elif command == '3':
        def default_parameters(h, e, l, ll='L', o='O'):
            h= 'H'
            e = 'E'
            l = 'L'
            return h, e, l, ll, o

        print(default_parameters('H', 'E', 'L'))

    elif command == '4':
        #FIXME finish this command option
        initial = int(input('Enter an integer: '))
        def half_int(initial):
            num = initial / 2
            return num

        new_num = half_int(initial)
        print('Half of your number is:' , new_num)

        def num_by_4(new_num):
            result = new_num * 4
            return result
        print('4 times the new number is:' , num_by_4(new_num))


    else:
        print('Please use a valid command from above.')


print('Thank you for playing, Goodbye!')

