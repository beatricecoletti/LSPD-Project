'''
Ciao
 Comment the module goal here.
'''
 birthdays = {
     'Albert Einstein': '03/14/1879',
     'Benjamin Franklin': '01/17/1706',
     'Ada Lovelace': '12/10/1815',
     'Donald Trump': '06/14/1946',
     'Rowan Atkinson': '01/6/1955'}
def print_birthdays():
'''Comment the function.'''
print('Welcome to the birthday dictionary:') for name in birthdays:
print(name)
def return_birthday(name): '''Comment the function.''' if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

