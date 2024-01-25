# Calculator 

# def lookTheStr(num1 ,num2,qst):
#     if qst == '+':
#         num3 = num1 + num2
#     elif qst == '-':
#         num3 = num1 - num2
#     elif qst == '*':
#         num3 = num1 * num2
#     elif qst == '/':
#         if num1 and num2 == 0:
#             print('You can\'t divide 0 by 0,choice another number') 
#         else: 
#             num3 = num1 / num2      
#     else:
#         qst = input('What is the symbol: +, -, *, /')
#     print(f'The calculator find {num3}')
        
    
# aws = True 
    
# while aws:
#     number_one = float(input('Type the first one number:')) 
#     str_question = str(input('What is the symbol: +, -, *, / :'))
#     number_two = float(input('Type the second number:'))  
    
#     lookTheStr(number_one,number_two,str_question)
    
#     question = str(input('Do you want go ahead?Type y to yes or n to no')).lower()[0]
#     if question == 'n':
#         aws = False
#     elif question == 'y':
#         aws = True
        
    

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():


    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
 
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        num1 = answer
    else:
        should_continue = False
calculator()