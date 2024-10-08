#Code checks if a number is positive or negetaive


x = int(input('Enter a number: '))

if x//1 > 0:

    print(f'{x} is a positive number')

elif x//1 < 0:

    print('x is a a negative number')
    
else:

    print("Input a number.")   


   ''' #Find the largest number between 3 inputs

x = int (input('Enter a number: '))
y = int (input('Enter a number: '))
z  = int (input('Enter a number: '))

if x>y & x>z:
    
    print(f'{x} is the greatest number.') 

elif y>z & y>x:

    print(f'{y} is the greatest number.')

elif z>x&z>y:

    print(f'{z} is the greatest number.')

else:
    print('They are equal.') '''
