user_name= input("Enter your name: ")
print(f"Hey {user_name}! Welcome to my Python quiz!!")

while True:
    play= input("Do you want to play this quiz? (yes/no): " ).lower()
    if play== "yes":
        break
    elif play== "no":
        print("Alright, may be next time!!")
        break
    else:
        print("please enter a valid input (yes/no)!!")
    

if play== "yes":
    print("Okayy!! let's play")
    score= 0

    answer= input("Ques1. What is the correct way to write comment in python? " \
    "\n(A). // comment" \
    "\n(B). # comment" \
    "\n(C). -- comment" \
    "\n(D). /*comment*/" \
    "\nEnter the correct option: ").upper()
    if answer== "B":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques2. Which of the following is used to define a  function in python? " \
    "\n(A). fun" \
    "\n(B). function" \
    "\n(C). def" \
    "\n(D). define" \
    "\nEnter the correct option: ").upper()
    if answer== "C":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques3. What is output of print(type(20)) in python? " \
    "\n(A). <class 'str'>" \
    "\n(B). <class 'float'>" \
    "\n(C). <class 'int'>" \
    "\n(D). <class 'double'>" \
    "\nEnter the correct option: ").upper()
    if answer== "C":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques4. What is the result of print(5//2) in python? " \
    "\n(A). 2.5" \
    "\n(B). 2" \
    "\n(C). 3" \
    "\n(D). 2.0" \
    "\nEnter the correct option: ").upper()
    if answer== "B":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")
    
    answer= input("Ques5. Which of the following is a valid variable name? " \
    "\n(A). 2num" \
    "\n(B). num_2" \
    "\n(C). num-2" \
    "\n(D). num 2" \
    "\nEnter the correct option: ").upper()
    if answer== "B":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques6. What does len() function do? " \
    "\n(A). returns the last element of the list" \
    "\n(B). returns the length of the string or list" \
    "\n(C). converts strings to list" \
    "\n(D). returns memory size" \
    "\nEnter the correct option: ").upper()
    if answer== "B":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques7. What data type is immutable in python? " \
    "\n(A). list" \
    "\n(B). set" \
    "\n(C). dictionary" \
    "\n(D). tuple" \
    "\nEnter the correct option: ").upper()
    if answer== "D":
        print("Correct!!")
        score +=  1
    else:
        print("Wrong!!")

    answer= input("Ques8. What is the output of print(bool(""))? " \
    "\n(A). True" \
    "\n(B). False" \
    "\n(C). Error" \
    "\n(D). None" \
    "\nEnter the correct option: ").upper()
    if answer== "B":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques9. Which keyword is used to handle exceptions? " \
    "\n(A). handle" \
    "\n(B). catch" \
    "\n(C). except" \
    "\n(D). try-catch" \
    "\nEnter the correct option: ").upper()
    if answer== "C":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    answer= input("Ques10. What will range(3) return? " \
    "\n(A). [0, 1, 2]" \
    "\n(B). (0, 1, 2)" \
    "\n(C). range(0, 3)" \
    "\n(D). 0 1 2" \
    "\nEnter the correct option: ").upper()
    if answer== "C":
        print("Correct!!")
        score += 1
    else:
        print("Wrong!!")

    print(f"Your total score is {score} out of 10!!")
