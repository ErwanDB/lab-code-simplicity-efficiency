"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

# Define lists
numbers = ['zero','one','two','three','four','five']
operation = ['plus','minus']

# Define functions for player inputs
def player_a():
    a = input('Please choose your first number (zero to five): ')
    
    while a not in numbers:
        print('Number needs to be between zero and five and written with letters')
        a = input('Please choose your second number (zero to five): ')
    
    a = numbers.index(f'{a}')
    
    return a
        
def player_b():
    b = input('What do you want to do? plus or minus: ')
    while b not in operation:
        print('please choose between plus or minus and write it in letters')
        b = input('What do you want to do? plus or minus: ')
        
    return b
                
def player_c():
    c = input('Please choose your second number (zero to five): ')
    
    while c not in numbers:
        print('Number needs to be between zero and five and written with letters')
        c = input('Please choose your second number (zero to five): ')
        
    c = numbers.index(f'{c}')
    
    return c

# Define function for game execution
def calculator(a,b,c):
    if b == 'plus':
        return a+c
    elif b == 'minus':
        return a-c

# Game execution    
    
a = player_a()
b = player_b()
c = player_c()

print(f'the result of {a} {b} {c} is: ',calculator(a,b,c))


print("Thanks for using this calculator, goodbye :)")
