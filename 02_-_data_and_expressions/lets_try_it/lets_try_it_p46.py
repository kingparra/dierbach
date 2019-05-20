# Let's Try It, p. 46
print('Hello World!')
# OUT: Hello World!
print('Hello World\n')
# OUT: Hello World
print('Hello World\n\n')
# OUT: Hello World
print('\nHello World')
# OUT: Hello World
print('Hello\nWorld')
# OUT: Hello
# OUT: World
print('Hello\n\nWorld')
# OUT: Hello
# OUT: World
print(r'Hello\n\nWorld') # Testing out raw strings
# OUT: Hello\n\nWorld
print(1, '\n', 2, '\n', 3)
# OUT: 1 
# OUT:  2 
# OUT:  3
print('\n', 1, '\n', 2, '\n', 3)
# OUT:  1 
# OUT:  2 
# OUT:  3
# The space before each character appear because print() seperates elements
# with a space by deafult. This can be overriden by specifying the 'sep'
# paramater of the print function.
