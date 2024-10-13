# basic_calculator
#Created basic calculator that performs mathematical calculations and equation solver (solves for x).
print("Welcome to the calculator!") 

#Ask user for first number
first_num = float(input("Enter your first number: ")) 
print(f'Your first number is {first_num}')

#Ask user for second number
second_num = float(input("Enter your second number: "))
print(f'Your second number {second_num}')

print("Enter you operation: ")

print('1: Add')

print('2: Subtract')

print('3: Multiply')

print('4: Divide')

print('5: Exponent')

#Ask user to choose an operation
operation = int (input("> ")) 

print (f'You have chosen operation #{operation}')

#Blocking other options 
if operation < 1:
    print("Invalid operation")
    quit()

if operation > 5:
    print("Invalid operation")
    quit()

#Conditions for calculations
if operation == 1:
    result = first_num + second_num

    #Change for float type output
    float_value = float(result)
    print(f'{first_num} + {second_num} = {float_value}')
    
    #Change for integer type output
    integer_value = int(result)
    print(f'Answer: {integer_value}')

elif operation == 2:
    result = first_num - second_num
    
    #Change for float type output
    float_value = float(result)
    print(f'{first_num} - {second_num} = {float_value}')
    
    #Change for integer type output
    integer_value = int(result)
    print(f'Answer: {integer_value}')

elif operation == 3:
    result = first_num * second_num
    
    #Change for float type output
    float_value = float(result)
    print(f'{first_num} * {second_num} = {float_value}')
    
    #Change for integer type output
    integer_value = int(result)
    print(f'Answer: {integer_value}')

elif operation == 4:
    result = first_num / second_num
    
    #Change for float type output
    float_value = float(result)
    print(f'{first_num} / {second_num} = {float_value}')
    
    #Change for integer type output
    integer_value = int(result)
    print(f'Answer: {integer_value}')

else:
    result = first_num ** second_num
    
    #Change for float type output
    float_value = float(result)
    print(f'{first_num} ** {second_num} = {float_value}')
    
    #Change for integer type output
    integer_value = int(result)
    print(f'Answer: {integer_value}')
