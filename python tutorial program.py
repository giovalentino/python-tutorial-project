choice = 0
#choices ng user
while choice != 6:
    print()
    print("======== PYTHON TUTORIAL ========")
    print("1. INTRODUCTION TO PROGRAMMING")
    print("2. BASIC SYNTAX")
    print("3. ARITHMETIC OPERATORS")
    print("4. VARIABLES AND DATA TYPES")
    print("5. EXERCISE QUIZ")
    print("6. EXIT")
    print("=================================")
    print()

    choice = int(input("Choose lesson: "))

#choice 1 introduction
    if choice == 1:
        print()
        print("===== INTRODUCTION TO PROGRAMMING =====")
        print("Programming is the process of creating instructions")
        print("that a computer follows.")
        print("Python is a programming language.")
        print("=================================")

#choice 2 basic syntax in python
    elif choice == 2:
        print()
        print("===== BASIC SYNTAX =====")
        print("Python syntax refers to the rules of Python.")
        print()
        print('Example: print("Hello World")')
        print()
        print("The print() function displays output.")
        print("=================================")

#choice 3 arithmetic operators
    elif choice == 3:
        print()
        print("===== ARITHMETIC OPERATORS =====")
        print("Addition: +")
        print("Subtraction: -")
        print("Multiplication: *")
        print("Division: /")
        print()
        print("Example:")
        print("Addition: 10 + 5 =", 10 + 5)
        print("Subtraction: 10 - 5 =", 10 - 5)
        print("Multiplication: 10 * 5 =", 10 * 5)
        print("Division: 10 / 5 =", 10 / 5)
        print("=================================")

#choice 4 variables and data types
    elif choice == 4:
        print()
        print("===== VARIABLES AND DATA TYPES =====")
        print("A variable is a container for storing data values.")
        print("Data Types indicate the type of value a variable holds.")
        print()
        print("Common Data Types:")
        print("1. String (str) - Text: name = 'Alice'")
        print("2. Integer (int) - Whole numbers: age = 20")
        print("3. Float (float) - Decimals: price = 19.99")
        print("4. Boolean (bool) - True or False")
        print("=======================================")

#choice 5 exercise quiz with aasnwers review
    elif choice == 5:
        print()
        print("===== PYTHON EXERCISE QUIZ =====")
        score = 0

#question 1
        q1 = input("1. What function is used to display output in Python? ")
        q1_correct = "print()"
        q1_is_correct = q1 == q1_correct
        if q1_is_correct:
            score += 1

        print()
#question 2
        q2 = input("2. What symbol is used for multiplication in Python? (* or x): ")
        q2_correct = "*"
        q2_is_correct = q2 == q2_correct
        if q2_is_correct:
            score += 1

        print()
        print("========== QUIZ RESULT & REVIEW ==========")
        print(f"Your Total Score: {score} out of 2")
        print()
        print("=== Review Your Answers ===")

#review q1
        print("Q1: What function is used to display output in Python?")
        print(f"Your answer: {q1}")
        print(f"Correct answer: {q1_correct}")
        print("Status:", "Correct" if q1_is_correct else "Wrong")
        print()

#review q2
        print("Q2: What symbol is used for multiplication in Python?")
        print(f"Your answer: {q2}")
        print(f"Correct answer: {q2_correct}")
        print("Status:", "Correct" if q2_is_correct else "Wrong")
        print("==========================================")
#choice 6 exit or done
    elif choice == 6:
        print()
        print("Thank you for using Python Tutorial!")
        print()
#invlaid code
    else:
        print()
        print("Invalid choice. Please choose 1 to 6.")

