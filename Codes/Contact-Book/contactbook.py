# Contact Book 

from pathlib import Path

print('                                            \n'
      '********************************************\n'
      "            Smart Contact Book              \n"
      '********************************************\n'
      'By Ayush Sehrawat (github.com/AyushSehrawat)\n'
      '********************************************\n'
      '                                              '
      '\n                                          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n'
      '  ==========================    ||          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n'
      ' ||                         ||  ||          \n')


def menu():
    print('\n\n\n                                      \n'
          '********************************************\n'
          "            Smart Contact Book              \n"
          '********************************************\n'
          'By Ayush Sehrawat (github.com/AyushSehrawat)\n'
          '********************************************\n'
          '                                            \n'
          '1- Add Contact\n2-See all contacts\n3-Remove all Contacts\n4-Exit')


main_list = []

while True:
    menu()
    main_choice = int(input('Choice: '))

    if main_choice == 1:
        tmp = []
        name = input('Name: ')
        tmp.append(name)
        try:
            number = int(input('Number: '))
            tmp.append(number)
        except:
            print('Something went wrong :(')
            number = None
            tmp.append(number)
        
        try:
            #
            email = input('Email: ')
            rel = input('Relation (Friend/Family/Others): ')
            tmp.append(email)
            tmp.append(rel)
        except:
            pass

        main_list.append(tmp)

    elif main_choice == 2:
        print('\n                                          \n'
              '********************************************\n')
        print(main_list)
        print('********************************************\n')

    elif main_choice == 3:
        main_list.clear()
    elif main_choice == 4:

        save = input('Do you want to save it?\n(Y)es or (N)o\n>>> ').upper()

        if save == 'Y':
            with open("contacts.txt", "a+") as file:
                data = Path('contacts.txt').stat().st_size
                file.write(f'\n{main_list}') if data else file.write(f'{main_list}')
                print('Check the same directory where this script is saved! ')
            break
        else:
            print('Thanks for using!')
            break
        


