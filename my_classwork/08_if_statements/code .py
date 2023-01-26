"""Python refresher course - If Statements Section"""

# i'm not using input() because my console won't let me type answers, so the mood variable can be changed
mood = "happy"

if mood == "tired":
    print("You should take a nap.")
elif mood == "sad":
    print("You should go outside for a couple minutes.")
else:
    print("You're great company today.")
    
    
# when using input(), you can also use the .lower() method too to ensure that whatever case the user types in, matches your if/else arguments:
my_mood = input("Tell me about your mood: ").lower()

if mood == "tired":
    print("You should take a nap.")
elif mood == "sad":
    print("You should go outside for a couple minutes.")
else:
    print("You're great company today.")

# this way, if the user types in Tired or tired, you'll get the correct response
