#Ask the users for two numbers between 1 and 100. Then count from the lower number to the higher number. Print the results to the screen
num_1 = int(input('Please enter the first number from 1 to 100 \n' ))
num_2 = int(input('Please enter the second number from 1 to 100 \n' ))
while num_1 < 0 or num_2 < 0  or num_1 > 100 or num_2 > 100:
    print('Please enter a number within range')
    num_1 = int(input('Please enter the first number from 1 to 100 \n' ))
    num_2 = int(input('Please enter the second number from 1 to 100 \n' ))
    
if num_1 < num_2:
    for n in range( num_1, num_2 + 1):
        print(n, end = " ")
else: 
    for n in range( num_1, num_2 + 1):
        print(n, end = " ")