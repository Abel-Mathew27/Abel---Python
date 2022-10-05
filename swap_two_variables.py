#python program to swap two variables

#to take input from the user
x= float(input('Enter value of x: '))
y= float(input('Enter value of y: '))

#create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swaping: {}'.format(x))
print('the value of y after swaping: {}'.format(y))
