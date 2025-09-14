history_file= "history.txt"

def show_history():
    file= open(history_file, "r")
    lines= file.readlines()
    if len(lines)== 0:
        print("No History found!")
    else:
        for line in reversed(lines): #for history in reverse order
            print(line.strip())
    file.close()

def clear_history():
    file= open(history_file, "w")
    file.close()
    print("History cleared!")
    
def save_to_history(equation, result):
    file= open(history_file, "a")
    file.write(equation + '=' + str(result) + '\n')
    file.close()

def calculate(user_input):
    for operator in ['+','-','*','/']:
        user_input= user_input.replace(operator, f' {operator} ') #for separating the user input
    parts= user_input.split() 

    if len(parts) != 3:
        print("Invalid input; use format- num operator num (e.g. 8+4)")
        return 
    
    try:
        num1= float(parts[0])
        op= parts[1]
        num2= float(parts[2])

    except ValueError:
        print("Invalid number in expression")
        return

    if op == '+':
        result= num1+ num2
    elif op == '-':
        result= num1- num2
    elif op == '*':
        result= num1* num2
    elif op == '/':
        if num2== 0:
            print("division by 0 is not possible!")
            return
        result= num1/ num2
    else:
        print("Invalid operation; use from [+,-,*,/]")
        return

    if int(result)== result: #result is a float value; for converting into integer
        result= int(result) 
    print(f"RESULT: {result}")
    save_to_history(user_input, result) #expression & result are not together

def main():
    print("---SIMPLE CALCULATOR---(type history, clear, exit)")
    while True:
        user_input= input("Enter expression or give order history, clear, exit:")
        if user_input== 'exit':
            print("GoodBye")
            break  
        elif user_input== 'clear':
            clear_history()
        elif user_input== 'history':
            show_history()
        else:
            calculate(user_input)
main()



