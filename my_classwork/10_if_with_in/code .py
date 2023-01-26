"""Python refresher course - If with In Section"""

shows_watched = {"That 90's Show", "Only Murders in the Building", "Abbott Elementary"}
user_show = {"Beavis & Butthead"}

if user_show in shows_watched:
    print(f"I've watched {user_show} too!")
else:
    print(f"I haven't seen {user_show} yet. Bummer!")
    

# guessing number game
number = 9
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: ")) # user puts in 8
    if user_number == number:
        print("You guessed it!")
    elif number - user_number in (1, -1): # if the result of 9 - 8 is in the provided tuple, print this
        print("You're only off by 1!")
    else:
        print("Sorry, kiddo. No dice!")