# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Westminster ID: w1962758
# Name : W.L.M. Isira Udam Wasala
# IIT Number :20200257
# Date: 04.21.2023

# progression_outcome takes in three integer arguments and their outcome
def results(pass_credits, defer_credits, fail_credits):
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif fail_credits >= 80:
        return "Exclude"
    else:
        return "Do not progress – module retriever"

# initialize counters
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
inputs = []

# PART 01
while True:
    try:
        # get student ID
        student_ID = input("enter your student ID here : ")
        
        # check the characters of the student_ID are equal to 8
        if len(student_ID) != 8:
            print("Invalid Input. Your student ID must have 8 characters")
            continue

        # get pass credits
        pass_credits = int(input("Please enter your pass credits : "))

        # check validity
        if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue

    # check value error
    except ValueError:
        print("Integer required. Program will run again !")
        continue

    try:
        # get defer credits
        defer_credits = int(input("Please enter your defer credits : "))

        # check validity
        if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            
    # check value error
    except ValueError:
            print("Integer required. Program will run again !")
            continue
    try:
        # get fail credits
        fail_credits = int(input("Please enter your fail credits : "))

        # check validity
        if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            
    # check value error        
    except ValueError:
        print("Integer required. Program will run again !")
        continue

    # checking the sum of all three values is NOT equal to 120
    if pass_credits + defer_credits + fail_credits != 120:
        print("Total incorrect.")
        continue

    # assume results to new variable called outcome
    outcome = results(pass_credits, defer_credits, fail_credits)

    # display the output
    print (outcome)

    # append a list of the progression outcome, pass credits, defer credits, and fail credits to the inputs list. 
    inputs.append([outcome, pass_credits, defer_credits, fail_credits])
    
    # update counters
    if outcome == "Progress":
        progress_count += 1
        
    elif outcome == "Progress (module trailer)":
        trailer_count += 1
       
    elif outcome == "Do not progress – module retriever":
        retriever_count += 1
            
    else:
        outcome == "Exclude"
        exclude_count += 1
        
    # ask user's choice
    # user can input 'Q' to exit and 'Y' to continue
    continue_exit = input("Do you want to continue the program? Press 'Y'\n Do you want to quit the program? Press 'Q' : ")

    # convert all the letters into simple letters
    lower_continue_exit = continue_exit.lower()
    
    if lower_continue_exit == 'q':
        break
    elif lower_continue_exit == 'y':
        continue
    else:
        
        # this runs, when user input other letter instead of 'Q' and 'Y'
        print ("invalid input")
        continue_exit = input("\nDo you want to continue the program?\n(press 'Q' to exit and 'Y' to continue) : ")
    
# print histogram
# assume the sum of pogress_count, defer_count, fail_count to the count_outcome

count_outcome = progress_count + trailer_count + retriever_count + exclude_count
print("----------------------------------------------------------")
print("Histogram")
print(f"Progress {progress_count} : {'*' * progress_count}")
print(f"Trailing {trailer_count }: {'*' * trailer_count}")
print(f"Retriever {retriever_count} : {'*' * retriever_count}")
print(f"Exclude {exclude_count} : {'*' * exclude_count}")
print(f"{count_outcome} outcomes in total")


# PART - 02
print ("\n----------------------------------------------------------")
print("\nPart 2:")

# This block of code loops through the list inputs and assigns the values of each sublist to outcome, pass_credits, defer_credits, and fail_credits.
for data in inputs:
    outcome = data[0]
    pass_credits = data[1]
    defer_credits = data[2]
    fail_credits = data[3]

    # print values in a formatted string.
    print(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")


# Part 03 - File Handling
# create new file
with open ('Outcome - Part 03.txt', 'w') as file:

    # write/input in the file
    file.write("part 03: \n")
    outcome = data[0]
    pass_credits = data[1]
    defer_credits = data[2]
    fail_credits = data[3]

    # write the results in the txt file
    file.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")

