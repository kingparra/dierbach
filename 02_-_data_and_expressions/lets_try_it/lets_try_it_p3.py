dir()
# OUT: ['__builtins__', '__doc__', '__name__', 'help']
[elem for elem in *__name__]
# OUT:   File "<input>", line 1
# OUT:     [elem for elem in *__name__]
# OUT:                       ^
# OUT: SyntaxError: invalid syntax
[elem for elem in __name__]
# OUT: ['_', '_', 'c', 'o', 'n', 's', 'o', 'l', 'e', '_', '_']
# Let's Try It, page 53
num = input('Enter number: ')
# OUT: Enter number: 5
num = int(input('Enter number: '))
# OUT: Enter number: 5
num = input('Enter name: ')
# OUT: Enter name: Chris
num = int(input('Enter name: '))
# OUT: Enter name: Chris
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     num = int(input('Enter name: '))
# OUT: ValueError: invalid literal for int() with base 10: 'Chris'