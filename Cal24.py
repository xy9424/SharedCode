# -*- coding: UTF-8 -*-

from UtilArray import EnhancedArray

successfulSteps = []
resultSteps = []

# Display final result
def display_result():
    global resultSteps
    print(resultSteps)
    return

# Save final result
def save_result():
    successfulSteps.append(resultSteps.copy())
    return

# Clear temp steps
def clear_steps():
    resultSteps.clear()
    return

# Get four input numbers.
def get_input_data():
    listNumbers = []
    print ("Input 4 numbers, separate by , :")
    # When count of list is not 4, let user input again.
    while(len(listNumbers) !=4):
        # Get input data from keyboard
        inputNumbers = input()
        # Transform input data to list by ","
        listNumbers = inputNumbers.split(",")
        print(listNumbers)
        numberCount = len(listNumbers)
        if (numberCount !=4):
            print("You shall only input %d numbers. " %(numberCount))
            print("Please input 4 numbers, separate by , :")
    
    return listNumbers

# Check if the next few steps can reach 24
def is_still_possible ():
    return True

# Check if reulst is 24
def is_24(result):
    isSuccess = False
    # Check if result is close to 24
    if (result > 23.99999 and result < 24.00001):
        save_result()
        # For debug purpose, to print good result after each successful try.
        # print("result is 24")
        # display_result()
        isSuccess = True
    else:
        isSuccess= False
    return isSuccess
  
# Record the step of the latest calculation
def record_step(numberA, numberB, operation, result):
    global resultSteps
    # A+B and B+A, A*B and B*A are considered as the same.
    if (operation =="+" or operation =="*"):
        if (numberB<numberA):
                temp = numberA
                numberA = numberB
                numberB = temp
    resultSteps.append("%.2f %s %.2f = %.2f" %(numberA, operation, numberB, result))

# Remove the latest step
def remove_step():
    global resultSteps
    resultSteps.pop()

# Filter out duplicated solutions
def filter_duplication():
    global successfulSteps
    successfulSteps = EnhancedArray.distinct_list(successfulSteps)

# Print final result
def print_all_successful_solutions():
    global successfulSteps
    for solution in successfulSteps:
        print(solution)

# A better way to calculate. Cover more scenarios include effect of "()" for priority
# Receive two numbers for calculation
# Try four different way to calcualte result
# Combine result with recieved remaining list as a new list
# Call calculate24_new, consider to calculate with 4->3->2 numbers
availableOperationList = ["+","-","*","/"]
def one_operation_new(calNumberA, calNumberB, listNumbers):
    global availableOperationList
     
    result = 0.0

    # Validate calNumbers
    try:
        numberA = float(calNumberA)
        numberB = float(calNumberB)
    except Exception:
        raise Exception("%s or %s is not a number : " %(str(calNumberA), str(calNumberB)))

    # Two numbers are ready for calculation.
    # Get one calculation operation.
    # Try 4 kinds of calculation
    for calculateOperation in availableOperationList:
        if calculateOperation == "+":
            result = numberA + numberB
        elif calculateOperation == "-":
            result = numberA - numberB
        elif calculateOperation == "*":
            result = numberA * numberB
        elif calculateOperation == "/":
            # If divide by 0, skip the divide, continue try other operations
            if numberB == 0:
                continue
            else:
                result = numberA / numberB
        # Record current operation step in the trace
        record_step(numberA, numberB, calculateOperation,result)
        # Compose new list with less element
        nextList = listNumbers.copy()
        nextList.append(result)
        # The problem converts to calculate24 with less element.
        calculate24_new(nextList)
        # Remove last step in the trace
        remove_step()

# Get a list of number, select two numbers from it
# Send two numbers to one_operation_new to calculate a result
# Send remaining list to one_operation_new too
# Then one_operation_new will combine the result with remaining list as a new list
# Call calculate24_new with the new shorter list
def calculate24_new(listNumbers):
    i=0
    j=0

    lengthOfList = len(listNumbers)

    # Validate if it is a 0 length list
    if(lengthOfList ==0):
        raise Exception("No number in the list during calculation.")
    # If the length is 1, means it is the end of this calculation for 24.
    if(lengthOfList==1):
        # Validate the result, and end this round of calculation
        return is_24(listNumbers[0])
    elif (lengthOfList>=2):
        # If more than or equals 2 numbers in the list
        # Get all kinds combination of number 
        # Call one_operation_new for the all possible calculation types.
        for i in range(lengthOfList):
            firstCalNumber = listNumbers[i]
            secondListNumbers = listNumbers.copy()
            del secondListNumbers[i]
            for j in range(len(secondListNumbers)):
                secondCalNumber = secondListNumbers[j]
                remainingListNumbers = secondListNumbers.copy()
                del remainingListNumbers[j]
                one_operation_new(firstCalNumber, secondCalNumber, remainingListNumbers)
            
if __name__ == "__main__":
    listNumbers = get_input_data()
    calculate24_new(listNumbers.copy())
    filter_duplication()
    print_all_successful_solutions()


