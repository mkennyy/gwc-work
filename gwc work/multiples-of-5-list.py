# a function that takes in a list of numbers and prints all the multiples of 5 in the list
numbersList = [0, 1, 3, 10, 15, 17, 20, 25, 26]
def multiples(aList):

    # prints all multiples of 5
    for number in aList:
        if number % 5 == 0:
            print(number)
        #else:
            #print(False)
        # check if the number is divisible by 5 with remainder 0
        # print(number)
multiples(numbersList)
