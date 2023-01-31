"""Python refresher course - List Comprehension Section"""

numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)
    
print(doubled)


# below is the same thing using LINE COMPREHENSION
digits = [7, 9, 11]
doubled_digits = [digit * 2 for digit in digits]

print(doubled_digits)


# another example with a for loop
friends = ["Stephanie", "Gidget", "Sylvie", "Sophie", "Viola" ]
starts_s = []

for friend in friends:
    if friend.startswith("S"): # more fun methods
        starts_s.append(friend)
        
print(starts_s)


# above now with list comprehension which creates a NEW list even if the elements are the same 
friends = ["Stephanie", "Gidget", "Sylvie", "Sophie", "Viola" ]
starts_s = [friend for friend in friends if friend.startswith("S")] # adds the conditional at the end
 
print(starts_s)