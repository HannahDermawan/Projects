"""
for x in range(n), for x in []


lst = [1,2,3,4,5]
for item in lst : 
    print(item)

answer = 0
for item in range(100): #range() only accepts integers
    answer = answer + item + 1
print(answer)
"""

#EXERCISE
"""
Activity: Create a script which asks for a number and then calculates the factorial of that number
    E.g: If the number entered was 4, then print the number 24 because 4!=4*3*2*1=24. Note: 0!=1
If the user entered something other than "0" or a positive integer, print("Invalid response") and ask again
    i.e: Do not accept negative numbers, decimal numbers or letters
If the user entered a number larger than 100000 (one hundred thousand), print("Number too large") and ask again

Hint: Create a list of all the numbers to multiply together, then use a for loop to find the product of the numbers in the list

"""

numbervalid = False

while numbervalid == False :
    number = input("Please enter the number you want to find the factorial of: ")
    try:
        number = int(number)
        if number < 0:
            print("Invallid response")

        elif number > 100000 :
            print("Number too large")

        else :
            numbervalid = True
    except:
        print("Invalid response")

lst = [] #Creates list in a variable 
for i in range(number) : 
    lst.append(i+1) 
    #lst.append(i) 0,1,2 
    #lst.append(i+1) --> 1,2,3
print(lst)
#print(len(lst)) #len counts the number of items in the list
"""
Alternative way of creating list of items to multiply:
lst = []
while number > 0:
    lst.append(number) #Appends the number to the list
    number -= 1 #Increments the number down by one to add the next number to the list
"""

output = 1 #Initializes output variable as 1
for item in lst:
    output = item * output 
    #Iterates through the list and multiplies each of the items to the product of all previous items in the list

print(output) #Prints output

