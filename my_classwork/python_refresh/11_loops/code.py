"""Python refresher course - Loops Section"""

# we're doing this same number guessing game but this time, the code will loop until a correct answer is found
# instead of our if statement, we're going to let the user play the game as long as their answer is NOT 'n' - perfect for a WHILE loop!

number = 9

while True: # instead of while user_input != "n"
    user_input = input("Would you like to play? (Y/n) ") # (Y/n) is common - have to press n to stop 
    
    if user_input == "n": #add this if answer is no so you don't have infinite loop!
        break
  
    user_number = int(input("Guess our number: ")) # user puts in 8
    if user_number == number:
        print("You guessed it!")
    elif number - user_number in (1, -1): # if the result of 9 - 8 is in the provided tuple, print this
        print("You're only off by 1!")
    else:
        print("Sorry, kiddo. No dice!")
        
        
# basic for loop
friends = ["Minnie", "Darlinda", "Cookie", "GiGi"]

for friend in friends:
    print(f"{friend} is one of my favorite people!")
 
    
# this for loop will help us calculate an avg grade for a class
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades) # counts the # of grades aka 5

for grade in grades:
    total += grade # same as <total = total + grade> • adds up the existing total plus the new grade & sets it back to total

print(total / amount) # this equation gives us the average


# you can also do the above WITHOUT a for loop!
grades = [35, 67, 98, 100, 100]
total = sum(grades) # get you the sum of all grades
amount = len(grades) # counts the # of grades aka 5

print(total / amount) # BAM
