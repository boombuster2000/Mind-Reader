print('I am Mystic Meredith, what is your name? ')
name = input()
print('Welcome ' + name +', I am going to read your mind') 
print('Think of a number between 1 and 10 ')
original_number = int(input()) # converts the input into int data type (you can't do mathematics to string)

# Says what the user has to do
print('Multipy it by 2')
input() # can press enter for next instruction when ready
print('Multiply it by 5')
input()
print('Divide it by the number you started with')
input()
print('Takeaway 7 from it')

# does the calculations
new_number = original_number*2
new_number = new_number *5
new_number = new_number/original_number
new_number = new_number - 7

print('Your new number is...')
input()
print(int(new_number)) # I put int() to remove the decimal place, can test without int func and see for yourself